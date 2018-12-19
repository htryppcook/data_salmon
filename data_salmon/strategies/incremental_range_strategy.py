
from .strategy import Strategy

class IncrementalRangeStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        if len(field.arguments) != 3:
            raise ValueError('Incremental range arguments invalid, expecting: '
                             '\nincremental_range(min, max, increment)')

        minimum = field.cast(field.arguments[0])
        maximum = field.cast(field.arguments[1])
        increment = field.cast(field.arguments[2])

        if minimum > maximum:
            raise ValueError(('Minimum ({}) must be lower than '
                'maximum ({}).').format(minimum, maximum))

        def incremental_generator():
            index = minimum
            while True:
                yield index
                index += increment
                if increment >= 0:
                    if index > maximum:
                        index = minimum
                else:
                    if index < minimum:
                        index = maximum

        return incremental_generator
