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

def update_note(db: Session, note_id: int, title: str, content: str):
       note = db.query(Note).filter(Note.id == note_id).first()
       if not note:
           return None
       note.title = title
       note.content = content
       db.commit()
       db.refresh(note)
       return note

def delete_note(db: Session, note_id: int):
       note = db.query(Note).filter(Note.id == note_id).first()
       if not note:
           return None
       db.delete(note)
       db.commit()
       return note