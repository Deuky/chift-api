from typing import Union

from fastapi import FastAPI
from database import select, exec
import models

app = FastAPI()

@app.get("/contacts/{contact_id}")
def get_contact_by_id(contact_id):
    return exec(select(models.Contact).where(models.Contact.id == contact_id)).first()

@app.get("/contacts")
def get_contact_all():
    return list(exec(select(models.Contact)))


