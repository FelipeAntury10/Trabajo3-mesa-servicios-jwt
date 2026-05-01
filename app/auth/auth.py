from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Mapeo rol → scopes
ROLE_SCOPES = {
    "solicitante": ["tickets:crear", "tickets:ver_propios"],
    "auxiliar": ["tickets:ver_propios", "tickets:atender"],
    "tecnico_especializado": ["tickets:ver_propios", "tickets:atender"],
    "responsable_tecnico": [
        "tickets:ver_propios",
        "tickets:recibir",
        "tickets:asignar",
        "tickets:finalizar"
    ],
    "admin": [
        "tickets:crear",
        "tickets:ver_propios",
        "tickets:recibir",
        "tickets:asignar",
        "tickets:atender",
        "tickets:finalizar",
        "tickets:ver_todos",
        "usuarios:gestionar"
    ]
}

def create_access_token(user):
    scopes = ROLE_SCOPES.get(user.rol, [])

    payload = {
        "sub": user.correo,
        "id_usuario": user.id_usuario,
        "rol": user.rol,
        "scopes": scopes,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)