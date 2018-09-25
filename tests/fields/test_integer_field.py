
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
            field = IntegerField(name='field', typ='uint16',
                                 **test_case['input']['kwargs'])
            for key in test_case['expected'].keys():
                assert_equals(getattr(field, key), test_case['expected'][key])

    def test_format(self):
        test_cases = [
            {
                'input': {
                    'arguments': [1],
                    'type': '',
                    'output_format': 'txt'
                },
                'expected': TypeError()
            },
            {
                'input': {
                    'arguments': [255],
                    'type': 'uint16',
                    'output_format': 'hex'
                },
                'expected': '00ff'
            },
            {
                'input': {
                    'arguments': [65535],
                    'type': 'uint16',
                    'output_format': 'hex'
                },
                'expected': 'ffff'
            },
            {
                'input': {
                    'arguments': [65535],
                    'type': 'uint16',
                    'output_format': 'bin'
                },
                'expected': bytes([0xff, 0xff])
            },
            {
                'input': {
                    'arguments': [65535],
                    'type': 'uint32',
                    'output_format': 'bin'
                },
                'expected': bytes([0x00, 0x00, 0xff, 0xff])
            },
            {
                'input': {
                    'arguments': [65536],
                    'type': 'uint16',
                    'output_format': 'bin'
                },
                'expected': OverflowError()
            },
            {
                'input': {
                    'arguments': [65535],
                    'type': 'uint8',
                    'output_format': None
                },
                'expected': TypeError()
            },
        ]

        for test_case in test_cases:
            try:
                field = IntegerField(
                    name='field',
                    typ=test_case['input']['type'],
                    arguments=test_case['input']['arguments'])
                assert_equals(
                    field.format(field.arguments[0],
                                 test_case['input']['output_format']),
                    test_case['expected'])
            except TypeError as te:
                print(str(te))
                print(test_case['expected'])
                assert_equals(type(te), type(test_case['expected']))
            except OverflowError as oe:
                assert_equals(type(oe), type(test_case['expected']))
            except NotImplementedError as nie:
                assert_equals(type(nie), type(test_case['expected']))
