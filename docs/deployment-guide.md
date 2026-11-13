# Deployment Guide — Mekong Mobile Smart CRM L2

## 1. Requirements

- Docker Engine 24 or later.
- Docker Compose plugin v2.
- Git.
- A free host TCP port (default: 8000).
- Internet access for the first image build to download the Python base image and pinned packages.

The application uses SQLite inside the container. No external database service is required.

## 2. Setup steps

From a new terminal and an empty working directory, run the following two commands:

~~~bash
git clone https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2.git && cd cdtn1-huynhvuhuy-l2
docker compose up -d --build
~~~

The Docker image installs pinned Python requirements, copies the application, and runs Uvicorn as a non-root user. On first startup, the application creates the SQLite schema and inserts two demo tickets. The database is stored in the named Docker volume ticket_data. The default host port is 8000; no .env file is required.

To inspect the service:

~~~bash
docker compose ps
docker compose logs app
~~~

## 3. Environment variables

| Variable | Default | Required | Description |
|---|---|---|---|
| APP_PORT | 8000 | No | Host port mapped to container port 8000 |
| DATABASE_PATH | /app/data/tickets.db in container | No | SQLite file path; set internally by Compose |

Copy .env.example to .env only when you need to change APP_PORT. Do not add real secrets to the repository. No database password or JWT secret is required by this prototype.

## 4. Sample data

On application startup, src/seed.py inserts two synthetic sample tickets:

- TK-DEMO-001 — screen issue, HIGH priority.
- TK-DEMO-002 — battery issue, MEDIUM priority.

The seed operation uses INSERT OR IGNORE, so starting the application again does not create duplicate demo rows. Do not use real customer phone numbers or IMEIs in demo data.

## 5. Verify it works

Run:

~~~bash
docker compose ps
curl -fsS http://localhost:8000/health
curl -fsS http://localhost:8000/api/tickets/
~~~

Expected health response:

~~~json
{"status":"healthy","database":"connected"}
~~~

Open http://localhost:8000/docs to inspect and try the API.

To verify persistence, create a ticket, restart the service with docker compose restart app, and request the ticket again. The named volume preserves the SQLite file.

To remove the container and all persisted demo data, run:

~~~bash
docker compose down -v
~~~

## Clean-machine acceptance test

For the BT3 white-box test, clone the submitted tag v1.0 into a new empty folder, follow only the two setup commands above, verify the healthy state, run the API smoke checks, and capture screenshots. Do not claim the clean-machine test passed until this procedure has actually been executed on a separate Docker-capable machine.