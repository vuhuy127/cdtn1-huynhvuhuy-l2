"""Application service layer for warranty tickets."""
from src.models.ticket_model import STATUSES
from src.repositories import ticket_repo


def create_ticket(data: dict) -> dict:
    return ticket_repo.create_ticket(data)


def list_tickets(limit: int = 20, offset: int = 0) -> dict:
    items, total = ticket_repo.list_tickets(limit=limit, offset=offset)
    return {"items": items, "total": total, "limit": limit, "offset": offset}


def get_ticket(ticket_id: str) -> dict | None:
    return ticket_repo.get_ticket(ticket_id)


def update_ticket_status(ticket_id: str, status: str) -> dict | None:
    if status not in STATUSES:
        raise ValueError("Unsupported ticket status")
    return ticket_repo.update_ticket_status(ticket_id, status)