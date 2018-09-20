
from .strategy import Strategy

class ValueStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def value_generator():
            while True:
                yield field.value
        return value_generator
