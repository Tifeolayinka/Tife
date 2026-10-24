#!/usr/bin/env python3
"""Validate portable skill packaging with Python's standard library."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

from bundle_references import ROOT, bundle


def metadata(path):
    text = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError(f'{path.name}: missing frontmatter')
    fields = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(':')
        if not sep:
            raise ValueError('Invalid frontmatter line')
        value = value.strip()
        fields[key] = json.loads(value) if value.startswith('"') else value
    return fields


def validate(root=ROOT):
    errors = []
    manifest = json.loads((root / 'shared/manifest.json').read_text())
    actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if actual != set(manifest):
        errors.append('Skill folders and reference manifest disagree')
    errors.extend(bundle(root, check=True))
    for name in manifest:
        folder = root / 'skills' / name
        try:
            fields = metadata(folder / 'SKILL.md')
            if fields.get('name') != name or not re.fullmatch(r'[a-z0-9-]{1,63}', name):
                errors.append(f'{name}: invalid or mismatched name')
            if not fields.get('description') or len(fields['description']) > 1024:
                errors.append(f'{name}: invalid description')
            ui = (folder / 'agents/openai.yaml').read_text()
            for key in ('display_name', 'short_description', 'default_prompt'):
                line = re.search(rf'^  {key}: (.+)$', ui, re.M)
                value = json.loads(line[1]) if line else ''
                if not value:
                    errors.append(f'{name}: missing {key}')
                if key == 'short_description' and not 25 <= len(value) <= 64:
                    errors.append(f'{name}: short description must be 25–64 characters')
                if key == 'default_prompt' and f'${name}' not in value:
                    errors.append(f'{name}: default prompt missing invocation')
            for doc in folder.rglob('*.md'):
                for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', doc.read_text()):
                    if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                        continue
                    path = (doc.parent / unquote(target.split('#')[0])).resolve()
                    if not path.is_relative_to(folder.resolve()):
                        errors.append(f'{name}: nonportable link {target}')
                    elif not path.is_file():
                        errors.append(f'{name}: broken link {target}')
        except (OSError, ValueError, KeyError) as exc:
            errors.append(f'{name}: {exc}')
    plugin = json.loads((root / '.claude-plugin/plugin.json').read_text())
    if set(plugin.get('skills', [])) != {'./skills/' + n for n in manifest}:
        errors.append('Plugin manifest does not enumerate exactly the packaged skills')
    for path in root.rglob('*'):
        if path.is_symlink():
            errors.append(f'Symlinks are not portable: {path.relative_to(root)}')
    return errors


if __name__ == '__main__':
    findings = validate()
    if findings:
        raise SystemExit('\n'.join(findings))
    print('Validated all 9 skills: metadata, local links, references, and plugin manifest.')
