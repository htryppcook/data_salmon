
class BinDatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_file):
        with open(output_file, 'wb') as f:
            fields = zip(*[x.evaluate('bin') for x in dataset.fields])

            for _, evaluated in zip(range(0, int(count)), fields):
                for field in evaluated:
                    f.write(field)