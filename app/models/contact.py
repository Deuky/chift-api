from typing import Optional
from sqlmodel import Field, SQLModel

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: int
    name: str
    email: str

    def __eq__(self, other):
        if (not isinstance(other, Contact)):
            return False

        for key, value in self:
            if (key == "id"):
                continue

            if (getattr(self, key) != getattr(other, key)):
                return False

        return True

    def update(self, other):
        for key, value in self:
            if (key == "id"):
                continue

            if (key == "external_id"):
                continue

            setattr(self, key, getattr(other, key))

        return self
