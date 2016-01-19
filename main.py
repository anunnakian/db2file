import os

retvalue = os.system("sqlacodegen mysql://root:glbtyoung@localhost/mymoney --outfile db.py")

from db import *
import db
import inspect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

for name, obj in inspect.getmembers(db):
    if inspect.isclass(obj):
        print(obj)

print(metadata.tables)

# engine = create_engine('mysql://root:glbtyoung@localhost/mymoney')
# engine.connect()
# Session = sessionmaker(bind=engine)
# session = Session()
#
# link = MymCategory()
# link.name = "Imane"
# link.creation_date = DateTime()
# link.last_updated = DateTime()
#
# session.add(link)
# session.commit()