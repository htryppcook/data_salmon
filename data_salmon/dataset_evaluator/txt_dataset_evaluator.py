
class TxtDatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_stream, output_encoding):
        fields = zip(*[x.evaluate('txt') for x in dataset.fields])

        for _, evaluated in zip(range(0, int(count)), fields):
            for field in evaluated:
                output_stream.write((field).encode(output_encoding))