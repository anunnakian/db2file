# -*- coding: utf-8 -*-
import classes
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import *
import json
import argparse
import pickle
import datetime


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def new_alchemy_encoder():
    _visited_objs = []


    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    value = obj.__getattribute__(field)
                    if isinstance(value, datetime.datetime):
                        fields[field] = value.__str__()
                    else:
                        fields[field] = value
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract JSON, XML or CSV file from binary data file..')
    parser.add_argument('-p', '--path', help='Data file path', required=True)
    # if this param is not provided, display the result in the default output (the screen :D)
    parser.add_argument('-o', '--output', help='Output file path', required=False)
    args = parser.parse_args()
    with open(args.path, 'rb') as input:
        obj = pickle.load(input)
        print(json.dumps(obj, check_circular=False, cls=new_alchemy_encoder()))