from __future__ import unicode_literals, division, print_function, absolute_import

import os

import argparse
from sqlacodegen.codegen import CodeGenerator
import sqlacodegen

import codecs
import sys

from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

def generate(url, file='classes.py'):
    parser = argparse.ArgumentParser(description='Generates SQLAlchemy model code from an existing database.')
    parser.add_argument('url', nargs='?', help='SQLAlchemy url to the database')
    parser.add_argument('--version', action='store_true', help="print the version number and exit")
    parser.add_argument('--schema', help='load tables from an alternate schema')
    parser.add_argument('--tables', help='tables to process (comma-separated, default: all)')
    parser.add_argument('--noviews', action='store_true', help="ignore views")
    parser.add_argument('--noindexes', action='store_true', help='ignore indexes')
    parser.add_argument('--noconstraints', action='store_true', help='ignore constraints')
    parser.add_argument('--nojoined', action='store_true', help="don't autodetect joined table inheritance")
    parser.add_argument('--noinflect', action='store_true', help="don't try to convert tables names to singular form")
    parser.add_argument('--noclasses', action='store_true', help="don't generate classes, only tables")
    parser.add_argument('--outfile', help='file to write output to (default: stdout)')
    args = parser.parse_args()

    if args.version:
        print(sqlacodegen.version)
        return
    if not url:
        print('You must supply a url\n', file=sys.stderr)
        parser.print_help()
        return

    engine = create_engine(url)
    metadata = MetaData(engine)
    tables = args.tables.split(',') if args.tables else None
    metadata.reflect(engine, args.schema, not args.noviews, tables)
    outfile = codecs.open(file, 'w', encoding='utf-8') if file else sys.stdout
    generator = CodeGenerator(metadata, args.noindexes, args.noconstraints, args.nojoined, args.noinflect,
                              args.noclasses)
    generator.render(outfile)

generate('mysql://root:glbtyoung@localhost/4jva')

# generate class for each table, then it create a file that include all generated classes
# retvalue = os.system("sqlacodegen mysql://root:glbtyoung@localhost/mymoney --outfile classes.py")

from classes import *
import classes
import inspect

# get all classes from the generated module
for name, obj in inspect.getmembers(classes):
    # get a list of generated classes only, without other classes like 'Integer','DateTime'...etc
    if inspect.isclass(obj) and obj.__module__ == 'classes':
        # print the class name
        print(obj.__name__)

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



