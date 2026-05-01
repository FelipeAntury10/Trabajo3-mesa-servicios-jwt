

from fastapi import FastAPI

from app.core.database import engine, Base
from app.models.usuario import Usuario
from app.routers import usuarios, auth
from app.models.ticket import Ticket
from app.routers import tickets

app = FastAPI()

# Crear tablas en la base de datos
print("CREANDO TABLAS...")
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(usuarios.router)
app.include_router(auth.router)
app.include_router(tickets.router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}