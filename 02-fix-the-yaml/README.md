# Part 2 — Fix the YAML

## 🎯 Goal
Train your eye to spot the YAML mistakes that break real pipelines and deployments — and learn how the error messages point you to them.

## 🧠 What you practise here
- Reading a parser error and turning it into a fix
- The three most common YAML bugs: **indentation**, **missing quotes**, and **broken structure**

---

## 📝 The task

Each file in this folder is **broken on purpose**. For each one:

1. Run the checker to see the error:
   ```bash
   python check.py 02-fix-the-yaml/broken-1-indentation.yaml
   ```
2. Read the error (it tells you roughly which line and column).
3. Edit the file until `check.py` says ✅ VALID.
4. Compare your fix with the matching file in [`solutions/`](solutions).

| File | The bug to find |
|------|-----------------|
| `broken-1-indentation.yaml` | one list item is indented differently from the others |
| `broken-2-quotes.yaml`      | a value contains `: ` (a colon + space), which must be quoted |
| `broken-3-structure.yaml`   | a block tries to be a **list and a map at the same time** |

> 💡 The intended result for `broken-3` is: `stages` is a list of `build`, `test`, `deploy`, and there is a separate key `target: production`.

## 💡 Tips
- YAML indentation is **spaces only** and must be consistent inside the same block.
- If a value has a colon, a `#`, or starts with a special character (`@ * & ! % ?`), wrap it in quotes.
- A block under a key is **either** a list (`- item`) **or** a map (`key: value`) — never both.

➡️ Next: [Part 3 — Write DevOps Configs](../03-write-devops-configs/README.md).

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add a broken file or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
