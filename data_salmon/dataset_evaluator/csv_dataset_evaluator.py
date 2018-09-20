
class CsvDatasetEvaluator:
    @classmethod
    def evaluate(cls, dataset, count, output_file):
        with open(output_file, 'w') as f:
            header = ','.join([x.name for x in dataset.fields])
            fields = zip(*[x.evaluate('csv') for x in dataset.fields])

            f.write(header + "\n")
            for _, evaluated in zip(range(0, int(count)), fields):
                f.write(','.join(evaluated) + "\n")