
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields.string_field import StringField

class TestStringField:
    def test_string_field(self):
        test_cases = [
            {
                'input': {
                    'kwargs': {
                        'arguments': [1]
                    }
                },
                'expected': {
                    'strategy': 'value',
                    'arguments': ['1']
                }
            },
            {
                'input': {
                    'kwargs': {
                        'strategy': 'ordered_choice',
                        'arguments': ['a', 'b', 'c']
                    }
                },
                'expected': {
                    'strategy': 'ordered_choice',
                    'arguments': ['a', 'b', 'c']
                }
            },
            {
                'input': {
                    'kwargs': {
                        'strategy': 'random_choice',
                        'arguments': ['a', 'b', 'c']
                    }
                },
                'expected': {
                    'strategy': 'random_choice',
                    'arguments': ['a', 'b', 'c']
                }
            },
            {
                'input': {
                    'kwargs': {
                        'strategy': 'ordered_choice',
                        'arguments': ['a', 'b', 'c']
                    }
                },
                'expected': {
                    'strategy': 'ordered_choice',
                    'arguments': ['a', 'b', 'c']
                }
            },
        ]

        for test_case in test_cases:
            field = StringField(name='field', **test_case['input']['kwargs'])
            for key in test_case['expected'].keys():
                assert_equals(getattr(field, key), test_case['expected'][key])

    def test_format(self):
        test_cases = [
            {
                'input': {
                    'arguments': ['a'],
                    'output_format': 'txt'
                },
                'expected': 'a'
            },
            {
                'input': {
                    'arguments': ['a'],
                    'output_format': 'hex'
                },
                'expected': '61'
            },
            {
                'input': {
                    'arguments': ['a'],
                    'output_format': 'bin'
                },
                'expected': bytes([0x61])
            },
            {
                'input': {
                    'arguments': [65535],
                    'output_format': None
                },
                'expected': NotImplementedError()
            },
        ]

        for test_case in test_cases:
            try:
                field = StringField(
                    name='field', arguments=test_case['input']['arguments'])
                assert_equals(
                    field.format(field.arguments[0],
                                 test_case['input']['output_format']),
                    test_case['expected'])
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
