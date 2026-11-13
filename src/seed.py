"""Idempotent demo-data initializer used by local and container runs."""
from src.config.database import init_db, get_connection
from src.models.ticket_model import calculate_due_date, utc_now

DEMO_TICKETS = [
    {
        "ticket_id": "TK-DEMO-001",
        "customer_phone": "0912345678",
        "imei": "123456789012345",
        "issue_category": "MAN_HINH",
        "description": "Demo ticket: screen has vertical lines",
        "priority": "HIGH",
        "status": "MỚI",
    },
    {
        "ticket_id": "TK-DEMO-002",
        "customer_phone": "0987654321",
        "imei": "543210987654321",
        "issue_category": "PIN",
        "description": "Demo ticket: battery drains quickly",
        "priority": "MEDIUM",
        "status": "ĐANG XỬ LÝ",
    },
]


def seed_demo_data() -> None:
    init_db()
    now = utc_now()
    with get_connection() as connection:
        for item in DEMO_TICKETS:
            connection.execute(
                """
                INSERT OR IGNORE INTO tickets (
                    ticket_id, customer_phone, imei, issue_category, description,
                    priority, status, created_at, due_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item["ticket_id"],
                    item["customer_phone"],
                    item["imei"],
                    item["issue_category"],
                    item["description"],
                    item["priority"],
                    item["status"],
                    now.isoformat(),
                    calculate_due_date(item["priority"], now).isoformat(),
                ),
            )


if __name__ == "__main__":
    seed_demo_data()
    print("Database initialized; demo data seeded idempotently.")
