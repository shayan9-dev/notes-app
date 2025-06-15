from fastapi import APIRouter
from api.v1.endpoints import notes

router = APIRouter()
router.include_router(notes.router, prefix="/notes", tags=["Notes"])
