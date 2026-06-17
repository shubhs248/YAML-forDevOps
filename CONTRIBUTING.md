# 🤝 Contributing

Thanks for thinking about helping out! This is a learning project, so contributions of every size are welcome — even fixing a typo.

If this repo helped you, the easiest way to support it is to **star** ⭐ it, **fork** 🍴 it, and **share** 🔗 it on LinkedIn so others can find it too.

## Ways you can help

- **Fix something** — a typo, a broken link, or a wrong answer.
- **Add a broken file** — another realistic YAML mistake for people to spot and fix.
- **Add a write-from-spec task** — another real DevOps config (Ansible, Helm values, Prometheus rules, etc.).
- **Improve `check.py`** — clearer messages, schema checks, etc.

## How to contribute (step by step)

1. **Fork** this repo to your own GitHub account.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/yaml-practice-lab.git
   cd yaml-practice-lab
   pip install -r requirements.txt
   ```
3. **Create a branch**:
   ```bash
   git switch -c add-ansible-task
   ```
4. **Make your change** and test it (see the checklist below).
5. **Commit** and **push**, then open a **Pull Request**:
   ```bash
   git add .
   git commit -m "Add an Ansible playbook write-from-spec task"
   git push -u origin add-ansible-task
   ```

## Adding an exercise

Keep the same simple style:

- For a "fix the YAML" task: add a `broken-*.yaml` file that genuinely fails `python check.py`,
  describe the bug in the part `README.md`, and put the corrected file in `solutions/`.
- For a "write from spec" task: add an `exercise-*.md` brief, and a valid solution YAML in `solutions/`.
- Use plain, simple English.

## Checklist before you open a PR

- [ ] Broken files actually fail `python check.py` (and the fixed version passes).
- [ ] Solution files pass `python check.py` cleanly.
- [ ] Instructions use plain, simple English.
- [ ] If you added a new part, you linked it from the main `README.md`.

## Code of conduct

Be kind and helpful. Assume good intent and keep feedback friendly.

---

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
