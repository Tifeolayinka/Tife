#!/usr/bin/env python3
"""Install self-contained skill folders without overwriting existing skills."""
import argparse
import json
import shutil
import tempfile
from pathlib import Path

from bundle_references import ROOT
from validate import validate


def install(target, root=ROOT, dry_run=False):
    errors = validate(root)
    if errors:
        raise ValueError('Source validation failed:\n' + '\n'.join(errors))
    target = Path(target).expanduser().resolve()
    names = list(json.loads((root / 'shared/manifest.json').read_text()))
    # Check every destination before writing any skill. A dangling symlink is a collision too.
    collisions = [str(target / name) for name in names
                  if (target / name).exists() or (target / name).is_symlink()]
    if collisions:
        raise FileExistsError('Refusing to overwrite existing destinations:\n' + '\n'.join(collisions))
    if target.exists() and not target.is_dir():
        raise NotADirectoryError(target)
    if dry_run:
        return [str(target / name) for name in names]
    target.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        with tempfile.TemporaryDirectory(prefix='.tife-install-', dir=target) as staging:
            for name in names:
                shutil.copytree(root / 'skills' / name, Path(staging) / name)
            for name in names:
                destination = target / name
                # mkdir is exclusive: never replace a directory created since the preflight.
                destination.mkdir()
                created.append(destination)
                shutil.copytree(Path(staging) / name, destination, dirs_exist_ok=True)
    except Exception:
        for destination in reversed(created):
            shutil.rmtree(destination)
        raise
    return [str(path) for path in created]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, help='Host skill directory, e.g. ~/.codex/skills')
    parser.add_argument('--dry-run', action='store_true', help='Validate and preview without writing')
    args = parser.parse_args()
    try:
        paths = install(args.target, dry_run=args.dry_run)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'{exc}\n')
    print(('Would install' if args.dry_run else 'Installed') + f' {len(paths)} skills:')
    print('\n'.join(paths))
