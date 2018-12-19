
from data_salmon.dataset_evaluator import DatasetEvaluator

from .csv_dataset_writer import CsvDatasetWriter
from .txt_dataset_writer import TxtDatasetWriter
from .hex_dataset_writer import HexDatasetWriter
from .bin_dataset_writer import BinDatasetWriter

class DatasetWriterFactory:
    @staticmethod
    def build(dataset, output_format, output_encoding='utf-8'):
        records = DatasetEvaluator.evaluate(dataset, output_format)

        if output_format == 'csv':
            return CsvDatasetWriter(dataset, records, output_encoding)
        elif output_format == 'txt':
            return TxtDatasetWriter(dataset, records, output_encoding)
        elif output_format == 'hex':
            return HexDatasetWriter(dataset, records, output_encoding)
        elif output_format == 'bin':
            return BinDatasetWriter(dataset, records, output_encoding)
        else:
            raise NotImplementedError(
                "{} is not a valid output format".format(output_format))
