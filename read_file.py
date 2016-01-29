# -*- coding: utf-8 -*-

# classes module contains sqlacodegen generated classes
from classes import *

# implement an algorithm for serializing and de-serializing a Python object structure
import pickle

# you can change these values to test your case :)
file_to_read = "marks.data"

with open(file_to_read, 'rb') as input:
    obj = pickle.load(input)
    print(obj[0].ID)
    print(obj[0].COURSENAME)
