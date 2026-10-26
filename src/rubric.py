"""Human-rated language evaluation; not an automated Kiswahili correctness model."""
import json
from pathlib import Path
DIMENSIONS=('meaning','grammar','naturalness','context','code_switching','cultural_fit')
DESCRIPTIONS={0:'Not acceptable for the intended audience',1:'Partially acceptable; substantive edit needed',2:'Acceptable with minor issues',3:'Strong for this context'}

def validate_review(review):
    issues=[]
    for key in DIMENSIONS:
        score=review.get('scores',{}).get(key)
        if not isinstance(score,int) or isinstance(score,bool) or score not in range(4):
            issues.append(f'{key}: score must be integer 0..3')
    if not review.get('rationale'):issues.append('rationale required')
    if not review.get('register'):issues.append('register required')
    return issues

def summarize(review):
    problems=validate_review(review)
    if problems:return {'id':review.get('id'),'errors':problems}
    return {'id':review['id'],'average':round(sum(review['scores'].values())/len(DIMENSIONS),2),
            'dimensions':review['scores'],'human_review_required':True}

if __name__=='__main__':
    for review in json.loads(Path('data/reviews.json').read_text(encoding='utf-8')):
        print(json.dumps(summarize(review),ensure_ascii=False))
