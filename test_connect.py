# -*- coding: utf-8 -*-
import os

import argparse
import sqlacodegen
from sqlalchemy.orm import create_session
import codecs
from sqlacodegen.codegen import *

import sys

from sqlalchemy import *

SERVER_TYPE = {'mysql': 'mysql://{0}:{1}@{2}/{3}', 'sqlite': 'sqlite://{4}', 'oracle': 'oracle://{0}:{1}@{2}/{3}',
               'postgresql': 'postgresql://{0}:{1}@{2}/{3}',
               'mssql': 'mssql://{0}:{1}@{2}/{3}'}

# build database link from parameters
def build_url(args):
    if args.type in SERVER_TYPE:
        print("Server Type : " + args.server)
        connect_string = SERVER_TYPE[args.type].format(args.username, args.password, args.server, args.database, args.location)
        print("Database connectionString = " + connect_string)
    else:
        print("Database Server Type not recognized!")
        exit(1)

    return connect_string



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build Database URL from parameters.')
    parser.add_argument('-t', '--type', help='Database server type', required=True)
    args = parser.parse_known_args()

    server_param_required = args[0].type != 'sqlite'
    parser.add_argument('-s', '--server', help='Database server type', default="localhost")
    parser.add_argument('-u', '--username', help='Database server type', required=server_param_required)
    parser.add_argument('-p', '--password', help='Database server type', required=server_param_required)
    parser.add_argument('-d', '--database', help='Database name', required=server_param_required)
    parser.add_argument('-l', '--location', help='Database path', required=not server_param_required)
    parser.add_argument('-o', '--output', help='Output file', required=False)

    args = parser.parse_args()
    # if not url:
    #     print('You must supply a url\n', file=sys.stderr)
    #     parser.print_help()
    #         exit(1)

    # building connection string
    url = build_url(args)

    # Connect to the database
    engine = create_engine(url)
    metadata = MetaData(bind=engine)
    exit(0)
