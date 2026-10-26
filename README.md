# Kenyan Swahili AI Evaluation

**Focus:** evaluation design for Kenyan Kiswahili, code-switching, context, naturalness, meaning, grammar and audience fit.

## Why this matters
Generic language-model benchmarks can obscure local register, mixed-language usage and cultural relevance. Evaluation should distinguish **formal Kiswahili**, conversational Kenyan Kiswahili and context-appropriate code-switching without assuming one variety is universally preferable.

This project is a **prototype rubric and synthetic item set**, not a representative dataset of Kenyan speakers and not a certified linguistic gold standard.

## Evaluation dimensions
| Dimension | Question for human reviewers |
|---|---|
| Meaning preservation | Is the intended meaning retained? |
| Grammar | Is the wording grammatical for the intended register? |
| Naturalness | Would this sound plausible to an intended Kenyan audience? |
| Context | Does it respond appropriately to the scenario and social relationship? |
| Code-switching | Is mixing languages appropriate, neither forced nor unfairly penalized? |
| Cultural fit | Are idiom, politeness and local references contextually sound? |

Each dimension uses a 0–3 scale. Scores are **illustrative provisional labels**, not validated findings.

## Run
```bash
python -m src.rubric
python -m unittest discover -s tests -v
```

## Responsible benchmark design
1. Recruit native Kenyan Kiswahili reviewers representing multiple registers and demographics.
2. Obtain explicit permission for all original speech/text; avoid scraping private chats.
3. Record consent, anonymization strategy and provenance.
4. Include formal, informal and code-switched contexts with stratified item coverage.
5. Perform blind double annotation, calibration and adjudication.
6. Report disagreements and subgroup limitations, not just one aggregate score.
7. Evaluate errors at meaning level, not solely spelling or word matching.

## Suggested expansion
Add consented speech recordings and human transcription review, dialect/register labels, error taxonomy, rater agreement and an analysis notebook. **No audio recordings or transcription benchmark are supplied here**; 'transcription' is a proposed extension.

## Skills demonstrated
Swahili localization QA · Multilingual LLM evaluation · Rubric development · Register analysis · Code-switching · Dataset governance

# Scope and evidence

This is a **synthetic, independently developed demonstration**, not a reproduction of confidential employer data. All prompts, labels, examples, names and records are fabricated for demonstration. Sample counts and test outcomes are software demonstrations, **not historical workplace impact statistics**.

The repository demonstrates evaluation methodology and runnable code; it does not certify that the author achieved a specific result at a named client.

