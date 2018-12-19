
from . import Strategy

class NoneStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        def none_generator():
            while True:
                yield None
        return none_generator