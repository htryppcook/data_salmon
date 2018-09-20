
import random

from .strategy import Strategy

class RandomChoiceStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def random_choice_generator():
            length = len(field.choices)
            while length == len(field.choices):
                yield random.choice(field.choices)
            raise StopIteration()
        return random_choice_generator