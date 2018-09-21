
import random

from .strategy import Strategy

class RandomChoiceStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def random_choice_generator():
            length = len(field.arguments)
            while length == len(field.arguments):
                yield random.choice(field.arguments)
            raise StopIteration()
        return random_choice_generator