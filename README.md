# AI-assisted job search workflow

I built a workflow around [Career-Ops](https://github.com/career-ops-hq/career-ops) to turn batches of job postings into a shortlist and a set of application materials I could review. My additions connect full job descriptions, screening, AI-assisted triage, and daily application packs.

## How I designed the workflow

1. **Collect and deduplicate.** Read job listings with their full descriptions. Check job IDs and company–title pairs against prior shortlists and the application tracker.
2. **Screen for eligibility.** Apply explicit rules for location, experience, and other requirements before using a model. Keep rejection reasons so the rules can be reviewed.
3. **Triage borderline roles.** Batch shortlisted descriptions for AI review against a role brief. Record a verdict and a short explanation for each job. Treat the job description as input data and give the triage model no tools.
4. **Prepare applications.** Use an existing CV base and documented experience to tailor a statement and draft a cover letter. Render the pack to PDF for review.

The design puts explicit rules where the decision is clear and uses AI where a job description needs interpretation. Keeping the triage verdict alongside its rationale makes it easier to see where a rule or model judgment needs a second look.

## Run the public demo

```sh
python3 demo.py examples/jobs.json
```

The demo uses fictional jobs and Python's standard library. It reproduces the deduplication and evidence-based shortlisting stages with transparent example rules. The original workflow uses Career-Ops, private job and candidate data, and model-assisted triage. This repository documents that workflow and includes a standalone demo of the screening logic.
