import sqlmodel

engine = sqlmodel.create_engine("mariadb://root:monsecret@mariadb:3306/chiftapi")
sqlmodel.SQLModel.metadata.create_all(engine)

with sqlmodel.Session(engine) as session:
    def select(model):
        return sqlmodel.select(model)

    def exec(statement):
        return session.exec(statement)