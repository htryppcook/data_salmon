
import argparse

from .data_salmon import data_salmon

def main(*args, **kwargs):
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='dataset description file')
    parser.add_argument('count', help='number of records to generate')

    parser.add_argument('-fmt', '--format', help='dataset file format',
                        default='json')

    data_salmon.main(parser.parse_args())
