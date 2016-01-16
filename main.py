from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Notes.db")

metadata = MetaData()
metadata.create_all(engine)
eleve = Table('eleve', metadata, autoload=True, autoload_with=engine)

print(eleve.__repr__())


