from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.tickets import Ticket, TicketCreate, TicketUpdate
from app.services.tickets import TicketService
from app.clients.db import DatabaseClient
from app.dependencies import verify_token
from typing import List

def create_ticket_router(database_client: DatabaseClient) -> APIRouter:
    ticket_router = APIRouter()
    ticket_service = TicketService(database_client)

    @ticket_router.post("/", response_model=Ticket, status_code=201)
    async def create_ticket(ticket: TicketCreate, token_data: TokenData = Depends(verify_token)):
        new_ticket = await ticket_service.create_ticket(ticket, user_id=token_data.user_id)
        return new_ticket

    @ticket_router.get("/{ticket_id}", response_model=Ticket)
    async def read_ticket(ticket_id: int, token_data: TokenData = Depends(verify_token)):
        ticket = await ticket_service.get_ticket_by_id(ticket_id)
        return ticket

    @ticket_router.patch("/{ticket_id}", response_model=Ticket)
    async def update_ticket(ticket_id: int, ticket_update: TicketUpdate, token_data: TokenData = Depends(verify_token)):
        updated_ticket = await ticket_service.update_ticket(ticket_id, ticket_update)
        return updated_ticket

    @ticket_router.delete("/{ticket_id}", status_code=204)
    async def delete_ticket(ticket_id: int, token_data: TokenData = Depends(verify_token)):
        await ticket_service.delete_ticket(ticket_id)
        return {"detail": "Ticket deleted successfully"}

    return ticket_router
