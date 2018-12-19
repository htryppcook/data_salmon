
from nose.tools import assert_equals

from data_salmon.input_file_loader import DSLInputFileLoader
from data_salmon.tests.datasets import Datasets

class TestDSLInputFileLoader:
    def test(self):
        test_cases = [
            {
                'input': Datasets.input_file('dataset_1.dsl'),
                'expected': {
                    'dataset_name': 'dataset_1',
                    'total_fields': 3,
                    'total_reflective_fields': 1,
                }
            },
            {
                'input': Datasets.input_file('dataset_2.dsl'),
                'expected': {
                    'dataset_name': 'dataset_2',
                    'total_fields': 4,
                    'total_reflective_fields': 0
                }
            },
            {
                'input': Datasets.input_file('dataset_3.dsl'),
                'expected': {
                    'dataset_name': 'dataset_3',
                    'total_fields': 6,
                    'total_reflective_fields': 0
                }
            },
            {
                'input': Datasets.input_file('error_dataset_1.dsl'),
                'expected': ValueError(
                    '(/app/data_salmon/tests/datasets/input/error_dataset_1.dsl'
                    ') Error at 78, expecting {"strategy"}.')
            }
        ]

        for test_case in test_cases:
            try:
                with open(test_case['input'], 'r') as input_file:
                    dataset = DSLInputFileLoader.load(input_file)
                assert_equals(
                    dataset.name, test_case['expected']['dataset_name'])
                assert_equals(
                    len(dataset.fields), test_case['expected']['total_fields'])
                assert_equals(
                    len(dataset.reflective_fields),
                    test_case['expected']['total_reflective_fields'])
            except ValueError as ve:
                print(str(ve))
                assert_equals(type(ve), type(test_case['expected']))
                assert_equals(str(ve), str(test_case['expected']))
