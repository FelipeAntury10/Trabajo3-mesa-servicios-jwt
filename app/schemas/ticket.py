from pydantic import BaseModel

class TicketCreate(BaseModel):
    descripcion: str

class TicketResponse(BaseModel):
    id_ticket: int
    descripcion: str
    estado: str
    id_solicitante: int
    id_responsable: int | None
    id_asignado: int | None

    class Config:
        from_attributes = True