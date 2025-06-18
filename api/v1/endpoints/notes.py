from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.note import NoteCreate, NoteOut, NoteUpdate
from services.note_service import create_note_service, get_all_notes_service, update_note_service

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

@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    updated_note = update_note_service(db, note_id, note)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted_note = delete_note_service(db, note_id)
    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}