# API Mesa de Servicios con JWT y Scopes

## 1.Información General

* **Nombre del proyecto:** API Mesa de Servicios para Laboratorios Universitarios
* **Integrantes:**

  * Juan Felipe Antury Bermeo
  * Juan david restrepo quintero 
  * [Nombre Compañero 2]
  *Asignatura: Aplicaciones y servicios web
  *Fecha: 01/05/2026

---

## 2.Descripción del Sistema

Este proyecto consiste en el desarrollo de una API REST segura para la gestión de tickets de servicios en laboratorios universitarios.

La API permite:

* Crear solicitudes de servicio (tickets)
* Gestionar el flujo de atención
* Asignar responsables técnicos
* Controlar el acceso mediante autenticación JWT y autorización por scopes

### Entidades implementadas:

* Usuarios
* Tickets
* (Pendiente por equipo: Laboratorios y Servicios)

### Arquitectura

Se utilizó una arquitectura modular basada en:

* **Models:** SQLAlchemy (persistencia)
* **Schemas:** Pydantic (validación)
* **Routers:** Endpoints
* **Auth:** JWT + seguridad
* **Core:** Configuración y base de datos

---

## 3.Configuración del Entorno

### Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Archivo `.env`

```env
DATABASE_URL=postgresql://postgres:1234@localhost:5432/jwt_grupo_1 SECRET_KEY=clave_secreta
ALGORITHM=HS256 
ACCESS_TOKEN_EXPIRE_MINUTES=30
```


---

## 4. Configuración de Base de Datos

CREATE DATABASE jwt_grupo_1;
CREATE SCHEMA jwt_grupo_1;

* Motor: PostgreSQL
* Schema: `jwt_grupo_1`

La conexión se realiza mediante SQLAlchemy usando variables de entorno.

---

## 5. Endpoints Implementados

### Autenticación

| Método | Endpoint    | Descripción               |
| ------ | ----------- | ------------------------- |
| POST   | /auth/token | Login y generación de JWT |

---

### Usuarios

| Método | Endpoint   | Descripción   | Scope              |
| ------ | ---------- | ------------- | ------------------ |
| POST   | /usuarios/ | Crear usuario | usuarios:gestionar |

---

### Tickets

| Método | Endpoint             | Descripción    | Scope               |
| ------ | -------------------- | -------------- | ------------------- |
| POST   | /tickets/            | Crear ticket   | tickets:crear       |
| GET    | /tickets/            | Listar tickets | tickets:ver_propios |
| GET    | /tickets/{id}        | Ver detalle    | tickets:ver_propios |
| PATCH  | /tickets/{id}/estado | Cambiar estado | tickets:atender     |

---

## 6. Evidencias de Funcionamiento

### Autenticación

* ✔ Login exitoso con JWT
* ✔ Uso de botón Authorize en Swagger
* ✔ Acceso con token válido
* ✔ Error 401 sin token

---

### Autorización (Scopes)

* ✔ Acceso permitido con scope correcto
* ✔ Error 403 sin permisos
* ✔ Protección por roles

---

### Flujo de Tickets

* ✔ Ticket creado (estado: solicitado)
* ✔ Transición controlada entre estados
* ✔ Validación de flujo correcto
* ✔ Restricción de cambios inválidos

---

### Restricciones

* ✔ Usuario sin permisos → 403
* ✔ Usuario no asignado → 403
* ✔ Transición inválida → 400

---

## 7. Control de Versiones

* Repositorio: [URL DEL REPO]
* Se realizaron commits progresivos por cada integrante

---

## 8. Conclusiones

* Se implementó autenticación segura con JWT
* Se aplicaron mecanismos de autorización mediante scopes
* Se logró controlar el flujo de estados de tickets
* Se aplicaron buenas prácticas de desarrollo backend

### Dificultades:

* Configuración de entorno
* Problemas con bcrypt
* Manejo de autenticación

### Soluciones:

* Ajuste de dependencias
* Manejo de errores
* Validación de lógica de negocio

---

# Instrucciones para ejecutar

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```
