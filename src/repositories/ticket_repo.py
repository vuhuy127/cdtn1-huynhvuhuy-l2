"""Persistence operations. All SQL values are passed as parameters."""
from __future__ import annotations

from uuid import uuid4

from src.config.database import get_connection
from src.models.ticket_model import calculate_due_date, utc_now


def _row_to_dict(row):
    return dict(row) if row is not None else None


def create_ticket(data: dict) -> dict:
    created_at = utc_now()
    ticket_id = f"TK-{uuid4().hex[:10].upper()}"
    due_date = calculate_due_date(data["priority"], created_at)
    record = {
        "ticket_id": ticket_id,
        "customer_phone": data["customer_phone"],
        "imei": data["imei"],
        "issue_category": data["issue_category"],
        "description": data["description"],
        "priority": data["priority"],
        "status": "MỚI",
        "created_at": created_at.isoformat(),
        "due_date": due_date.isoformat(),
    }
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO tickets (
                ticket_id, customer_phone, imei, issue_category, description,
                priority, status, created_at, due_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            tuple(record.values()),
        )
    return record


def get_ticket(ticket_id: str) -> dict | None:
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,)
        ).fetchone()
    return _row_to_dict(row)


def list_tickets(limit: int = 20, offset: int = 0) -> tuple[list[dict], int]:
    with get_connection() as connection:
        total = connection.execute("SELECT COUNT(*) FROM tickets").fetchone()[0]
        rows = connection.execute(
            """
            SELECT * FROM tickets
            ORDER BY created_at DESC, ticket_id ASC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()
    return [dict(row) for row in rows], total


def update_ticket_status(ticket_id: str, status: str) -> dict | None:
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE tickets SET status = ? WHERE ticket_id = ?",
            (status, ticket_id),
        )
        if cursor.rowcount == 0:
            return None
        row = connection.execute(
            "SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,)
        ).fetchone()
    return _row_to_dict(row)


def count_tickets() -> int:
    with get_connection() as connection:
        return connection.execute("SELECT COUNT(*) FROM tickets").fetchone()[0]