"""FastAPI application entry point."""
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.config.database import database_is_ready, init_db
from src.routes.ticket_router import router as ticket_router
from src.seed import seed_demo_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    seed_demo_data()
    yield


app = FastAPI(
    title="Mekong Mobile Smart CRM - L2 API",
    description="Warranty intake and classification prototype.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Do not echo submitted values (phone number / IMEI) in validation responses.
    safe_errors = [
        {"loc": error.get("loc", []), "msg": error.get("msg", "Invalid input"), "type": error.get("type", "value_error")}
        for error in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": safe_errors})


@app.get("/", tags=["System"], summary="API welcome")
def root():
    return {"message": "Mekong Mobile Smart CRM - L2 API is running"}


@app.get("/health", tags=["System"], summary="Health check")
def health():
    try:
        database_is_ready()
        return {"status": "healthy", "database": "connected"}
    except Exception:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "database": "unavailable"},
        )


app.include_router(ticket_router)