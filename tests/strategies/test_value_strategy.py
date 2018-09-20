
from nose.tools import assert_equals

from data_salmon.strategies import ValueStrategy
from data_salmon.fields import IntegerField

class TestValueStrategy:
    def test_value(self):
        test_cases = [
            { 'input': {'kwargs':{'value':0}}, 'expected': [0] },
            { 'input': {'kwargs':{'value':1}}, 'expected': [1] },
            { 'input': {'kwargs':{'value':2}}, 'expected': [2] },
            { 'input': {'kwargs':{'value':'0'}}, 'expected': [0] },
            { 'input': {'kwargs':{'value':'1'}}, 'expected': [1] },
            { 'input': {'kwargs':{'value':None}}, 'expected': TypeError() },
            { 'input': {'kwargs':{'value':'a'}}, 'expected': ValueError() },
            { 'input': {'kwargs':{'value':[]}}, 'expected': TypeError() },
            { 'input': {'kwargs':{'value':[0]}}, 'expected': TypeError() },
            { 'input': {'kwargs':{'value':{}}}, 'expected': TypeError() },
            { 'input': {'kwargs':{'value':{'a':0}}}, 'expected': TypeError() },
            { 'input': {'kwargs':{'value':{0:'a'}}}, 'expected': TypeError() }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='value',
                    **test_case['input']['kwargs'])
                gen = ValueStrategy.evaluate_field(field)()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                print(te)
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))
