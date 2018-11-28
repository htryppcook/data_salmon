
from collections import OrderedDict

class DatasetEvaluator:
    @staticmethod
    def evaluate(dataset, output_format):
        # NOTE: rework for python 3.7 when dicts are ordered by default
        gen_dict = OrderedDict()

        for field in dataset.fields:
            gen_dict[field.name] = field.evaluate(output_format)

        def record_generator():
            while True:
                record = OrderedDict()

                # Iterate through self.fields because it's ordered
                for field in dataset.fields:
                    record[field.name] = next(gen_dict[field.name])

                yield record.values()
        return record_generator()