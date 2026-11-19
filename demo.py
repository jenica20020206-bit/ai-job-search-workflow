"""Show deterministic screening with fictional job postings."""
import json
import sys
from pathlib import Path


def screen(jobs, skills):
    seen = set()
    results = []
    for job in jobs:
        key = tuple(job[field].strip().casefold() for field in ("company", "title"))
        requirements = set(job["required_skills"])
        matched = sorted(requirements & skills)
        gaps = sorted(requirements - skills)
        if key in seen:
            verdict = "duplicate"
        elif job["location"] != "London":
            verdict = "outside target location"
        elif job["minimum_years"] > 1:
            verdict = "experience requirement"
        elif gaps:
            verdict = "review"
        else:
            verdict = "shortlist"
        seen.add(key)
        results.append({"job_id": job["id"], "verdict": verdict,
                        "matched_skills": matched, "skill_gaps": gaps})
    return results


if __name__ == "__main__":
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(screen(data["jobs"], set(data["candidate_skills"])), indent=2))
