# Exercise 3.1 — Kubernetes Deployment

**You write:** a Kubernetes Deployment manifest.

---

## 📋 The spec
Create a file (e.g. `my-deployment.yaml`) describing a Deployment with:

- `apiVersion: apps/v1` and `kind: Deployment`
- **metadata**: name `web-app`, label `app: web-app`
- **spec**:
  - `replicas: 3`
  - a `selector` that matches the label `app: web-app`
  - a pod **template** whose metadata has the label `app: web-app`
  - one container named `web`, image `nginx:1.27`, exposing container port `80`
  - resource **requests** of `cpu: "250m"`, `memory: "128Mi"` and **limits** of `cpu: "500m"`, `memory: "256Mi"`

## ✅ How to check
```bash
python check.py my-deployment.yaml      # must say [VALID]
```
Then compare with [`solutions/k8s-deployment.yaml`](solutions/k8s-deployment.yaml).

## 💡 Hints
- `selector.matchLabels` must match the labels under `template.metadata.labels` — this trips up everyone.
- `ports` under a container is a **list** of maps, each with `containerPort`.
- Quote values like `"250m"` and `"128Mi"` so they stay strings.

> Bonus once it parses: `kubectl apply --dry-run=client -f my-deployment.yaml`
