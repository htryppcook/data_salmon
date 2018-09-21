
from .strategy import Strategy

class OrderedChoiceStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def ordered_generator():
            index = 0
            length = len(field.arguments)
            while length == len(field.arguments):
                yield field.arguments[index]
                index += 1
                if index >= length:
                    index = 0
            raise StopIteration()
        return ordered_generator
