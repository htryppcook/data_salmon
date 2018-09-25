
class CsvDatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_stream, output_encoding):
        header = ','.join([x.name for x in dataset.fields])
        fields = zip(*[x.evaluate('csv') for x in dataset.fields])

        output_stream.write((header + "\n").encode(output_encoding))
        for _, evaluated in zip(range(0, int(count)), fields):
            output_stream.write(
                (','.join(evaluated) + "\n").encode(output_encoding))