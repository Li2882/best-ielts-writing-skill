"""Check local inputs without invoking models or accessing the network."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check():
    lock = ROOT / '.agents/skills/ielts-writing-review-final/references/baseline-lock.json'
    if not lock.is_file():
        return {'ready_for_initial_scoring': False, 'missing': [str(lock.relative_to(ROOT))]}
    data = json.loads(lock.read_text(encoding='utf-8-sig'))
    missing, changed = [], []
    for row in data['files']:
        path = ROOT / row['path']
        if not path.is_file():
            missing.append(row['path'])
        elif hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            changed.append(row['path'])
    if not (ROOT / 'library/index.json').is_file():
        missing.append('library/index.json')
    records = {'task1': 0, 'task2': 0}
    for task in records:
        folder = ROOT / 'library' / task
        if folder.is_dir():
            for path in folder.glob('*.json'):
                row = json.loads(path.read_text(encoding='utf-8-sig'))
                if row.get('status') == 'verified' and row.get('split') == 'reference':
                    records[task] += 1
    return {
        'ready_for_initial_scoring': not missing and not changed,
        'missing': missing,
        'hash_mismatches': changed,
        'verified_reference_records': records,
        'calibration_ready': 'not established by this file check',
        'note': 'Actual criterion quotas, chart availability, source rights and reading must still be verified. This check is not an accuracy test.'
    }


if __name__ == '__main__':
    result = check()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['ready_for_initial_scoring'] else 2)
