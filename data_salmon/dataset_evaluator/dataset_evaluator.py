
from .csv_dataset_evaluator import CsvDatasetEvaluator
from .txt_dataset_evaluator import TxtDatasetEvaluator
from .hex_dataset_evaluator import HexDatasetEvaluator
from .bin_dataset_evaluator import BinDatasetEvaluator

class DatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_format, output_file):

        if output_format == 'csv':
            CsvDatasetEvaluator.evaluate(dataset, count, output_file)
        elif output_format == 'txt':
            TxtDatasetEvaluator.evaluate(dataset, count, output_file)
        elif output_format == 'hex':
            HexDatasetEvaluator.evaluate(dataset, count, output_file)
        elif output_format == 'bin':
            BinDatasetEvaluator.evaluate(dataset, count, output_file)
        else:
            raise NotImplementedError(
                "{} is not a valid output format".format(output_format))
