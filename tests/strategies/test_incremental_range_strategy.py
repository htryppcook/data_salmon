
from nose.tools import assert_equals

from data_salmon.fields import IntegerField
from data_salmon.strategies import IncrementalRangeStrategy

class TestIncrementalRangeStrategy:
    def test_incremental_range(self):
        test_cases = [
            {
                'input': { 'arguments': [0, 5, 1] },
                'expected': [0, 1, 2, 3, 4, 5, 0, 1]
            },
            {
                'input': { 'arguments': [0, 5, 2] },
                'expected': [0, 2, 4, 0, 2, 4]
            },
            {
                'input': { 'arguments': [0, 5, 0] },
                'expected': [0, 0, 0, 0]
            },
            {
                'input': { 'arguments': [5, 0, 1] },
                'expected': ValueError()
            },
            {
                'input': { 'arguments': [0, 5, -1] },
                'expected': [0, 5, 4, 3, 2, 1, 0, 5]
            },
            { 'input': { 'arguments': [1] }, 'expected': ValueError() },
            { 'input': { 'arguments': ['1'] }, 'expected': ValueError() }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', strategy='incremental_range',
                    arguments=test_case['input']['arguments'])
                gen = IncrementalRangeStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))