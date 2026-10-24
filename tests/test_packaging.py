import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import install as installer
from validate import validate


class PackagingTests(unittest.TestCase):
    def test_distribution_is_valid(self):
        self.assertEqual(validate(ROOT), [])

    def test_fresh_install_is_portable_and_preserves_unrelated_files(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'skills'
            target.mkdir()
            sentinel = target / 'unrelated.txt'
            sentinel.write_text('keep')
            destinations = installer.install(target)
            manifest = json.loads((ROOT / 'shared/manifest.json').read_text())
            self.assertEqual(len(destinations), len(manifest))
            self.assertEqual(sentinel.read_text(), 'keep')
            for name, refs in manifest.items():
                folder = target / name
                self.assertTrue((folder / 'SKILL.md').is_file())
                for reference in refs:
                    self.assertEqual((folder / 'references' / reference).read_bytes(),
                                     (ROOT / 'shared' / reference).read_bytes())

    def test_collision_preflight_writes_nothing(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            existing = target / 'tife-update-thread'
            existing.mkdir()
            (existing / 'custom.md').write_text('custom content')
            before = sorted(str(p.relative_to(target)) for p in target.rglob('*'))
            with self.assertRaises(FileExistsError):
                installer.install(target)
            self.assertEqual(before, sorted(str(p.relative_to(target)) for p in target.rglob('*')))
            self.assertEqual((existing / 'custom.md').read_text(), 'custom content')

    def test_dry_run_does_not_create_target(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'missing'
            self.assertEqual(len(installer.install(target, dry_run=True)), 9)
            self.assertFalse(target.exists())

    def test_dangling_symlink_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            link = target / 'tife-create-thread'
            link.symlink_to(target / 'missing')
            with self.assertRaises(FileExistsError):
                installer.install(target)
            self.assertTrue(link.is_symlink())

    def test_failed_copy_rolls_back_only_new_skill_folders(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / 'keep.txt').write_text('keep')
            original = shutil.copytree

            def failing_copy(source, destination, *args, **kwargs):
                if Path(destination).resolve() == (target / 'tife-update-context').resolve():
                    raise OSError('simulated disk failure')
                return original(source, destination, *args, **kwargs)

            with patch.object(installer.shutil, 'copytree', side_effect=failing_copy):
                with self.assertRaises(OSError):
                    installer.install(target)
            self.assertEqual([p.name for p in target.iterdir()], ['keep.txt'])

    def test_corrupt_bundle_is_rejected_before_install(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'source'
            shutil.copytree(ROOT / 'skills', root / 'skills')
            shutil.copytree(ROOT / 'shared', root / 'shared')
            shutil.copytree(ROOT / '.claude-plugin', root / '.claude-plugin')
            (root / 'skills/tife-create-thread/references/workflow.md').write_text('stale')
            target = Path(temp) / 'target'
            with self.assertRaises(ValueError):
                installer.install(target, root=root)
            self.assertFalse(target.exists())


if __name__ == '__main__':
    unittest.main()
