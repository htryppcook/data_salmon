
class CsvDatasetWriter:
    def __init__(self, dataset, records, output_encoding):
        self.header = ','.join([x.name for x in dataset.fields])
        self.records = records
        self.output_encoding = output_encoding

    def write(self, output_stream, count):
        output_stream.write((self.header + "\n").encode(self.output_encoding))
        for _, evaluated in zip(range(0, int(count)), self.records):
            output_stream.write(
                (','.join(evaluated) + "\n").encode(self.output_encoding))
