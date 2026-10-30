from src.models.ticket_model import Ticket

fake_db = {}

class TicketService:
    @staticmethod
    def create_ticket(data: dict) -> Ticket:
        ticket_id = f"TK-{len(fake_db) + 1001}"
        new_ticket = Ticket(
            ticket_id=ticket_id,
            customer_phone=data.get("customer_phone"),
            imei=data.get("imei"),
            issue_category=data.get("issue_category"),
            description=data.get("description"),
            priority=data.get("priority", "MEDIUM")
        )
        fake_db[ticket_id] = new_ticket
        return new_ticket

    @staticmethod
    def get_ticket(ticket_id: str):
        return fake_db.get(ticket_id)

    @staticmethod
    def get_all_tickets():
        return [t.to_dict() for t in fake_db.values()]
