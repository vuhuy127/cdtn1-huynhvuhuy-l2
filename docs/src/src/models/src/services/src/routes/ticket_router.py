from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.ticket_service import TicketService

router = APIRouter(prefix="/api/tickets", tags=["Tickets"])

class TicketCreateRequest(BaseModel):
    customer_phone: str
    imei: str
    issue_category: str
    description: str
    priority: str = "MEDIUM"

@router.post("/", summary="Tạo phiếu bảo hành mới")
def create_ticket_endpoint(payload: TicketCreateRequest):
    ticket = TicketService.create_ticket(payload.dict())
    return {"message": "Tạo phiếu bảo hành thành công", "data": ticket.to_dict()}

@router.get("/", summary="Lấy danh sách phiếu bảo hành")
def list_tickets_endpoint():
    return {"tickets": TicketService.get_all_tickets()}
