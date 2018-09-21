
import argparse

from .data_salmon import data_salmon

def main(*args, **kwargs):
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', help='dataset description file')
    parser.add_argument('count', help='number of records to generate')
    parser.add_argument('output_file', help='output file name')

    parser.add_argument('-if', '--input-format', help='dataset file format',
                        default='dsl', choices=['json', 'dsl'])

    parser.add_argument('-of', '--output-format', help='output file format',
                        default='csv', choices=['txt', 'csv', 'hex', 'bin'])

    data_salmon.main(parser.parse_args())
