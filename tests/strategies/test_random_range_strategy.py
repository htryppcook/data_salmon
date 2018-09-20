
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields import IntegerField
from data_salmon.strategies import RandomRangeStrategy

class TestRandomRangeStrategy:
    def test_random_range(self):
        test_cases = [
            {
                'input': { 'kwargs': { 'min': 0, 'max': 2 } },
                'expected': range(0, 11)
            }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='random_range',
                    **test_case['input']['kwargs'])
                gen = RandomRangeStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    assert_true(
                        int(results[0]) >= test_case['input']['kwargs']['min'])
                    assert_true(
                        int(results[0]) <= test_case['input']['kwargs']['max'])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))