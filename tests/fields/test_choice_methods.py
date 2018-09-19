
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields.integer_field import IntegerField
from data_salmon.fields.string_field import StringField

class TestChoiceMethods:
    def test_value(self):
        test_cases = [
            { 'input': {'kwargs':{'value':0}}, 'expected': ['0'] },
            { 'input': {'kwargs':{'value':1}}, 'expected': ['1'] },
            { 'input': {'kwargs':{'value':2}}, 'expected': ['2'] },
            { 'input': {'kwargs':{'value':'0'}}, 'expected': ['0'] },
            { 'input': {'kwargs':{'value':'1'}}, 'expected': ['1'] },
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
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))

    def test_incremental_range(self):
        test_cases = [
            {
                'input': { 'kwargs':{ 'increment':1, 'min':0, 'max':5 } },
                'expected': ['0', '1', '2', '3', '4', '5', '0', '1']
            },
            {
                'input': { 'kwargs':{ 'increment':2, 'min':0, 'max':5 } },
                'expected': ['0', '2', '4', '0', '2', '4']
            },
            {
                'input': { 'kwargs':{ 'increment':0, 'min':0, 'max':5 } },
                'expected': ['0', '0', '0', '0']
            },
            {
                'input': { 'kwargs':{ 'increment':1, 'min':5, 'max':0 } },
                'expected': ValueError()
            },
            {
                'input': { 'kwargs':{ 'increment':-1, 'min':0, 'max':5 } },
                'expected': ['0', '5', '4', '3', '2', '1']
            },
            { 'input': {'kwargs':{'value':1}}, 'expected': ValueError() },
            { 'input': {'kwargs':{'value':'1'}}, 'expected': ValueError() }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='incremental_range',
                    **test_case['input']['kwargs'])
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']):
                    assert_equals(results[0], results[1])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))

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
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']):
                    assert_true(
                        int(results[0]) >= test_case['input']['kwargs']['min'])
                    assert_true(
                        int(results[0]) <= test_case['input']['kwargs']['max'])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))

    def test_ordered_choice(self):
        test_cases = [
            {
                'input': { 'kwargs': { 'choices': [0, 1, 2, 3] } },
                'expected': ['0', '1', '2', '3', '0', '1', '2', '3', '0']
            },
            {
                'input': { 'kwargs': { 'choices': [0, 1, 0, 0, 3] } },
                'expected': ['0', '1', '0', '0', '3', '0', '1', '0', '0', '3',
                             '0']
            }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='ordered_choice',
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
                'input': { 'kwargs': { 'choices': [x for x in range(0,4)] } },
                'expected': {
                    'count': range(0,10),
                    'choices': [str(x) for x in range(0,4)]
                }
            },
            {
                'input': { 'kwargs': { 'choices': [0, 1, 0, 0, 3] } },
                'expected': {
                    'count': range(0,10),
                    'choices': ['0', '1', '3']
                }
            }
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(name='field', method='random_choice',
                    **test_case['input']['kwargs'])
                gen = field.evaluate()
                for results in zip(gen, test_case['expected']['count']):
                    assert_true(
                        results[0] in test_case['expected']['choices'])
            except TypeError as te:
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))
