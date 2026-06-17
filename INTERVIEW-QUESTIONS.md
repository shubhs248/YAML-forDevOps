# 🎤 YAML — Interview Questions

> YAML shows up everywhere in DevOps (Kubernetes, CI/CD, Ansible, Compose), so interviewers test whether you really understand it — not just copy-paste it. Plain-English answers you can say out loud. Do the "fix-the-yaml" exercises first.

**How to use this file:** cover the answers, read a question, answer out loud, then check. Many YAML questions are really "do you know the gotchas?".

---

## 🟢 Warm-up

**1. What is YAML and where is it used in DevOps?**
YAML ("YAML Ain't Markup Language") is a human-readable data format for configuration. It's used by Kubernetes manifests, GitHub Actions / GitLab CI, Ansible playbooks, Docker Compose, and many more. It describes **data**, not logic.

**2. What are the three basic building blocks of YAML?**
- **Scalars** — single values (string, number, boolean): `name: web`
- **Mappings** — key/value pairs (like a dict): `port: 8080`
- **Sequences** — lists: `- item1` / `- item2`
Everything in YAML is some nesting of these three.

**3. How does YAML represent structure / nesting?**
With **indentation** (spaces). Indentation defines what belongs to what — there are no braces. This is why YAML is readable but also why indentation mistakes are the #1 source of errors.

**4. Can you use tabs for indentation in YAML?**
No. YAML **forbids tabs** for indentation — you must use spaces. A stray tab is a classic "why won't this parse" bug. (That's the indentation exercise in this lab.)

**5. How do you write a comment?**
With `#`. Everything after `#` on a line is ignored. YAML has no block-comment syntax — every comment line needs its own `#`.

---

## 🔵 The data types & gotchas (where interviews get you)

**6. What's the "Norway problem" / the boolean gotcha?**
YAML interprets unquoted `yes`, `no`, `true`, `false`, `on`, `off` as **booleans**. So a country code `NO` (Norway) becomes `false`. The fix: **quote** values that should stay strings — `"NO"`.

**7. Why might `version: 1.10` not behave as expected?**
Unquoted `1.10` is parsed as the **number** 1.1 (the trailing zero is dropped). Versions, ZIP codes, and IDs should be quoted: `version: "1.10"`.

**8. How do you force a value to be a string?**
Quote it: `"123"` or `'true'`. Use quotes whenever a value *looks* like a number/boolean/date but should be text. (That's the quotes exercise in this lab.)

**9. Single vs double quotes in YAML?**
- **Single** `'...'` — fully literal, except `''` escapes a single quote.
- **Double** `"..."` — supports escape sequences like `\n`, `\t`.
Use double quotes when you need escapes; single quotes otherwise.

**10. How do you represent null / empty?**
With `null`, `~`, or simply leaving the value blank: `value:`. All three mean "no value".

---

## 🟣 Multi-line, reuse, and multiple docs

**11. Difference between `|` and `>` for multi-line strings?**
- `|` (**literal block**) — keeps newlines exactly as written. Good for scripts, certs.
- `>` (**folded block**) — folds newlines into spaces (one long paragraph). Good for long prose.
Add `-` (`|-`, `>-`) to strip the trailing newline.

**12. What are anchors and aliases?**
A way to avoid repetition. `&name` defines an anchor, `*name` reuses it, and `<<: *name` merges a mapping:
```yaml
defaults: &defaults
  retries: 3
  timeout: 30
prod:
  <<: *defaults
  timeout: 60   # override
```
DRY config without copy-paste.

**13. How do you put multiple documents in one YAML file?**
Separate them with `---`. Kubernetes uses this a lot to put several resources (Deployment, Service, ConfigMap) in one file. `...` optionally marks the end of a document.

**14. Inline (flow) style vs block style?**
You can write the same data two ways: block (multi-line, indented) or flow/inline (`{name: web, port: 80}` and `[a, b, c]`). Block is more common and readable; flow is handy for short values.

---

## 🟠 YAML in real DevOps tools

**15. What are the required top-level fields of a Kubernetes manifest?**
`apiVersion`, `kind`, `metadata` (with at least `name`), and usually `spec`. Interviewers check you know the shape of a manifest, not that you memorise every field.

**16. In a GitHub Actions workflow, what are the key top-level keys?**
`name`, `on` (the trigger), and `jobs`. Each job has `runs-on` and `steps`. (That's exercise 2 in the "write configs" part.) Watch out: `on` is a YAML boolean-ish word, but tools special-case it.

**17. How do you pass environment variables in Docker Compose YAML?**
Under a service's `environment:` key, as either a mapping (`KEY: value`) or a list (`- KEY=value`). Reference a `.env` file with `env_file:`. (See the Compose exercise.)

**18. How do you validate a YAML file?**
Parse it with a tool: `yamllint`, `python -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))"`, or the `check.py` script in this lab. Tool-specific validators (`kubectl --dry-run`, `docker compose config`) catch schema errors too.

---

## 🔴 "Senior" / safety & real-world

**19. Why use `yaml.safe_load()` instead of `yaml.load()` in Python?**
Plain `yaml.load()` can construct arbitrary Python objects, which means a malicious YAML file could run code. `safe_load()` only builds basic types and is the safe default for any untrusted input.

**20. JSON vs YAML — when would you choose each?**
JSON is strict and great for machine-to-machine APIs. YAML is friendlier for humans to write/read (comments, less punctuation), so it's preferred for config files. Fun fact: valid JSON is also valid YAML.

**21. What's a common cause of "works locally, fails in CI" with YAML?**
Indentation/whitespace differences (tabs sneaking in via an editor), unquoted values being mis-typed, or a different parser/version being stricter. Always lint YAML in CI.

**22. How do you handle secrets in YAML config?**
Don't put plaintext secrets in YAML that lives in Git. Reference them from a secret store, environment variables, Kubernetes Secrets, or a sealed/encrypted mechanism (SOPS, Sealed Secrets, Vault).

**23. Your Kubernetes YAML is rejected. How do you debug it?**
`kubectl apply --dry-run=client -f file.yaml` to catch schema errors, `kubectl explain <kind>.spec` to check fields, and a YAML linter for syntax. Read the error — it usually names the line and field.

---

## 🧠 Spot-the-bug drills

These mirror the broken files in this lab. Can you find the issue?

1. A list item indented under the wrong key. → indentation bug.
2. `enabled: yes` meant as the string "yes". → quote it.
3. `tab` used to indent one line. → tabs are illegal.
4. `time: 22:30` unquoted. → colon-in-value needs quotes.
5. A duplicated key in the same mapping. → last one silently wins.

---

## ⭐ Found this useful?
If this helped your prep, please **star** ⭐, **fork** 🍴, and **share** 🔗 the repo on LinkedIn. Got a YAML gotcha that bit you in an interview? Add it via [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
