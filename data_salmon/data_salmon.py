
from .input_file_loader import JsonInputFileLoader
from .input_file_loader.dsl_input_file_loader import DSLInputFileLoader
from .dataset_evaluator import DatasetEvaluator

class data_salmon:
    def __init__(self):
        pass

    @classmethod
    def main(cls, namespace):
        if namespace.input_format == 'json':
            dataset = JsonInputFileLoader.load(namespace.input_file)
        elif namespace.input_format == 'dsl':
            dataset = DSLInputFileLoader.load(namespace.input_file)
        else:
            raise NotImplementedError(
                "{} input format is not implemented.".format(
                    namespace.input_format))

        DatasetEvaluator.evaluate(
            dataset, namespace.count, namespace.output_format,
            namespace.output_type, namespace.output_file,
            namespace.output_encoding)
