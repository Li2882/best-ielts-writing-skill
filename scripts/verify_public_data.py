"""Recompute published metrics; this is a numerical audit, not a model evaluation."""
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))


def main():
    current=read('research-data/current-evaluation.json')
    external=read('research-data/external-benchmark.json')
    checked=0
    for group in ('all','task1','task2'):
        rows=[r for r in current['per_essay'] if group=='all' or r['task']==group]
        for stage in ('initial','final'):
            errors=[r[stage+'_overall']-r['human_overall'] for r in rows]
            n=len(errors)
            metrics={'n':n,'MAE':sum(abs(x) for x in errors)/n,
                     'RMSE':math.sqrt(sum(x*x for x in errors)/n),'mean_bias':sum(errors)/n,
                     'exact_match':sum(x==0 for x in errors)/n,
                     'within_half_band':sum(abs(x)<=0.5 for x in errors)/n,
                     'max_absolute_error':max(abs(x) for x in errors)}
            for key,value in metrics.items():
                assert math.isclose(value,current['overall'][group][stage][key],abs_tol=1e-10),(group,stage,key)
                checked+=1
    buckets=defaultdict(list)
    for row in external['rows']:
        for c in ('task_response','CC','LR','GRA'):
            buckets[row['prompt_id']].append(abs(row['predicted'][c]-row['target'][c]))
    for summary in external['summary']:
        errs=buckets[summary['prompt_id']]
        assert abs(sum(errs)/len(errs)-summary['overall']['four_trait_mae'])<=0.00051,summary['name']
        checked+=1
    for r in current['per_essay']:
        for stage in ('initial','final'):
            scores=list(r[stage+'_traits'].values())
            assert len(scores)==4
            display=math.floor(sum(scores)/4*2+0.5)/2
            assert display==r[stage+'_overall'],(r['id'],stage)
            checked+=1
    print(json.dumps({'checks_passed':checked,'current_N':len(current['per_essay']),
                      'external_prompt_count':len(external['summary']),
                      'MAE':current['overall']['all']['final']['MAE'],
                      'within_half_band':current['overall']['all']['final']['within_half_band'],
                      'current_head_to_head_superiority_established':False,
                      'new_model_calls':0},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
