# Part 1 — YAML Basics (Refresher)

*The structure of a YAML document — mappings, sequences, scalars:*

<picture><source media="(prefers-color-scheme: dark)" srcset="../docs/01-yaml-structure-dark.png"><img alt="YAML structure" src="../docs/01-yaml-structure.png"></picture>

*Scalar data types (and the gotchas to quote around):*

<picture><source media="(prefers-color-scheme: dark)" srcset="../docs/02-data-types-dark.png"><img alt="YAML data types" src="../docs/02-data-types.png"></picture>

## 🎯 Goal
Refresh how YAML represents data so the broken-file and write-from-spec parts feel easy.

## 🧠 What you practise here
| Idea | What it is |
|------|------------|
| scalars | single values: text, numbers, booleans, null |
| mappings | `key: value` pairs |
| sequences | lists of items |
| nesting | maps and lists inside each other (by indentation) |
| types | how YAML decides if something is text, a number, or a boolean |
| multi-line | `\|` (keep newlines) and `>` (fold into one line) |
| anchors | `&name` / `*name` to reuse a block |
| documents | `---` to put several documents in one file |

You can check any snippet by saving it to a file and running `python check.py file.yaml`.

---

## 📝 Tasks
Write the YAML for each, then validate it. Answers are at the bottom.

1. **A simple map.** Describe a server with: `name` = web-01, `role` = web, `enabled` = true, `replicas` = 3.
2. **A list.** Make a key `ports` holding the list 80, 443, 8080.
3. **A list of maps.** Make a key `containers` with two items, each having `name` and `image`.
4. **Nesting.** Under a key `resources`, nest `limits` with `cpu` = "500m" and `memory` = "256Mi".
5. **Keep it a string.** Write a key `version` whose value is the text `1.10` (NOT the number 1.1).
6. **Booleans trap.** Write a key `country` whose value is the **text** `NO` (not the boolean false).
7. **Multi-line block.** Write a key `notes` that keeps these two lines exactly:
   `deploy at 9am` and `rollback plan ready`.
8. **Anchor & alias.** Define an anchor `defaults` with `retries: 3` and `timeout: 30`, then create `job_a` and `job_b` that reuse it (and each add their own `name`).
9. **Two documents.** Put two small documents in one file separated by `---`.
10. **Spot the type.** What Python types do these become: `value: yes`, `value: 1.0`, `value: "1.0"`, `value: 2026-06-17`? (Use `check.py` to confirm.)

---

## ✅ Answers

```yaml
# 1. A simple map
name: web-01
role: web
enabled: true
replicas: 3
```

```yaml
# 2. A list
ports:
  - 80
  - 443
  - 8080
```

```yaml
# 3. A list of maps
containers:
  - name: app
    image: nginx:1.27
  - name: sidecar
    image: busybox:1.36
```

```yaml
# 4. Nesting
resources:
  limits:
    cpu: "500m"
    memory: "256Mi"
```

```yaml
# 5. Keep it a string (quotes stop it becoming the float 1.1)
version: "1.10"
```

```yaml
# 6. Booleans trap (unquoted NO becomes false, so quote it)
country: "NO"
```

```yaml
# 7. Multi-line block ('|' keeps the line breaks)
notes: |
  deploy at 9am
  rollback plan ready
```

```yaml
# 8. Anchor & alias
defaults: &defaults
  retries: 3
  timeout: 30

job_a:
  <<: *defaults
  name: a
job_b:
  <<: *defaults
  name: b
```

```yaml
# 9. Two documents in one file
---
kind: ConfigMap
name: settings
---
kind: Service
name: web
```

```text
# 10. Types
value: yes          -> bool (True)        # surprise! quote it if you meant text
value: 1.0          -> float (1.0)
value: "1.0"        -> str ("1.0")
value: 2026-06-17   -> datetime.date
```

➡️ When you are comfortable, move on to [Part 2 — Fix the YAML](../02-fix-the-yaml/README.md).

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add a task or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
