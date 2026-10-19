from datetime import datetime, timedelta

class Ticket:
    def __init__(self, ticket_id: str, customer_phone: str, imei: str, issue_category: str, description: str, priority: str = "MEDIUM"):
        self.ticket_id = ticket_id
        self.customer_phone = customer_phone
        self.imei = imei
        self.issue_category = issue_category  # MAN_HINH, PIN, SAC, PHAN_MEM
        self.description = description
        self.priority = priority              # LOW, MEDIUM, HIGH, URGENT
        self.status = "MỚI"                   # Trạng thái ban đầu
        self.created_at = datetime.now()
        self.due_date = self.calculate_sla()

    def calculate_sla(self):
        hours_map = {"LOW": 72, "MEDIUM": 48, "HIGH": 24, "URGENT": 12}
        hours = hours_map.get(self.priority, 48)
        return self.created_at + timedelta(hours=hours)

    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "customer_phone": self.customer_phone,
            "imei": self.imei,
            "issue_category": self.issue_category,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "due_date": self.due_date.isoformat()
        }
