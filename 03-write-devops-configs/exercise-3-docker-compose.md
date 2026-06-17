# Exercise 3.3 — Docker Compose File

**You write:** a Docker Compose file for a small web + database stack.

---

## 📋 The spec
Create a file (e.g. `compose.yaml`) describing:

- two **services**: `web` and `db`
- **web**:
  - image `nginx:1.27`
  - maps host port `8080` to container port `80` (remember to quote `"8080:80"`)
  - `depends_on` the `db` service
  - an environment variable `APP_ENV: production`
- **db**:
  - image `postgres:16`
  - environment variable `POSTGRES_PASSWORD: secret`
  - a named **volume** `db-data` mounted at `/var/lib/postgresql/data`
- a top-level `volumes` section that declares `db-data`

## ✅ How to check
```bash
python check.py compose.yaml      # must say [VALID]
```
Then compare with [`solutions/docker-compose.yaml`](solutions/docker-compose.yaml).

## 💡 Hints
- `ports` and `volumes` (inside a service) are **lists** of strings.
- The port mapping `8080:80` must be quoted, or YAML may read the colon oddly.
- The top-level `volumes:` just needs the volume name with an empty value, e.g. `db-data:`.

> Bonus once it parses: `docker compose -f compose.yaml config` checks it against the Compose schema.
