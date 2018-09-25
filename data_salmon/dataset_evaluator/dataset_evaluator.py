
from sys import stdout

from .csv_dataset_evaluator import CsvDatasetEvaluator
from .txt_dataset_evaluator import TxtDatasetEvaluator
from .hex_dataset_evaluator import HexDatasetEvaluator
from .bin_dataset_evaluator import BinDatasetEvaluator

class DatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_format, output_type='stdout',
            output_file=None, output_encoding='utf-8'):

        if output_type == 'stdout':
            output_stream = stdout.buffer
        elif output_type == 'file':
            output_stream = open(output_file, 'wb')
        else:
            raise NotImplementedError(
                '{} is not a valid output type.'.format(output_type))

        if output_format == 'csv':
            CsvDatasetEvaluator.evaluate(dataset, count, output_stream,
                output_encoding)
        elif output_format == 'txt':
            TxtDatasetEvaluator.evaluate(dataset, count, output_stream,
                output_encoding)
        elif output_format == 'hex':
            HexDatasetEvaluator.evaluate(dataset, count, output_stream,
                output_encoding)
        elif output_format == 'bin':
            BinDatasetEvaluator.evaluate(dataset, count, output_stream)
        else:
            raise NotImplementedError(
                "{} is not a valid output format".format(output_format))

        if output_type == 'file':
            output_stream.close()
