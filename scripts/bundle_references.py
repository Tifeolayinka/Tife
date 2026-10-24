#!/usr/bin/env python3
"""Copy only each skill's declared references, making every folder portable."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bundle(root=ROOT, check=False):
    manifest = json.loads((root / 'shared/manifest.json').read_text())
    errors = []
    for name, refs in manifest.items():
        if Path(name).name != name:
            raise ValueError('Invalid skill directory name')
        destination = root / 'skills' / name / 'references'
        expected = set(refs)
        for reference in refs:
            if Path(reference).name != reference:
                raise ValueError('Invalid reference filename')
            source = root / 'shared' / reference
            target = destination / reference
            content = source.read_bytes()
            if check:
                if not target.is_file() or target.read_bytes() != content:
                    errors.append(f'{name}: missing or stale {reference}')
            else:
                destination.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
        if destination.exists():
            for target in destination.iterdir():
                if target.name not in expected:
                    errors.append(f'{name}: undeclared reference {target.name}; remove deliberately')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    findings = bundle(check=args.check)
    if findings:
        raise SystemExit('\n'.join(findings))
    print('Bundled references are current.' if args.check else 'References bundled.')
