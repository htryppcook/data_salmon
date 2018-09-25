
from nose.tools import assert_equals

from data_salmon.fields.field_factory import FieldFactory

class TestFieldFactory:
    def test_build_field(self):
        test_cases = [
            {
                'input': {
                    'name': 'field0',
                    'typ': 'string',
                    'strategy': 'value',
                    'arguments': ['abcd']
                },
                'expected': {
                    'name': 'field0',
                    'strategy': 'value',
                    'arguments': ['abcd']
                }
            },
            {
                'input': {
                    'name': 'field1',
                    'typ': 'int16',
                    'strategy': 'value',
                    'arguments': [42],
                },
                'expected': {
                    'name': 'field1',
                    'strategy': 'value',
                    'arguments': [42],
                    'bit_length': 16
                }
            },
            {
                'input': {
                    'name': 'field2',
                    'typ': 'int64',
                    'strategy': 'value',
                    'arguments': [42],
                },
                'expected': {
                    'name': 'field2',
                    'strategy': 'value',
                    'arguments': [42],
                    'bit_length': 64
                }
            },
            {
                'input': {
                    'name': 'field3',
                    'typ': 'int42',
                    'strategy': 'value',
                    'arguments': [42],
                },
                'expected': ValueError("Unknown type found: int42. Valid "
                    "types: ['string', 'int16', 'int32', 'int64', 'uint16', "
                    "'uint32', 'uint64'].")
            }
        ]

        for test_case in test_cases:
            try:
                field = FieldFactory.build_field(**test_case['input'])
                print(field)
                for key in test_case['expected'].keys():
                    assert_equals(getattr(field, key), test_case['expected'][key])
            except TypeError as te:
                print(str(te))
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                print(str(ve))
                assert_equals(type(ve), type(test_case['expected']))