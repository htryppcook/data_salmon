
import sys
import argparse

from .data_salmon import DataSalmon

def main(argv=None):
    if argv == None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument('count', help='number of records to generate')

    parser.add_argument('--input-type', help='input type',
                        default='stdin', choices=['stdin', 'file'])
    parser.add_argument('--input-format', help='dataset file format',
                        default='dsl', choices=['json', 'dsl'])
    parser.add_argument('-i', '--input-file', help='dataset description file',
                        default=None)

    parser.add_argument('--output-type', help='output type',
                        default='stdout', choices=['stdout', 'file'])
    parser.add_argument('-o', '--output-format', help='output file format',
                        default='csv', choices=['txt', 'csv', 'hex', 'bin'])
    parser.add_argument('-f', '--output-file', help='output file name',
                        default=None)
    parser.add_argument('--output-encoding',
                        help='desired encoding for text-based output',
                        default='utf-8')

    DataSalmon.main(parser.parse_args(argv))

if __name__ == '__main__':
    main()
