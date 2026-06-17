# 📄 YAML — Practice Lab

> A **clone-and-go** lab to quickly refresh YAML and practise the configs you write every day in DevOps: Kubernetes manifests, GitHub Actions, Docker Compose, and more. Comes with a tiny validator so you get instant feedback.

[![YAML](https://img.shields.io/badge/Format-YAML-CB171E.svg?logo=yaml&logoColor=white)](https://yaml.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 Why this repo?

YAML looks easy until a single wrong space breaks your pipeline or your Kubernetes deploy. This lab gives you a fast refresher, a set of **broken files to fix**, and **write-from-scratch** tasks for real DevOps configs — with a `check.py` script that tells you immediately whether your YAML is valid.

## 🗂️ What's inside

```
yaml-practice-lab/
├── README.md                 ← you are here
├── CHEATSHEET.md             ← 1-page YAML reminder + the common gotchas
├── CONTRIBUTING.md           ← how to add your own exercises
├── requirements.txt          ← just PyYAML (used by check.py)
├── check.py                  ← validate any YAML file and see its structure
├── 01-yaml-basics/           ← refresher: scalars, lists, maps, types, anchors
│   └── README.md
├── 02-fix-the-yaml/          ← 3 broken files to repair
│   ├── README.md
│   ├── broken-1-indentation.yaml
│   ├── broken-2-quotes.yaml
│   ├── broken-3-structure.yaml
│   └── solutions/
└── 03-write-devops-configs/  ← write real configs from a spec
    ├── README.md
    ├── exercise-1-k8s-deployment.md
    ├── exercise-2-github-actions.md
    ├── exercise-3-docker-compose.md
    └── solutions/
```

## ✅ Requirements

- **Python 3.8+** and **PyYAML** (the only dependency, used by `check.py`).

```bash
pip install -r requirements.txt
```

## 🚀 Quick start

```bash
# 1. Get the code
git clone https://github.com/shubhs248/yaml-practice-lab.git
cd yaml-practice-lab

# 2. Install the one dependency
pip install -r requirements.txt

# 3. Check any YAML file — valid or broken — and see what's wrong
python check.py 02-fix-the-yaml/broken-1-indentation.yaml
```

`check.py` prints a clear error (with the line/column) if the file is invalid, or a short summary of the structure if it is valid.

## 🧭 Suggested path (about 60 minutes)

| # | Part | What you practise | Time |
|---|------|-------------------|------|
| 1 | [YAML Basics](01-yaml-basics/README.md) | scalars, lists, maps, types, multiline, anchors, multi-doc | 20 min |
| 2 | [Fix the YAML](02-fix-the-yaml/README.md) | spotting & repairing real YAML errors | 20 min |
| 3 | [Write DevOps Configs](03-write-devops-configs/README.md) | K8s, GitHub Actions, Docker Compose from a spec | 20 min |

## 📝 How each part works

- **Part 1** is a refresher: read it, try the tasks, check the answers at the bottom.
- **Part 2** gives you broken files. Run `python check.py <file>`, read the error, fix the file until it passes. Compare with `solutions/`.
- **Part 3** gives you a written spec; you create the YAML, validate it with `python check.py`, then compare with `solutions/`.

---

## 🎤 Prepping for an interview?

After you've done the exercises, open **[INTERVIEW-QUESTIONS.md](INTERVIEW-QUESTIONS.md)** — the YAML questions interviewers actually ask (including all the gotchas), in plain English with short answers you can say out loud and spot-the-bug drills.

---

## ⭐ Found this useful?

- **Star** ⭐ the repo so more people discover it.
- **Fork** 🍴 it and practise on your own copy.
- **Share** 🔗 it on LinkedIn and tag me — I would love to see your progress.
- **Contribute** 🤝 a new exercise or fix. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 👋 About the author

Made with care by **Shubham Sharma**.

- GitHub: [github.com/shubhs248](https://github.com/shubhs248)
- LinkedIn: [linkedin.com/in/shubhs248](https://www.linkedin.com/in/shubhs248)

## 📜 License

MIT — free to use, fork, teach with, and share. A star ⭐ or a tag on LinkedIn is always appreciated!
