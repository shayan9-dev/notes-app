from sqlalchemy.orm import Session
from crud import note as note_crud
from schemas.note import NoteCreate

def create_note_service(db: Session, note_in: NoteCreate):
    return note_crud.create_note(db, note_in)

def get_all_notes_service(db: Session):
    return note_crud.get_notes(db)
