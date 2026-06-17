# 📋 YAML Quick-Revision Cheatsheet

A one-page reminder of YAML, plus the gotchas that catch everyone. Use it with the exercises.

## The basics
```yaml
# A comment starts with a hash

# key: value pairs (a "mapping")
name: web-server
replicas: 3
enabled: true

# Indentation uses SPACES (never tabs). 2 spaces is the norm.
resources:
  cpu: 500m
  memory: 256Mi
```

## Lists (sequences)
```yaml
# a list of strings
ports:
  - 80
  - 443

# inline (flow) style
ports: [80, 443]

# a list of maps
containers:
  - name: app
    image: nginx:1.27
  - name: sidecar
    image: busybox
```

## Maps inside lists, lists inside maps
```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
```

## Data types
```yaml
a_string: hello
a_number: 42
a_float: 3.14
a_bool: true            # also false
nothing: null           # also ~ or just empty
a_date: 2026-06-17
inline_list: [a, b, c]
inline_map: {x: 1, y: 2}
```

## Multi-line text
```yaml
# block scalar with | keeps newlines
description: |
  line one
  line two

# block scalar with > folds newlines into spaces
summary: >
  this becomes
  one long line
```

## Quotes
```yaml
plain: no quotes needed most of the time
single: 'use single quotes for literal text - no escapes'
double: "use double quotes when you need \n escapes or special chars"
# Quote a value that LOOKS like something else:
version: "1.0"          # keep it a string, not the float 1.0
port_range: "8080:80"   # the colon would confuse YAML if unquoted
```

## Anchors & aliases (reuse a block)
```yaml
defaults: &defaults     # &defaults defines an anchor
  retries: 3
  timeout: 30

job_a:
  <<: *defaults         # merge the anchored map in
  name: a
job_b:
  <<: *defaults
  name: b
```

## Multiple documents in one file
```yaml
---
kind: ConfigMap
name: a
---
kind: Service
name: b
```

## ⚠️ The gotchas (these cause real outages)
```yaml
# 1. TABS are not allowed for indentation. Use spaces.
# 2. These unquoted values become BOOLEANS, not strings:
country: NO            # -> false (Norway problem!)  use "NO"
answer: yes            # -> true                       use "yes"
# 3. Numbers lose meaning when you wanted text:
version: 1.10          # -> 1.1 (float!)              use "1.10"
zip: 01234             # leading zero / octal trap    use "01234"
# 4. A value with ': ' or starting with @ * % & ! needs quotes.
# 5. Indentation must be consistent within the same block.
```

## Validate it
```bash
python check.py path/to/file.yaml      # this lab's helper
yamllint path/to/file.yaml             # popular linter (pip install yamllint)
```

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to improve it? See [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
