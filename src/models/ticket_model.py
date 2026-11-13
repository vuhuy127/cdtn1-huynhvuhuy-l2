"""Domain constants and SLA calculation for warranty tickets."""
from datetime import datetime, timedelta, timezone

SLA_HOURS = {
    "LOW": 72,
    "MEDIUM": 48,
    "HIGH": 24,
    "URGENT": 12,
}

ISSUE_CATEGORIES = ("MAN_HINH", "PIN", "SAC", "PHAN_MEM")
PRIORITIES = tuple(SLA_HOURS)
STATUSES = ("MỚI", "ĐANG XỬ LÝ", "HOÀN TẤT", "ĐÃ HỦY")


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def calculate_due_date(priority: str, created_at: datetime | None = None) -> datetime:
    if priority not in SLA_HOURS:
        raise ValueError(f"Unsupported priority: {priority}")
    created = created_at or utc_now()
    return created + timedelta(hours=SLA_HOURS[priority])