# -*- coding: utf-8 -*-
from utils import *
import argparse
import pickle
import csv
from types import *


def write_csv(data_dict):
    item_values = []
    for key in data_dict:
        value = data_dict.get(key, '')
        if isinstance(value, StringTypes):
            item_values.append(value.encode('utf-8'))
        else:
            item_values.append(value)
    return item_values

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract JSON, XML or CSV file from binary data file..')
    parser.add_argument('-p', '--path', help='Generated binary data file path', required=True)
    # if this param is not provided, display the result in the default output (the screen :D)
    parser.add_argument('-o', '--output', help='Output file path', required=False)

    args = parser.parse_args()
    with open(args.path, 'rb') as input:
        # loading the list of all stored objects from serialized-file
        data = pickle.load(input)

        write_header = True
        item_keys = []

        # if the user specified the output file path
        if args.output:
            # write the generated csv text in it
            with open("test.csv", 'wb') as csv_file:
                writer = csv.writer(csv_file)
                if len(data) > 0:
                    for k in data[0].__dict__:
                        item_keys.append(k)
                    writer.writerow(item_keys)
                    for item in data:
                        writer.writerow(write_csv(item.__dict__))
        else:
            # write the generated csv on the screen
            if len(data) > 0:
                for k in data[0].__dict__:
                    item_keys.append(k)
                print(",".join([str(mli) for mli in item_keys]))
                for item in data:
                    s = ",".join([str(mli) for mli in write_csv(item.__dict__)])
                    print(s)