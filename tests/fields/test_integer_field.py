
from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields.integer_field import IntegerField

class TestIntegerField:
    def test_integer_field(self):
        test_cases = [
            {
                'input': {
                    'kwargs': {
                        'value': 1
                    }
                },
                'expected': {
                    'value': 1,
                    'increment': None,
                    'min': None,
                    'max': None,
                    'method': 'value',
                    'choices': []
                }
            },
            {
                'input': {
                    'kwargs': {
                        'method': 'random_range',
                        'increment': 1,
                        'min': 1,
                        'max': 42
                    }
                },
                'expected': {
                    'value': None,
                    'increment': 1,
                    'min': 1,
                    'max': 43,
                    'method': 'random_range',
                    'choices': []
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
                    'value': 1,
                    'bit_length': None,
                    'output_format': 'txt'
                },
                'expected': '1'
            },
            {
                'input': {
                    'value': 255,
                    'bit_length': 1,
                    'output_format': 'hex'
                },
                'expected': 'ff'
            },
            {
                'input': {
                    'value': 65535,
                    'bit_length': 2,
                    'output_format': 'hex'
                },
                'expected': 'ffff'
            },
            {
                'input': {
                    'value': 65535,
                    'bit_length': 2,
                    'output_format': 'bin'
                },
                'expected': bytes([0xff, 0xff])
            },
            {
                'input': {
                    'value': 65535,
                    'bit_length': 4,
                    'output_format': 'bin'
                },
                'expected': bytes([0x00, 0x00, 0xff, 0xff])
            },
            {
                'input': {
                    'value': 65535,
                    'bit_length': 1,
                    'output_format': 'bin'
                },
                'expected': OverflowError()
            },
            {
                'input': {
                    'value': 65535,
                    'bit_length': 1,
                    'output_format': None
                },
                'expected': NotImplementedError()
            },
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(
                    name='field',
                    value=test_case['input']['value'],
                    bit_length=test_case['input']['bit_length'])
                assert_equals(
                    field.format(field.value,
                                 test_case['input']['output_format']),
                    test_case['expected'])
            except OverflowError as oe:
                assert_equals(type(oe), type(test_case['expected']))
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
