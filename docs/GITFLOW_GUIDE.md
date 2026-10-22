# Gitflow guide

Branches: `main` (production), `develop` (integration), `feature/*`, `release/*`, `hotfix/*`.

## Initialize and push
```bash
git init
git add .
git branch -M main
git commit -m "chore: initial project"
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
git checkout -b develop
git push -u origin develop
```

## Feature -> PR
```bash
git checkout develop
git checkout -b feature/add-greeting
# edit code/tests
python -m pytest -q
git add .
git commit -m "feat: add greeting behavior"
git push -u origin feature/add-greeting
```
Open a PR from feature branch into develop, review, then merge on GitHub.

## Release
```bash
git checkout develop
git checkout -b release/1.0.0
python -m pytest -q
git checkout main
git merge --no-ff release/1.0.0
git tag -a v1.0.0 -m "Release 1.0.0"
git checkout develop
git merge --no-ff release/1.0.0
```

## Hotfix
```bash
git checkout main
git checkout -b hotfix/1.0.1
# make a fix and update tests
python -m pytest -q
git add .
git commit -m "fix: correct production behavior"
git checkout main
git merge --no-ff hotfix/1.0.1
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git checkout develop
git merge --no-ff hotfix/1.0.1
```

## Hooks
Enable in Git Bash with `git config core.hooksPath .githooks`. On Windows, scripts need LF endings and executable behavior; you can run the hook commands manually if Git Bash does not execute them.
