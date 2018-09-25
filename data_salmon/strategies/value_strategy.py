
from .strategy import Strategy

class ValueStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        value = field.cast(field.arguments[0])
        def value_generator():
            while True:
                yield value
        return value_generator
