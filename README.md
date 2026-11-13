# Mekong Mobile Smart CRM — Warranty Intake (L2)

**Track:** SE · **Workflow:** L2 · **Prototype:** FastAPI + SQLite

This repository contains the L2 prototype for receiving and classifying warranty requests. It validates customer phone and device IMEI, assigns an SLA from priority, persists tickets in SQLite, and exposes APIs for listing, retrieving, and updating ticket status.

## Implemented scope

- Create warranty tickets.
- List tickets with pagination.
- Retrieve one ticket by ID.
- Update a ticket status.
- Validate phone number (10 digits), IMEI (15 digits), category, priority, and description.
- Store data in SQLite; initialize schema and two synthetic demo tickets idempotently.
- Health endpoint checks application-to-database connectivity.

Not implemented: authentication, per-customer authorization, encryption at rest, production database operations, and public production deployment. Do not use real customer data.

## Technology

- Python 3.12 / 3.13
- FastAPI, Pydantic, Uvicorn
- SQLite (Python standard library)
- Pytest + HTTPX
- Docker Compose

## Run with Docker

Requirements: Docker Engine and Docker Compose plugin.

~~~bash
git clone https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2.git && cd cdtn1-huynhvuhuy-l2
docker compose up -d --build
~~~

Open http://localhost:8000/docs. The app seeds two synthetic demo tickets at startup. See docs/deployment-guide.md.

## Run locally

~~~bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn src.main:app --reload
~~~

By default, SQLite is stored at data/tickets.db. Override with DATABASE_PATH.

## Test

~~~bash
python -m pytest -q
~~~

## API endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | / | API welcome |
| GET | /health | App and SQLite health |
| POST | /api/tickets/ | Create a ticket |
| GET | /api/tickets/ | List tickets |
| GET | /api/tickets/{ticket_id} | Get one ticket |
| PATCH | /api/tickets/{ticket_id}/status | Update status |

Interactive API documentation: /docs.

## Repository documents

- docs/test-plan.md — Test Plan.
- docs/test-report.md — 12 test cases and recorded local run.
- docs/bug-log.md — Bug Log.
- docs/deployment-guide.md — English Deployment Guide.
- docs/security-checklist.md — seven-item security checklist.
- docs/api-documentation.md — English API documentation.
- docs/ai-disclosure.md — AI-use declaration.
- docs/erd.drawio — implemented SQLite schema.
- docs/architecture.drawio — current prototype architecture.
- docs/usecase.drawio — implemented use cases.

## Important

Do not commit .env, local database files, customer data, or credentials. .env.example contains only a non-secret port setting. The Docker volume persists data between container restarts; docker compose down -v deletes that volume and its data.