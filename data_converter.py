# -*- coding: utf-8 -*-
import json
import argparse
import pickle
import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta


_visited_objects = []


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # don't re-visit self
            if obj in _visited_objects:
                return None
            _visited_objects.append(obj)

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


if __name__ == '__main__':
    import classes
    import inspect
    import os
    from types import *
    import json
    import csv


    #cree le repertoire csv s'il n'existe pas
    if not os.path.exists('csv'):
         os.mkdir('csv')
    # get all classes from the generated module
    for name, obj in inspect.getmembers(classes):

        # get a list of generated classes only, without other classes like 'Integer','DateTime'...etc
        if inspect.isclass(obj) and obj.__module__ == 'classes':
            json_data = []
            data = None
            write_header = True
            item_keys = []
            with open("json/" + obj.__tablename__ + '.json') as json_file:
                json_data = json_file.read()
            try:
                data = json.loads(json_data)
            except Exception as e:
                raise e
            with open("csv/" + obj.__tablename__ + '.csv', 'wb') as csv_file:
                writer = csv.writer(csv_file)
                for item in data:
                    item_values = []
                    for key in item:
                        if write_header:
                            item_keys.append(key)
                        value = item.get(key, '')
                        if isinstance(value, StringTypes):
                            item_values.append(value.encode('utf-8'))
                        else:
                            item_values.append(value)
                    if write_header:
                        writer.writerow(item_keys)
                        write_header = False
                    writer.writerow(item_values)


