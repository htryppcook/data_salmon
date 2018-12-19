from nose.tools import assert_equals
from nose.tools import assert_true

from data_salmon.fields import IntegerField
from data_salmon.fields import StringField
from data_salmon.fields import LengthField
from data_salmon.input_file_loader.json_input_file_loader import \
    JsonInputFileLoader
from data_salmon.tests.datasets import Datasets

class TestJsonInputFileLoader:
    def test_load(self):
        with open(Datasets.input_file('dataset_1.json'), 'r') as input_file:
            dataset = JsonInputFileLoader.load(input_file)

        assert_equals(len(dataset.fields), 3)
        assert_equals(len(dataset.reflective_fields), 1)

        assert_true(isinstance(dataset.reflective_fields[0], LengthField))
        assert_equals(dataset.reflective_fields[0].name, 'field0_length')
        assert_equals(dataset.reflective_fields[0].strategy, 'length')
        assert_equals(dataset.reflective_fields[0].arguments, ['field0'])

        assert_true(isinstance(dataset.fields[0], LengthField))
        assert_equals(dataset.fields[0].name, 'field0_length')
        assert_equals(dataset.fields[0].strategy, 'length')
        assert_equals(dataset.fields[0].arguments, ['field0'])

        assert_true(isinstance(dataset.fields[1], IntegerField))
        assert_equals(dataset.fields[1].name, 'field0')
        assert_equals(dataset.fields[1].strategy, 'incremental_range')
        assert_equals(dataset.fields[1].arguments, [0, 100, 1])
        assert_equals(dataset.fields[1].bit_length, 32)
        assert_equals(dataset.fields[1].signed, True)

        assert_true(isinstance(dataset.fields[2], StringField))
        assert_equals(dataset.fields[2].name, 'field1')
        assert_equals(dataset.fields[2].strategy, 'value')
        assert_equals(dataset.fields[2].arguments, ['abcd'])
