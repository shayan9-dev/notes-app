from fastapi import FastAPI
from db.base import Base
from db.session import engine
from api.v1.routes import router as api_router
from utils.error_handler import validation_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI(title="Notes App")

app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")
