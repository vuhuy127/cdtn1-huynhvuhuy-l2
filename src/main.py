from fastapi import FastAPI
from src.routes.ticket_router import router as ticket_router

app = FastAPI(title="Mekong Mobile Smart CRM - L2 API", version="1.0.0")

app.include_router(ticket_router)

@app.get("/")
def root():
    return {"message": "Hệ thống Smart CRM - Luồng L2 đang hoạt động ổn định!"}
