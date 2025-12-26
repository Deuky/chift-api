from typing import Optional
from sqlmodel import Field, SQLModel

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: int
    first_name: str
    last_name: str
    email: str