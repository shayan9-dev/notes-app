from sqlalchemy.orm import Session
from crud import note as note_crud
from schemas.note import NoteCreate, NoteUpdate

def create_note_service(db: Session, note_in: NoteCreate):
    return note_crud.create_note(db, note_in)

def get_all_notes_service(db: Session):
    return note_crud.get_notes(db)

def update_note_service(db: Session, note_id: int, note_update: NoteUpdate):
    return note_crud.update_note(db, note_id, note_update.title, note_update.content)

def delete_note_service(db: Session, note_id: int):
       return note_crud.delete_note(db, note_id)