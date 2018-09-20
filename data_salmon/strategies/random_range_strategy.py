
import random

from .strategy import Strategy
from .utility import check_min_max

class RandomRangeStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        check_min_max(field)

        def random_range_generator():
            while True:
                yield random.randrange(field.min, field.max)
        return random_range_generator
