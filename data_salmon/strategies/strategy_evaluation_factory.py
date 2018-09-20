
import random

from .value_strategy import ValueStrategy
from .incremental_range_strategy import IncrementalRangeStrategy
from .ordered_choice_strategy import OrderedChoiceStrategy
from .random_choice_strategy import RandomChoiceStrategy
from .random_range_strategy import RandomRangeStrategy

class StrategyEvaluationFactory:
    @classmethod
    def evaluate_strategy(cls, strategy):
        if strategy == 'value':
            return ValueStrategy
        elif strategy == 'random_choice':
            return RandomChoiceStrategy
        elif strategy == 'ordered_choice':
            return OrderedChoiceStrategy
        elif strategy == 'incremental_range':
            return IncrementalRangeStrategy
        elif strategy == 'random_range':
            return RandomRangeStrategy
        else:
            raise NotImplementedError(
                "'{}' is not a valid choice method.".format(strategy))
