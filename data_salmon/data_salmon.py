
import sys

from .input_file_loader import JsonInputFileLoader
from .input_file_loader.dsl_input_file_loader import DSLInputFileLoader
from .dataset_evaluator import DatasetEvaluator

class DataSalmon:
    def __init__(self):
        pass

    @classmethod
    def main(cls, namespace):
        if namespace.input_type == 'stdin':
            input_stream = sys.stdin
        elif namespace.input_type == 'file':
            input_stream = open(namespace.input_file, 'r')
        else:
            raise NotImplementedError("{} is an invalid input type.".format(
                namespace.input_type))

        if namespace.input_format == 'json':
            dataset = JsonInputFileLoader.load(input_stream)
        elif namespace.input_format == 'dsl':
            dataset = DSLInputFileLoader.load(input_stream)
        else:
            raise NotImplementedError(
                "{} input format is not implemented.".format(
                    namespace.input_format))

        DatasetEvaluator.evaluate(
            dataset, namespace.count, namespace.output_format,
            namespace.output_type, namespace.output_file,
            namespace.output_encoding)

        input_stream.close()
