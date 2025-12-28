from typing import Union

from fastapi import FastAPI
from database import Database
import models
import os

app = FastAPI()
db = Database(os.getenv("DATABASE_DSN"), os.getenv("DATABASE_PASSWORD_FILE"), [models.Contact])

@app.get("/contacts/{contact_id}")
def get_contact_by_id(contact_id):
    with db as session:
        return session.exec(session.select(models.Contact).where(models.Contact.id == contact_id)).first()

@app.get("/contacts/external_id/{external_id}")
def get_contact_by_external_id(external_id):
    with db as session:
        return session.exec(session.select(models.Contact).where(models.Contact.external_id == external_id)).first()

@app.get("/contacts")
def get_contact_all():
    with db as session:
        return session.exec(session.select(models.Contact)).fetchall()


