
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields import IntegerField
from data_salmon.strategies import RandomChoiceStrategy

class TestRandomChoiceStrategy:
    def test_random_choice(self):
        test_cases = [
            {
                'input': { 'kwargs': { 'choices': [x for x in range(0,4)] } },
                'expected': {
                    'count': range(0,10),
                    'choices': [x for x in range(0,4)]
                }
            },
            {
                'input': { 'kwargs': { 'choices': [0, 1, 0, 0, 3] } },
                'expected': {
                    'count': range(0,10),
                    'choices': [0, 1, 3]
                }
            }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='random_choice',
                    **test_case['input']['kwargs'])
                gen = RandomChoiceStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']['count']):
                    assert_true(
                        results[0] in test_case['expected']['choices'])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))
