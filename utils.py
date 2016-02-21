# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import
import json
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