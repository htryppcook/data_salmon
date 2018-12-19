
import random

from .strategy import Strategy

class RandomChoiceStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        arguments = [field.cast(x) for x in field.arguments]

        def random_choice_generator():
            length = len(arguments)
            while length == len(arguments):
                yield random.choice(arguments)
            raise StopIteration()
        return random_choice_generator