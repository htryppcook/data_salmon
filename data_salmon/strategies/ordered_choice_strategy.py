
from .strategy import Strategy

class OrderedChoiceStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        arguments = [field.cast(x) for x in field.arguments]

        def ordered_generator():
            index = 0
            length = len(arguments)
            while length == len(arguments):
                yield arguments[index]
                index += 1
                if index >= length:
                    index = 0
            raise StopIteration()
        return ordered_generator
