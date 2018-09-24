
from nose.tools import assert_equals

from data_salmon.fields import IntegerField
from data_salmon.strategies import OrderedChoiceStrategy

class TestOrderedChoiceStrategy:
    def test_ordered_choice(self):
        test_cases = [
            {
                'input': [0, 1, 2, 3],
                'expected': [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
            },
            {
                'input': [0, 1, 0, 0, 3],
                'expected': [0, 1, 0, 0, 3, 0, 1, 0, 0, 3, 0]
            }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(
                    name='field', typ='uint16', strategy='ordered_choice',
                    arguments=test_case['input'])
                gen = OrderedChoiceStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))