# -*- coding: utf-8 -*-

from classes import *
import pickle

with open('marks.data', 'rb') as input:
    obj = pickle.load(input)
    print(obj[0].ID)
    print(obj[0].COURSENAME)
