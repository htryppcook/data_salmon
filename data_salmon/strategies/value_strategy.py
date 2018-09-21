
from .strategy import Strategy

class ValueStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def value_generator():
            while True:
                yield field.arguments[0]
        return value_generator
