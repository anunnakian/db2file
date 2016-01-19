import os

# generate class for each table, then it create a file that include all generated classes
retvalue = os.system("sqlacodegen mysql://root:glbtyoung@localhost/mymoney --outfile classes.py")

from classes import *
import classes
import inspect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# get all classes from the generated module
for name, obj in inspect.getmembers(classes):
    # get a list of generated classes only, without other classes like 'Integer','DateTime'...etc
    if inspect.isclass(obj) and obj.__module__ == 'classes':
        # print the class name
        print(obj.__name__)

print(metadata.tables)

# this part of code can be useful for future use :)
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