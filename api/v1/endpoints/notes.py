from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.note import NoteCreate, NoteOut
from services.note_service import create_note_service, get_all_notes_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note_service(db, note)

@router.get("/", response_model=list[NoteOut])
def read_notes(db: Session = Depends(get_db)):
    return get_all_notes_service(db)
