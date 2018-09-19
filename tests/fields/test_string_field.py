
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields.string_field import StringField

class TestStringField:
    def test_string_field(self):
        test_cases = [
            {
                'input': {
                    'kwargs': {
                        'value': 1
                    }
                },
                'expected': {
                    'value': '1',
                    'method': 'value',
                    'choices': []
                }
            },
            {
                'input': {
                    'kwargs': {
                        'method': 'ordered_choice',
                        'choices': ['a', 'b', 'c']
                    }
                },
                'expected': {
                    'value': None,
                    'method': 'ordered_choice',
                    'choices': ['a', 'b', 'c']
                }
            },
            {
                'input': {
                    'kwargs': {
                        'method': 'random_choice',
                        'choices': ['a', 'b', 'c']
                    }
                },
                'expected': {
                    'value': None,
                    'method': 'random_choice',
                    'choices': ['a', 'b', 'c']
                }
            },
            {
                'input': {
                    'kwargs': {
                        'value': 'abcd',
                        'method': 'ordered_choice',
                        'choices': ['a', 'b', 'c']
                    }
                },
                'expected': {
                    'value': 'abcd',
                    'method': 'ordered_choice',
                    'choices': ['a', 'b', 'c']
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
                    'value': 'a',
                    'output_format': 'txt'
                },
                'expected': 'a'
            },
            {
                'input': {
                    'value': 'a',
                    'output_format': 'hex'
                },
                'expected': '61'
            },
            {
                'input': {
                    'value': 'a',
                    'output_format': 'bin'
                },
                'expected': bytes([0x61])
            },
            {
                'input': {
                    'value': 65535,
                    'output_format': None
                },
                'expected': NotImplementedError()
            },
        ]

        for test_case in test_cases:
            try:
                field = StringField(
                    name='field', value=test_case['input']['value'])
                assert_equals(
                    field.format(field.value,
                                 test_case['input']['output_format']),
                    test_case['expected'])
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
