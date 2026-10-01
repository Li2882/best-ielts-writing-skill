"""Export numeric research records using explicit allowlists; no essay text or credentials."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def save(path, value):
    if path.exists():
        raise FileExistsError(f'Refusing to replace existing research export: {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    current_rel = 'evaluations/integer28-current-01/results.json'
    external_rel = 'evaluations/strict-public-prompts-01/REPORT.json'
    manifest_rel = 'library/prompts/public-benchmark-strict-10/manifest.json'
    current = read(source/current_rel)
    external = read(source/external_rel)
    manifest = read(source/manifest_rel)
    per_essay_fields = ('id','source_id','task','initial_traits','final_traits','human_traits',
                        'initial_overall','final_overall','human_overall','source_url')
    rows = [{k:r.get(k) for k in per_essay_fields} for r in current['per_essay']]
    public_current = {k:current.get(k) for k in ('run_id','compared_at','n','pair_comparisons',
                       'overall','criterion_metrics','per_band','caveats','scoring_configuration')}
    public_current['per_essay'] = rows
    public_current['model_configuration'] = read(source/'evaluations/integer28-current-01/scoring-runtime.json')
    public_current['metric_definition'] = 'Absolute error of the displayed single-essay overall band against the source-published overall label; public development regression, not fresh blind validation.'
    external_rows = [{k:r[k] for k in ('prompt_id','prompt_name','group','case_id','task','target','predicted')}
                     for r in external['rows']]
    public_external = {
        'date':external['date'], 'protocol':read(source/'evaluations/strict-public-prompts-01/protocol.json'),
        'summary':external['summary'], 'rows':external_rows,
        'metric_definition':'Mean absolute error across the four separately labelled criteria, not the overall band.'
    }
    source_ids={r['source_id'] for r in rows}
    common_ids=sorted(source_ids & {r['case_id'] for r in external_rows})
    assert len(common_ids)==1, f'Recheck written comparability statement: {common_ids}'
    public_external['overlap_with_current_evaluation'] = {
        'common_original_ids':common_ids,'n':len(common_ids),
        'supports_current_head_to_head_lead_claim':False
    }
    save(ROOT/'research-data/current-evaluation.json',public_current)
    save(ROOT/'research-data/external-benchmark.json',public_external)
    deps=[]
    for r in manifest['qualified']:
        if r['id'] in ('02-gishguo-claude-skill','04-quyen244-ai-evaluator'):
            deps.append({k:r[k] for k in ('id','name','repo','files')})
    lock=read(source/'.agents/skills/ielts-writing-review-final/references/baseline-lock.json')
    save(ROOT/'research-data/dependencies.json',{
        'initial_source_packages':deps,
        'locked_files':lock['files'],
        'official_standard_url':'https://ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf',
        'note':'Manifest only. Obtain authorized copies locally. Full third-party prompts, descriptor copies, essays, charts and paid reviews are not republished in this package.'
    })
    records=[]
    for task in ('task1','task2'):
        for path in sorted((source/'library'/task).glob('*.json')):
            r=read(path)
            if r.get('status')=='verified' and r.get('split')=='reference':
                records.append({k:r.get(k) for k in ('id','task','source_url','publisher','score_source','label_scope','traits','overall')})
    save(ROOT/'research-data/reference-sources.json',{
        'purpose':'Source metadata only, not a redistributable corpus or a promise that every source is free.',
        'records':records
    })
    reviewed_files=[current_rel,external_rel,manifest_rel,
                    'evaluations/composite-holdout-01/REPORT.md',
                    'evaluations/lr-independent-deduction-ablation-01/REPORT.md',
                    'docs/final-skill-modification-record.md']
    save(ROOT/'research-data/provenance.json',{
        'export_date_local':'2026-10-02','workflow_version':'final-composite-1.4',
        'input_hashes':[{'path':p,'sha256':hashlib.sha256((source/p).read_bytes()).hexdigest()} for p in reviewed_files],
        'publication_allowlist':'Own workflow instructions, short authorized review excerpts, numeric predictions and human labels, source links, public documentation, own visual assets and utilities.',
        'excluded':'Private essays, screenshots of full third-party works, books, teacher comment corpus, credentials, settings, payment data and raw runtime logs.',
        'skill_copied_without_scoring_rule_changes':True
    })
    print(json.dumps({'exported_current_essays':len(rows),'external_predictions':len(external_rows),
                      'common_originals':common_ids,'reference_metadata_records':len(records)},ensure_ascii=False))


if __name__=='__main__':
    main()
