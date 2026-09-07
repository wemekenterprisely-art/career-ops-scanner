# ScholarSpace-ships 2027 — World Map v3 handoff

A complete implementation patch was built against `wemekenterprisely-art/scholar-space-ships-2027` commit `9f2c7ab`.

## Why this is a handoff patch

This Arena session is attached to `wemekenterprisely-art/career-ops-scanner`. The agent can read `scholar-space-ships-2027`, but GitHub denied write access to that separate repository:

```text
remote: Permission to wemekenterprisely-art/scholar-space-ships-2027.git denied to arena-ai-coding-agent[bot].
fatal: unable to access 'https://github.com/wemekenterprisely-art/scholar-space-ships-2027.git/': The requested URL returned error: 403
```

Open a new Arena session directly on `wemekenterprisely-art/scholar-space-ships-2027`, then apply:

```bash
git am handoff/scholar-space-ships-2027-world-map-v3.patch
python -m compileall -q .
python test_filters.py && python scholar_ollama_test.py && python test_national_programs.py && python test_world_map.py
python world_map.py refresh
python scanner.py --tier 1 --skip-ai
```

## What the patch adds

- `data/world_universities.json` — MIT-licensed Hipo University Domains snapshot.
- `world_map.py` — normalizes world university data, creates summaries, and plans official scholarship/funding URLs.
- `fetchers/world_university_map.py` — optional tier-3 source inventory.
- Scanner integration — every scan emits world-map JSON outputs.
- Excel integration — adds **World Country Map** and **World University Map** sheets.
- API endpoints — `/api/world-map`, `/api/world-summary`, `/api/university-sources`.
- Dashboard KPIs/table for mapped countries/universities.
- State sync — persists compact `world_map_summary.json` and `university_sources.json`.
- Tests — `test_world_map.py` + fixed `test_national_programs.py`; workflows run both.

## Verified locally

- Dataset coverage: 10,259 universities, 201 countries.
- Libya: 11 universities.
- Planned source inventory: 500 universities, 5,500 official scholarship/funding candidate URLs.
- Local scan with `--skip-ai`: workbook created with 7 sheets.
- Tests passed: filters, scholarship gates, national registry, world map.
