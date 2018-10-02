
from sys import stdin
from sys import stdout

from .input_file_loader import JsonInputFileLoader
from .input_file_loader.dsl_input_file_loader import DSLInputFileLoader
from .dataset_evaluator import DatasetEvaluator

class DataSalmon:
    def __init__(self):
        pass

    @classmethod
    def main(cls, namespace):
        in_file = False
        out_file = False

        if namespace.input_type == 'file' or namespace.input_file != None:
            in_file = True
            input_stream = open(namespace.input_file, 'r')
        elif namespace.input_type == 'stdin':
            input_stream = stdin
        else:
            raise NotImplementedError("{} is an invalid input type.".format(
                namespace.input_type))

        if namespace.output_type == 'file' or namespace.output_file != None:
            out_file = True
            output_stream = open(namespace.output_file, 'wb')
        elif namespace.output_type == 'stdout':
            output_stream = stdout.buffer
        else:
            raise NotImplementedError(
                '{} is not a valid output type.'.format(namespace.output_type))

        if namespace.input_format == 'json':
            dataset = JsonInputFileLoader.load(input_stream)
        elif namespace.input_format == 'dsl':
            dataset = DSLInputFileLoader.load(input_stream)
        else:
            raise NotImplementedError(
                "{} input format is not implemented.".format(
                    namespace.input_format))

        DatasetEvaluator.evaluate(
            dataset, namespace.count, namespace.output_format, output_stream,
            namespace.output_encoding)

        if in_file:
            input_stream.close()

        if out_file:
            output_stream.close()
