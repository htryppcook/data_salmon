
from nose.tools import assert_equals

from data_salmon.dataset import Dataset
from data_salmon.fields import IntegerField

class TestDataset:
    def test_append_non_field(self):
        dataset = Dataset('dataset')

        try:
            dataset.append_field(None)
        except ValueError as ve:
            assert_equals(type(ve), ValueError)
            assert_equals(str(ve), "<class 'NoneType'> is not an instance of "
                "class Field or one of its subclasses.")

    def test_str(self):
        dataset = Dataset('dataset')

        dataset.append_field(IntegerField('field0', 'int16', 'value'))

        assert_equals(str(dataset),
            "dataset: [\n\tIntegerField(strategy=value, arguments=[], "
                "bit_length=16, signed=True) \n]")
