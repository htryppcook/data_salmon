
from .utility import check_min_max
from .utility import check_increment

from .strategy import Strategy

class IncrementalRangeStrategy(Strategy):
    @classmethod
    def evaluate_field(cls, field):
        check_min_max(field)
        check_increment(field)

        def incremental_generator():
            index = field.min
            while True:
                yield index
                index += field.increment
                if field.increment >= 0:
                    if index >= field.max:
                        index = field.min
                else:
                    if index < field.min:
                        index = field.max - 1
        return incremental_generator
