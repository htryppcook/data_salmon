
class DatasetEvaluator:
    @staticmethod
    def evaluate(dataset, output_format):
        gen_dict = dict()

        for field in dataset.fields:
            gen_dict[field.name] = field.evaluate(output_format)

        def record_generator():
            while True:
                record = dict()

                # Iterate through self.fields because it's ordered
                for field in dataset.fields:
                    record[field.name] = next(gen_dict[field.name])

                yield record.values()
        return record_generator()