
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields import IntegerField
from data_salmon.strategies import RandomRangeStrategy

class TestRandomRangeStrategy:
    def test_random_range(self):
        test_cases = [
            {
                'input': [0, 15],
                'expected': range(0, 100)
            },
            {
                'input': [15, 0],
                'expected': ValueError()
            }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(
                    name='field', typ='uint16', strategy='random_range',
                    arguments=test_case['input'])
                gen = RandomRangeStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    assert_true(int(results[0]) >= test_case['input'][0])
                    assert_true(int(results[0]) <= test_case['input'][1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))