"""12 deterministic API and persistence tests for BT3."""
import pytest
from fastapi.testclient import TestClient

from src.config.database import init_db
from src.main import app
from src.repositories.ticket_repo import count_tickets
from src.seed import seed_demo_data


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("DATABASE_PATH", str(tmp_path / "test-tickets.db"))
    with TestClient(app) as test_client:
        yield test_client


def valid_payload(**overrides):
    payload = {
        "customer_phone": "0901234567",
        "imei": "123456789012345",
        "issue_category": "MAN_HINH",
        "description": "Screen shows vertical lines after impact",
        "priority": "HIGH",
    }
    payload.update(overrides)
    return payload


# TC-01 — Happy path: root endpoint is available.
def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "running" in response.json()["message"]


# TC-02 — Happy path: health check verifies SQLite connectivity.
def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "database": "connected"}


# TC-03 — Happy path: a valid ticket is created and receives the HIGH SLA.
def test_create_ticket_success(client):
    response = client.post("/api/tickets/", json=valid_payload())
    assert response.status_code == 201
    data = response.json()["data"]
    assert data["ticket_id"].startswith("TK-")
    assert data["priority"] == "HIGH"
    assert data["status"] == "MỚI"
    assert data["due_date"] > data["created_at"]


# TC-04 — Happy path: list endpoint returns pagination metadata.
def test_list_tickets_with_pagination(client):
    response = client.get("/api/tickets/?limit=1&offset=0")
    assert response.status_code == 200
    body = response.json()
    assert body["limit"] == 1
    assert body["offset"] == 0
    assert body["total"] >= 2
    assert len(body["items"]) == 1


# TC-05 — Happy path: an existing seeded ticket can be retrieved.
def test_get_existing_ticket(client):
    response = client.get("/api/tickets/TK-DEMO-001")
    assert response.status_code == 200
    assert response.json()["data"]["ticket_id"] == "TK-DEMO-001"


# TC-06 — Happy path: status can be updated.
def test_update_ticket_status(client):
    response = client.patch(
        "/api/tickets/TK-DEMO-001/status",
        json={"status": "HOÀN TẤT"},
    )
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "HOÀN TẤT"


# TC-07 — Boundary: a 9-digit phone number is rejected.
def test_phone_below_boundary_is_rejected(client):
    response = client.post(
        "/api/tickets/",
        json=valid_payload(customer_phone="090123456"),
    )
    assert response.status_code == 422


# TC-08 — Boundary: an 11-digit phone number is rejected.
def test_phone_above_boundary_is_rejected(client):
    response = client.post(
        "/api/tickets/",
        json=valid_payload(customer_phone="09012345678"),
    )
    assert response.status_code == 422


# TC-09 — Invalid data: a 14-digit IMEI is rejected.
def test_imei_below_boundary_is_rejected(client):
    response = client.post(
        "/api/tickets/",
        json=valid_payload(imei="12345678901234"),
    )
    assert response.status_code == 422


# TC-10 — Invalid data: unsupported priority is rejected without echoing input.
def test_invalid_priority_is_rejected_without_echoing_payload(client):
    response = client.post(
        "/api/tickets/",
        json=valid_payload(priority="ROOT"),
    )
    assert response.status_code == 422
    assert "ROOT" not in response.text


# TC-11 — Security: SQL-like input is stored as data, not executed as SQL.
def test_sql_injection_string_is_treated_as_plain_text(client):
    attack_text = "'; DROP TABLE tickets; --"
    response = client.post(
        "/api/tickets/",
        json=valid_payload(description=attack_text),
    )
    assert response.status_code == 201
    assert client.get("/api/tickets/").status_code == 200
    ticket_id = response.json()["data"]["ticket_id"]
    fetched = client.get(f"/api/tickets/{ticket_id}")
    assert fetched.status_code == 200
    assert fetched.json()["data"]["description"] == attack_text


# TC-12 — Reproducibility: running seed twice does not duplicate demo records.
def test_seed_is_idempotent(client):
    before = count_tickets()
    seed_demo_data()
    seed_demo_data()
    after = count_tickets()
    assert before == after == 2