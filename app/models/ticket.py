from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id_ticket = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    estado = Column(String, default="solicitado")

    id_solicitante = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_responsable = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)
    id_asignado = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)