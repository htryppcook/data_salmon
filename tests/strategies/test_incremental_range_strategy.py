
from nose.tools import assert_equals

from data_salmon.fields import IntegerField
from data_salmon.strategies import IncrementalRangeStrategy

class TestIncrementalRangeStrategy:
    def test_incremental_range(self):
        test_cases = [
            {
                'input': { 'kwargs':{ 'increment':1, 'min':0, 'max':5 } },
                'expected': [0, 1, 2, 3, 4, 5, 0, 1]
            },
            {
                'input': { 'kwargs':{ 'increment':2, 'min':0, 'max':5 } },
                'expected': [0, 2, 4, 0, 2, 4]
            },
            {
                'input': { 'kwargs':{ 'increment':0, 'min':0, 'max':5 } },
                'expected': [0, 0, 0, 0]
            },
            {
                'input': { 'kwargs':{ 'increment':1, 'min':5, 'max':0 } },
                'expected': ValueError()
            },
            {
                'input': { 'kwargs':{ 'increment':-1, 'min':0, 'max':5 } },
                'expected': [0, 5, 4, 3, 2, 1, 0, 5]
            },
            { 'input': {'kwargs':{'value':1}}, 'expected': ValueError() },
            { 'input': {'kwargs':{'value':'1'}}, 'expected': ValueError() }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='incremental_range',
                    **test_case['input']['kwargs'])
                gen = IncrementalRangeStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    print(results)
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))