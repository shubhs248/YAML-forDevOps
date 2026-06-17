# Exercise 3.2 — GitHub Actions Workflow

**You write:** a CI workflow for GitHub Actions.

---

## 📋 The spec
Create a file (e.g. `ci.yaml`) describing a workflow with:

- a `name`: `CI`
- it runs `on` push **and** pull_request to the `main` branch
- one **job** called `build` that:
  - runs on `ubuntu-latest`
  - has these **steps** (a list):
    1. uses `actions/checkout@v4`
    2. uses `actions/setup-python@v5` with `python-version: "3.12"`
    3. a step named `Install deps` that runs `pip install -r requirements.txt`
    4. a step named `Run tests` that runs `pytest`

## ✅ How to check
```bash
python check.py ci.yaml      # must say [VALID]
```
Then compare with [`solutions/github-actions.yaml`](solutions/github-actions.yaml).

## 💡 Hints
- `on` can be a map: `push:` and `pull_request:` each with a `branches` list.
- ⚠️ Remember the YAML gotcha: the word `on` is fine as a key here, but if a parser ever turns it into a boolean, quote it as `"on"`.
- Each step is an item in a list (`- uses: ...` or `- name: ... \n  run: ...`).
- `with` is a map of inputs under a `uses` step.

> Bonus once it parses: lint it with `actionlint`.
