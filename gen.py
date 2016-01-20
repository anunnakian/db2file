from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///Notes.db")


metadata = MetaData()
metadata.create_all(engine)
eleve = Table('eleve', metadata, autoload=True, autoload_with=engine)

for key in metadata.tables:
    eleve = Table(key, metadata, autoload=True, autoload_with=engine)
    print(eleve.__repr__())