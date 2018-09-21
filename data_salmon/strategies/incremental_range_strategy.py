
from .strategy import Strategy

class IncrementalRangeStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        if len(field.arguments) != 3:
            raise ValueError('Incremental range arguments invalid, expecting: \n'
                'incremental_range(min, max, increment)')

        minimum = field.arguments[0]
        maximum = field.arguments[1] + 1
        increment = field.arguments[2]

        if minimum > maximum:
            raise ValueError(('Minimum ({}) must be lower than '
                'maximum ({}).').format(minimum, maximum))

        def incremental_generator():
            index = minimum
            while True:
                yield index
                index += increment
                if increment >= 0:
                    if index >= maximum:
                        index = minimum
                else:
                    if index < minimum:
                        index = maximum - 1

        return incremental_generator
