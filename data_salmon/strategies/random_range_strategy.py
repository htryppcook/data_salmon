
import random

from .strategy import Strategy

class RandomRangeStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        if len(field.arguments) != 2:
            raise ValueError('Random range arguments invalid, expecting: \n'
                'random_range(min, max)')

        minimum = field.arguments[0]
        maximum = field.arguments[1]

        if minimum > maximum:
            raise ValueError(('Minimum ({}) must be lower than '
                'maximum ({}).').format(minimum, maximum))

        def random_range_generator():
            while True:
                yield random.randrange(minimum, maximum)
        return random_range_generator
