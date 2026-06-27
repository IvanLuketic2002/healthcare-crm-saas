# Healthcare CRM SaaS

Modularni SaaS projekat (CRM/healthcare), izgradjen postepeno kroz faze:

1. Lokalni MVP (FastAPI + Postgres, Docker Compose)
2. Lokalni Kubernetes (k3d)
3. AWS Free Tier (Terraform + k3s na EC2)
4. CI/CD (GitHub Actions)

## Struktura

- `backend/` - FastAPI aplikacija (Patient, Doctor, Appointment modeli)
- `k8s/` - Kubernetes manifesti (Deployment, Service, Ingress, Secret)
- `terraform/` - Infrastructure as Code za AWS (VPC, EC2, Security Group)
- `docker-compose.yml` - lokalno pokretanje za development

## Lokalno pokretanje

```bash
docker compose up --build
```

API dostupan na http://localhost:8000/docs
