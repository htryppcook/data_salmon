
from data_salmon.errors import ArgumentError
from data_salmon.strategies import NoneStrategy

from .integer_field import IntegerField
from .reflective_field import ReflectiveField

class LengthField(IntegerField, ReflectiveField):
    length_strategy_name = 'length'
    supported_strategies = (length_strategy_name)

    def evaluate(self, output_format):
        ''' Override Field's evaluate method as we won't need it. '''
        return NoneStrategy.evaluate_field(None)()

    def reflective_evaluate(self, record, output_format):
        if len(self.arguments) != 1:
            raise ArgumentError(
                'Invalid number of arguments ({}) for field {} - {}'
                    .format(len(self.arguments), self.name, self.arguments))

        reflected_field = self.arguments[0]

        if reflected_field not in record:
            raise ArgumentError(
                '{} not a valid identifier in the record - {}.'.format(
                    reflected_field, record.keys()))

        record[self.name] = self.format(
            len(record[reflected_field]), output_format)

    def __str__(self):
        return ('LengthField(strategy={}, arguments={}, bit_length={}, '
                'signed={})').format(
                    self.strategy, self.arguments, self.bit_length,
                    self.signed)
