
class HexDatasetWriter:
    def __init__(self, dataset, records, output_encoding):
        self.records = records
        self.output_encoding = output_encoding

    def write(self, output_stream, count):
        for _, evaluated in zip(range(0, int(count)), self.records):
            for field in evaluated:
                output_stream.write((field).encode(self.output_encoding))