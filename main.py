# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import

import os

import argparse
from sqlacodegen.codegen import CodeGenerator
import sqlacodegen
from sqlalchemy.orm import create_session

import codecs
import sys

from sqlalchemy import *
import sqlalchemy

file = 'classes.py'
url = 'mysql://root:glbtyoung@localhost/4jva'

def welcome():
    print("****************************************************************")
    print("* Master Spécialisé Big Data & Cloud Computing, Promotion 2015 *")
    print("****************************************************************")
    print("SQLaCodeGen version: " + sqlacodegen.version)


def generate():
    print("Generating SQLAlchemy model code from an existing database...")
    engine = create_engine(url)
    metadata = MetaData(bind=engine)
    metadata.reflect(engine, schema=None, views=True, only=None)
    outfile = codecs.open(file, 'w', encoding='utf-8') if file else sys.stdout
    generator = CodeGenerator(metadata, noindexes=False, noconstraints=False, nojoined=False, noinflect=False,
                              noclasses=False)
    generator.render(outfile)
    print("Generated [OK].")


if __name__ == '__main__':
    welcome()

    if (os.path.isfile(file)):
        print("SQLAlchemy model code already generated.")
    else:
        parser = argparse.ArgumentParser(description='Generates SQLAlchemy model code from an existing database.')
        parser.add_argument('url', nargs='?', help='SQLAlchemy url to the database')
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

        if not url:
            print('You must supply a url\n', file=sys.stderr)
            parser.print_help()
            exit(1)

        engine = create_engine(url)
        metadata = MetaData(bind=engine)

        from multiprocessing import Process

        generator = Process(target=generate)
        generator.start()
        generator.join()

    # generate class for each table, then it create a file that include all generated classes
    # retvalue = os.system("sqlacodegen mysql://root:glbtyoung@localhost/mymoney --outfile classes.py")

    engine = create_engine(url)
    metadata = MetaData(bind=engine)

    from classes import *
    import classes
    import inspect
    import pickle

    session = create_session(bind=engine)

    # get all classes from the generated module
    for name, obj in inspect.getmembers(classes):
        # get a list of generated classes only, without other classes like 'Integer','DateTime'...etc
        if inspect.isclass(obj) and obj.__module__ == 'classes':
            # print the class name
            testlist = session.query(obj).all()
            print(len(testlist))
            with open("data/" + obj.__tablename__ + '.data', 'wb') as output:
                pickle.dump(testlist, output, pickle.HIGHEST_PROTOCOL)
