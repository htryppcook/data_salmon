
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields.string_field import StringField

class TestStringField:
    def test_value(self):
        test_cases = [
            { 'input': {'kwargs':{'value':0}}, 'expected': ['0'] },
            { 'input': {'kwargs':{'value':1}}, 'expected': ['1'] },
            { 'input': {'kwargs':{'value':2}}, 'expected': ['2'] },
            { 'input': {'kwargs':{'value':'0'}}, 'expected': ['0'] },
            { 'input': {'kwargs':{'value':'1'}}, 'expected': ['1'] },
            { 'input': {'kwargs':{'value':None}}, 'expected': ['None'] },
            { 'input': {'kwargs':{'value':'a'}}, 'expected': ['a'] },
            { 'input': {'kwargs':{'value':[]}}, 'expected': ['[]'] },
            { 'input': {'kwargs':{'value':[0]}}, 'expected': ['[0]'] },
            { 'input': {'kwargs':{'value':{}}}, 'expected': ['{}'] },
            { 'input': {'kwargs':{'value':{'a':0}}},'expected': ["{'a': 0}"] },
            { 'input': {'kwargs':{'value':{0:'a'}}},'expected': ["{0: 'a'}"] }
        ]

        for test_case in test_cases:
            try:
                field = StringField(choice_method='value',
                    **test_case['input']['kwargs'])
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']):
                    print(results)
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))

    def test_ordered_choice(self):
        test_cases = [
            {
                'input': { 'kwargs': { 'choices': [0, 1, 2, 3] } },
                'expected': ['0', '1', '2', '3']
            },
            {
                'input': { 'kwargs': { 'choices': ['a', 'b', 'c', 'd'] } },
                'expected': ['a', 'b', 'c', 'd', 'a', 'b']
            }
        ]

        for test_case in test_cases:
            try:
                field = StringField(choice_method='ordered_choice',
                    **test_case['input']['kwargs'])
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))

    def test_random_choice(self):
        test_cases = [
            {
                'input': { 'kwargs': { 'choices': [0, 1, 2, 3] } },
                'expected': {
                    'count': range(0, 10),
                    'choices': ['0', '1', '2', '3']
                }
            },
            {
                'input': { 'kwargs': { 'choices': ['a', 'b', 'c', 'd'] } },
                'expected': {
                    'count': range(0, 10),
                    'choices': ['a', 'b', 'c', 'd']
                }
            }
        ]

        for test_case in test_cases:
            try:
                field = StringField(choice_method='random_choice',
                    **test_case['input']['kwargs'])
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']['count']):
                    assert_true(
                        results[0] in test_case['expected']['choices'])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))