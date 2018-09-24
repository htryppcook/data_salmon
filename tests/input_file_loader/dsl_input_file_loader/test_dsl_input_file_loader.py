
from nose.tools import assert_equals

from data_salmon.input_file_loader import DSLInputFileLoader

class TestDSLInputFileLoader:
    def test(self):
        test_cases = [
            {
                'input': 'tests/datasets/dataset_1.dsl',
                'expected': {
                    'dataset_name': 'dataset_1',
                    'total_fields': 2
                }
            },
            {
                'input': 'tests/datasets/dataset_2.dsl',
                'expected': {
                    'dataset_name': 'dataset_2',
                    'total_fields': 4
                }
            },
            {
                'input': 'tests/datasets/dataset_3.dsl',
                'expected': {
                    'dataset_name': 'dataset_3',
                    'total_fields': 6
                }
            },
            {
                'input': 'tests/datasets/error_dataset_1.dsl',
                'expected': ValueError(
                    '(tests/datasets/error_dataset_1.dsl) Error at 78, expecting '
                    '{"strategy"}.')
            }
        ]

        for test_case in test_cases:
            try:
                dataset = DSLInputFileLoader.load(test_case['input'])
                assert_equals(
                    dataset.name, test_case['expected']['dataset_name'])
                assert_equals(
                    len(dataset.fields), test_case['expected']['total_fields'])
            except ValueError as ve:
                assert_equals(type(ve), type(test_case['expected']))
                assert_equals(str(ve), str(test_case['expected']))
