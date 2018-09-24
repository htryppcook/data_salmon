
class BinDatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_stream):
        fields = zip(*[x.evaluate('bin') for x in dataset.fields])

        for _, evaluated in zip(range(0, int(count)), fields):
            for field in evaluated:
                output_stream.write(field)
