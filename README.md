# AI Website Generator

An experimental full-stack scaffold for an AI-assisted website-generation service.

The repository contains a FastAPI backend, a Next.js frontend directory and a Docker Compose configuration for supporting services. The project is under development and is not presented as a production-ready application.

## Architecture

| Component | Technology |
| --- | --- |
| Backend API | Python, FastAPI, Uvicorn |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Cache / queue support | Redis |
| Authentication | JWT-related dependencies |
| AI runtime | Ollama |
| Monitoring | Prometheus client, Sentry SDK |
| Frontend | Next.js scaffold |
| Reverse proxy | Nginx |
| Deployment | Docker Compose |

The Compose configuration also declares Grafana and supporting containers.

## Backend dependencies

Install the backend requirements:

```bash
cd backend
python -m venv .venv

# Windows
.venv\\Scripts\\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Running the stack

The root Compose file describes the development environment:

```bash
docker compose up --build
```

The configuration expects a root `.env` file. Supply environment variables for the database, JWT signing, Redis and other configured services before starting the containers. Never commit real credentials.

## Project status

The repository is an implementation scaffold. The frontend package manifest is currently empty and the application components may require additional implementation before the full Compose stack can build successfully.

## Security

Use non-default credentials, restrict exposed service ports, and review the Docker and Nginx configuration before deploying to a public host.
