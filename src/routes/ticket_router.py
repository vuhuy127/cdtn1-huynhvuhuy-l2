"""HTTP endpoints and request validation for warranty tickets."""
from typing import Literal

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.services import ticket_service

router = APIRouter(prefix="/api/tickets", tags=["Tickets"])


class TicketCreateRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    customer_phone: str = Field(pattern=r"^\d{10}$", description="Exactly 10 digits")
    imei: str = Field(pattern=r"^\d{15}$", description="Exactly 15 digits")
    issue_category: Literal["MAN_HINH", "PIN", "SAC", "PHAN_MEM"]
    description: str = Field(min_length=5, max_length=1000)
    priority: Literal["LOW", "MEDIUM", "HIGH", "URGENT"] = "MEDIUM"

    @field_validator("description")
    @classmethod
    def description_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Description must not be blank")
        return value


class TicketStatusRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    status: Literal["MỚI", "ĐANG XỬ LÝ", "HOÀN TẤT", "ĐÃ HỦY"]


@router.post("/", status_code=status.HTTP_201_CREATED, summary="Create a warranty ticket")
def create_ticket_endpoint(payload: TicketCreateRequest):
    ticket = ticket_service.create_ticket(payload.model_dump())
    return {"message": "Ticket created successfully", "data": ticket}


@router.get("/", summary="List warranty tickets")
def list_tickets_endpoint(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return ticket_service.list_tickets(limit=limit, offset=offset)


@router.get("/{ticket_id}", summary="Get a warranty ticket by ID")
def get_ticket_endpoint(ticket_id: str):
    ticket = ticket_service.get_ticket(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"data": ticket}


@router.patch("/{ticket_id}/status", summary="Update a ticket status")
def update_ticket_status_endpoint(ticket_id: str, payload: TicketStatusRequest):
    ticket = ticket_service.update_ticket_status(ticket_id, payload.status)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket status updated", "data": ticket}