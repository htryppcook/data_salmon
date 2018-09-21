
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields.integer_field import IntegerField

class TestIntegerField:
    def test_integer_field(self):
        test_cases = [
            {
                'input': {
                    'kwargs': {
                        'arguments': [1]
                    }
                },
                'expected': {
                    'strategy': 'value',
                    'arguments': [1]
                }
            },
            {
                'input': {
                    'kwargs': {
                        'strategy': 'random_range',
                        'arguments': [1, 42, 1]
                    }
                },
                'expected': {
                    'strategy': 'random_range',
                    'arguments': [1, 42, 1]
                }
            }
        ]

        for test_case in test_cases:
            field = IntegerField(name='field', **test_case['input']['kwargs'])
            for key in test_case['expected'].keys():
                assert_equals(getattr(field, key), test_case['expected'][key])

    def test_format(self):
        test_cases = [
            {
                'input': {
                    'arguments': [1],
                    'bit_length': None,
                    'output_format': 'txt'
                },
                'expected': '1'
            },
            {
                'input': {
                    'arguments': [255],
                    'bit_length': 8,
                    'output_format': 'hex'
                },
                'expected': 'ff'
            },
            {
                'input': {
                    'arguments': [65535],
                    'bit_length': 16,
                    'output_format': 'hex'
                },
                'expected': 'ffff'
            },
            {
                'input': {
                    'arguments': [65535],
                    'bit_length': 16,
                    'output_format': 'bin'
                },
                'expected': bytes([0xff, 0xff])
            },
            {
                'input': {
                    'arguments': [65535],
                    'bit_length': 32,
                    'output_format': 'bin'
                },
                'expected': bytes([0x00, 0x00, 0xff, 0xff])
            },
            {
                'input': {
                    'arguments': [65535],
                    'bit_length': 8,
                    'output_format': 'bin'
                },
                'expected': OverflowError()
            },
            {
                'input': {
                    'arguments': [65535],
                    'bit_length': 8,
                    'output_format': None
                },
                'expected': NotImplementedError()
            },
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(
                    name='field',
                    arguments=test_case['input']['arguments'],
                    bit_length=test_case['input']['bit_length'])
                assert_equals(
                    field.format(field.arguments[0],
                                 test_case['input']['output_format']),
                    test_case['expected'])
            except OverflowError as oe:
                assert_equals(type(oe), type(test_case['expected']))
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
