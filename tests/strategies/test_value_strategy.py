
from nose.tools import assert_equals

from data_salmon.strategies import ValueStrategy
from data_salmon.fields import IntegerField

class TestValueStrategy:
    def test_value(self):
        test_cases = [
            { 'input': [0], 'expected': [0] },
            { 'input': [1], 'expected': [1] },
            { 'input': [2], 'expected': [2] },
            { 'input': ['1'], 'expected': [1] },
            { 'input': ['0'], 'expected': [0] },
            { 'input': [None], 'expected': TypeError() },
            { 'input': ['a'], 'expected': ValueError() },
            { 'input': [[]], 'expected': TypeError() },
            { 'input': [[0]], 'expected': TypeError() },
            { 'input': [{}], 'expected': TypeError() },
            { 'input': [{'a':0}], 'expected': TypeError() },
            { 'input': [{0:'a'}], 'expected': TypeError() }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', strategy='value',
                    arguments=test_case['input'])
                gen = ValueStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                print(te)
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))
