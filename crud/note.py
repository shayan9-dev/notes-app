from sqlalchemy.orm import Session
from models.note import Note
from schemas.note import NoteCreate

def create_note(db: Session, note: NoteCreate) -> Note:
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session) -> list[Note]:
    return db.query(Note).all()
