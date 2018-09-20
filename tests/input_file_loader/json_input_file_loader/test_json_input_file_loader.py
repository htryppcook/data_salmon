from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields import IntegerField
from data_salmon.fields import StringField
from data_salmon.input_file_loader.json_input_file_loader import \
    JsonInputFileLoader

class TestJsonInputFileLoader:
    def test_build_field(self):
        test_cases = [
            {
                'input': {
                    'name': 'field0',
                    'type': 'string',
                    'method': 'value',
                    'value': 'abcd'
                },
                'expected': {
                    'method': 'value',
                    'value': 'abcd',
                    'choices': []
                }
            },
            {
                'input': {
                    'name': 'field1',
                    'type': 'int16',
                    'method': 'value',
                    'value': 42,
                },
                'expected': {
                    'method': 'value',
                    'value': 42,
                    'choices': [],
                    'min': None,
                    'max': None,
                    'increment': None,
                    'bit_length': 16
                }
            },
            {
                'input': {
                    'name': 'field2',
                    'type': 'int64',
                    'method': 'value',
                    'value': 42,
                },
                'expected': {
                    'method': 'value',
                    'value': 42,
                    'choices': [],
                    'min': None,
                    'max': None,
                    'increment': None,
                    'bit_length': 64
                }
            },
            {
                'input': {
                    'type': 'string',
                    'method': 'value',
                    'value': 'abcd'
                },
                'expected': ValueError(
                    "Field {'method': 'value', 'value': 'abcd'} missing name.")
            },
            {
                'input': {
                    'name': 'field3',
                    'type': 'int42',
                    'method': 'value',
                    'value': 42,
                },
                'expected': ValueError("Unknown type found: int42. Valid "
                    "types: ['string', 'int16', 'int32', 'int64', 'uint16', "
                    "'uint32', 'uint64'].")
            },
            {
                'input': {
                    'name': 'garbage',
                    'type': 'string',
                    'garbage': None
                },
                'expected': TypeError("__init__() got an unexpected keyword "
                    "argument 'garbage'")
            }
        ]

        for test_case in test_cases:
            try:
                field = JsonInputFileLoader.build_field(test_case['input'])
                print(field)
                for key in test_case['expected'].keys():
                    assert_equals(getattr(field, key), test_case['expected'][key])
            except TypeError as te:
                print(str(te))
                assert_equals(type(te), type(test_case['expected']))
            except ValueError as ve:
                print(str(ve))
                assert_equals(type(ve), type(test_case['expected']))

    def test_load(self):
        input_file = 'tests/datasets/dataset_1.json'
        dataset = JsonInputFileLoader.load(input_file)

        assert_equals(len(dataset.fields), 2)

        assert_true(isinstance(dataset.fields[0], StringField))
        assert_equals(dataset.fields[0].name, 'field0')
        assert_equals(dataset.fields[0].method, 'value')
        assert_equals(dataset.fields[0].value, 'abcd')

        assert_true(isinstance(dataset.fields[1], IntegerField))
        assert_equals(dataset.fields[1].name, 'field1')
        assert_equals(dataset.fields[1].method, 'value')
        assert_equals(dataset.fields[1].value, 65535)
        assert_equals(dataset.fields[1].bit_length, 32)
        assert_equals(dataset.fields[1].signed, True)