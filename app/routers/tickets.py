from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.ticket import Ticket
from app.models.usuario import Usuario
from app.schemas.ticket import TicketCreate, TicketResponse
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/tickets", tags=["Tickets"])


# 🔹 Crear ticket
@router.post("/", response_model=TicketResponse)
def crear_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Security(get_current_user, scopes=["tickets:crear"])
):
    nuevo = Ticket(
        descripcion=ticket.descripcion,
        estado="solicitado",
        id_solicitante=current_user.id_usuario
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


# 🔥 Cambiar estado del ticket
@router.patch("/{id_ticket}/estado")
def cambiar_estado(
    id_ticket: int,
    nuevo_estado: str,
    db: Session = Depends(get_db),
    current_user: Usuario = Security(get_current_user, scopes=["tickets:atender"])
):
    ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    # Flujo de estados permitido
    transiciones = {
        "solicitado": ["recibido"],
        "recibido": ["asignado"],
        "asignado": ["en_proceso"],
        "en_proceso": ["en_revision"],
        "en_revision": ["terminado"]
    }

    if nuevo_estado not in transiciones.get(ticket.estado, []):
        raise HTTPException(status_code=400, detail="Transición no permitida")

    # Validación de relación (solo asignado puede avanzar)
    if nuevo_estado in ["en_proceso", "en_revision"]:
        if ticket.id_asignado != current_user.id_usuario:
            raise HTTPException(status_code=403, detail="No eres el técnico asignado")

    ticket.estado = nuevo_estado

    db.commit()

    return {"mensaje": f"Estado actualizado a {nuevo_estado}"}