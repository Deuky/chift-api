import sqlmodel
import dsnparser
from os import path

class Database(): 
    def __init__(self, dsn, password_file=False):
        if (path.isfile(password_file)):
            with open(password_file, 'r') as passfile:
                password = passfile.read().strip();
                dsnparsed = dsnparser.parse(dsn)
                dsnparsed["password"] = password
                dsn = f"{dsnparsed["driver"]}://{dsnparsed["user"]}:{dsnparsed["password"]}@{dsnparsed["host"]}:{dsnparsed["port"]}/{dsnparsed["database"]}"

        self.dsn = dsn

    def __enter__(self):
        self.engine = sqlmodel.create_engine(self.dsn)
        sqlmodel.SQLModel.metadata.create_all(self.engine)
        self.session = sqlmodel.Session(self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.engine.dispose()

    def select(self, model):
        return sqlmodel.select(model)

    def exec(self, statement):
        return self.session.exec(statement)

    def insert(self, model, commit=False):
        r = self.session.add(model)
        if (commit):
            self.commit()

        return r

    def update(self, model):
        return sqlmodel.update(model.__class__)

    def add(self, model, commit=False):
        r = self.session.add(model)
        if (commit):
            self.commit()

        return r

    def delete(self, model, commit=False):
        r = self.session.delete(model)
        if (commit):
            self.commit()

        return r

    def commit(self):
        return self.session.commit()