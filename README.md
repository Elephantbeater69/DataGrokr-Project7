# DataGrokr Week 7 — Full Gitflow Simulation

## Contents
- `app.py`, `test_app.py` — sample app and unit tests
- `.githooks/` — pre-commit and commit-msg hook examples
- `.github/workflows/ci.yml` — GitHub Actions CI
- `docs/GITFLOW_GUIDE.md` — feature -> PR -> release -> hotfix walkthrough

## Run locally
```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```

## Enable hooks
```bash
git config core.hooksPath .githooks
```
Gitflow branch names and PR/release steps are documented in `docs/GITFLOW_GUIDE.md`.
The ZIP cannot include live GitHub PRs or branches; create those after pushing to your own repository.
