from typing import Union

from fastapi import FastAPI
from database import Database
import models
import os

app = FastAPI()

with Database(os.getenv("DATABASE_DSN"), os.getenv("DATABASE_PASSWORD_FILE")) as DB:
    @app.get("/contacts/{contact_id}")
    def get_contact_by_id(contact_id):
        return DB.exec(DB.select(models.Contact).where(models.Contact.id == contact_id)).first()

    @app.get("/contacts/external_id/{external_id}")
    def get_contact_by_external_id(external_id):
        return DB.exec(DB.select(models.Contact).where(models.Contact.external_id == external_id)).first()

    @app.get("/contacts")
    def get_contact_all():
        return DB.exec(DB.select(models.Contact)).fetchall()


