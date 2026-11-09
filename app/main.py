"""CampusVault v1: a small notes API. No database and no login yet (weeks 5 
and 8)."""
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Query, Response, status
from pydantic import BaseModel, ConfigDict, Field
app = FastAPI(title="CampusVault", version="1.0.0")


# ---------- DTOs: what may come in, what may go out ----------
class NoteCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")          
# unknown fields -> 422
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(default="", max_length=5000)
    class NoteUpdate(BaseModel):
        model_config = ConfigDict(extra="forbid")
    title: str | None = Field(default=None, min_length=1, max_length=100)
    body: str | None = Field(default=None, max_length=5000)
    class NoteOut(BaseModel):
        id: int
    title: str
    body: str
    created_at: datetime
# ---------- "Database": a dict in memory ----------
NOTES: dict[int, dict] = {}
_next_id = 1
@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
@app.post("/notes", response_model=NoteOut, 
status_code=status.HTTP_201_CREATED)
def create_note(data: NoteCreate, response: Response):
    global _next_id
    note = {"id": _next_id, "title": data.title, "body": data.body,
            "created_at": datetime.now(timezone.utc)}
    NOTES[_next_id] = note
    response.headers["Location"] = f"/notes/{_next_id}"
    _next_id += 1
    return note
# TODO 1: GET /notes            -> list, with ?limit= (1 to 100, default 20) and ?offset= (0 or more)
# TODO 2: GET /notes/{note_id}  -> one note, or 404 "Note not found"
# TODO 3: PATCH /notes/{note_id} -> change only the fields sent (hint: data.model_dump(exclude_unset=True))
# TODO 4: DELETE /notes/{note_id} -> 204 No Content, or 404