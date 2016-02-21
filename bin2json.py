# -*- coding: utf-8 -*-
from utils import *
import argparse
import pickle

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract JSON, XML or CSV file from binary data file..')
    parser.add_argument('-p', '--path', help='Generated binary data file path', required=True)
    # if this param is not provided, display the result in the default output (the screen :D)
    parser.add_argument('-o', '--output', help='Output file path', required=False)

    args = parser.parse_args()
    with open(args.path, 'rb') as input:
        # loading the list of all stored objects from serialized-file
        obj = pickle.load(input)
        obj = {"data":obj}

        # if the user specified the output file path
        if args.output:
            # write the generated json text in it
            with open(args.output, 'w') as outfile:
                json.dump(obj, outfile, check_circular=False, cls=AlchemyEncoder)
        else:
            # write the generated json on the screen
            print(json.dumps(obj, check_circular=False, cls=AlchemyEncoder))