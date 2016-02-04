# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import
import sqlacodegen.codegen as gen

from keyword import iskeyword

from sqlalchemy.util import OrderedDict

from sqlalchemy import *


class BD2CModelClass(gen.Model):
    parent_name = 'Base'

    def __init__(self, table, association_tables, inflect_engine, detect_joined):
        super(BD2CModelClass, self).__init__(table)
        self.name = self._tablename_to_classname(table.name, inflect_engine)
        self.children = []
        self.attributes = OrderedDict()

        # Assign attribute names for columns
        for column in table.columns:
            self._add_attribute(column.name, column)

        # Add many-to-one relationships
        pk_column_names = set(col.name for col in table.primary_key.columns)
        for constraint in sorted(table.constraints, key= gen._get_constraint_sort_key):
            if isinstance(constraint, ForeignKeyConstraint):
                target_cls = self._tablename_to_classname(constraint.elements[0].column.table.name, inflect_engine)
                if detect_joined and self.parent_name == 'Base' and set(constraint.columns) == pk_column_names:
                    self.parent_name = target_cls
                else:
                    relationship_ = gen.ManyToOneRelationship(self.name, target_cls, constraint, inflect_engine)
                    self._add_attribute(relationship_.preferred_name, relationship_)

        # Add many-to-many relationships
        for association_table in association_tables:
            fk_constraints = [c for c in association_table.constraints if isinstance(c, ForeignKeyConstraint)]
            fk_constraints.sort(key=gen._get_constraint_sort_key)
            target_cls = self._tablename_to_classname(fk_constraints[1].elements[0].column.table.name, inflect_engine)
            relationship_ = gen.ManyToManyRelationship(self.name, target_cls, association_table)
            self._add_attribute(relationship_.preferred_name, relationship_)

    @staticmethod
    def _tablename_to_classname(tablename, inflect_engine):
        camel_case_name = ''.join(part[:1].upper() + part[1:] for part in tablename.split('_'))
        return inflect_engine.singular_noun(camel_case_name) or camel_case_name

    @staticmethod
    def _convert_to_valid_identifier(name):
        assert name, 'Identifier cannot be empty'
        if name[0].isdigit() or iskeyword(name):
            name = '_' + name
        return gen._re_invalid_identifier.sub('_', name)

    def _add_attribute(self, attrname, value):
        attrname = tempname = self._convert_to_valid_identifier(attrname)
        counter = 1
        while tempname in self.attributes:
            tempname = attrname + str(counter)
            counter += 1

        self.attributes[tempname] = value
        return tempname

    def add_imports(self, collector):
        super(BD2CModelClass, self).add_imports(collector)

        if any(isinstance(value, gen.Relationship) for value in self.attributes.values()):
            collector.add_literal_import('sqlalchemy.orm', 'relationship')

        for child in self.children:
            child.add_imports(collector)


if __name__ == '__main__':
   print("Ok")