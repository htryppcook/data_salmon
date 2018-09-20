
from .strategy import Strategy

class OrderedChoiceStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def ordered_generator():
            index = 0
            length = len(field.choices)
            while length == len(field.choices):
                yield field.choices[index]
                index += 1
                if index >= length:
                    index = 0
            raise StopIteration()
        return ordered_generator
