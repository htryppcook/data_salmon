
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.strategies import *

from data_salmon.fields.integer_field import IntegerField
from data_salmon.fields.string_field import StringField

class TestStrategyEvaluationFactory:
    def test_evaluation(self):
        test_cases = [
            {
                'input': 'value',
                'expected': ValueStrategy
            },
            {
                'input': 'random_choice',
                'expected': RandomChoiceStrategy
            },
            {
                'input': 'ordered_choice',
                'expected': OrderedChoiceStrategy
            },
            {
                'input': 'incremental_range',
                'expected': IncrementalRangeStrategy
            },
            {
                'input': 'random_range',
                'expected': RandomRangeStrategy
            },
            {
                'input': 'garbage',
                'expected': NotImplementedError()
            }
        ]

        for test_case in test_cases:
            try:
                assert_equals(
                    type(StrategyEvaluationFactory.evaluate_strategy(
                        test_case['input'])),
                    type(test_case['expected']))
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
