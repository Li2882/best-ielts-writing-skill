"""Import an existing authorized local corpus; no downloads, overwrites or uploads."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_EXTENSIONS = {'.json', '.md', '.txt', '.py', '.yaml', '.yml', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.pdf', '.html', '.csv'}


def contained(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f'Path escapes the source project: {value}')
    return path


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--from', dest='source', required=True, type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    source = args.source.resolve()
    if source == ROOT:
        raise SystemExit('Source and destination must differ.')
    if not (source / 'library/index.json').is_file():
        raise SystemExit('The source must contain library/index.json.')
    paths = {p.relative_to(source).as_posix() for p in (source / 'library').rglob('*')
             if p.is_file() and not p.is_symlink() and p.suffix.lower() in ALLOWED_EXTENSIONS}
    for path in (source / 'library').rglob('*.json'):
        value = json.loads(path.read_text(encoding='utf-8-sig'))
        for text in strings(value):
            if text.startswith('research/') and contained(source, text).is_file():
                if Path(text).suffix.lower() in ALLOWED_EXTENSIONS:
                    paths.add(text)
    plans = []
    for rel in sorted(paths):
        src = contained(source, rel)
        # Research source assets are private local dependencies, not research publication files.
        dst = contained(ROOT, rel)
        if src.is_symlink():
            continue
        if dst.exists():
            if hashlib.sha256(dst.read_bytes()).digest() != hashlib.sha256(src.read_bytes()).digest():
                raise SystemExit(f'Refusing to overwrite a different file: {rel}')
            continue
        plans.append((src, dst))
    if not args.dry_run:
        for src, dst in plans:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    print(json.dumps({'files_to_copy' if args.dry_run else 'copied_files': len(plans),
                      'destination': str(ROOT), 'uploads': 0, 'model_calls': 0}, ensure_ascii=False))


if __name__ == '__main__':
    main()
