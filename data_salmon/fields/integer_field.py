
from ..dataset.output_formats import output_formats
from ..errors import NotSupportedError

from .field import Field
from .choice_methods import ChoiceMethod

class IntegerField(Field):
    supported_choice_methods = (
        'value', 'incremental_range', 'random_range', 'ordered_choice',
        'random_choice'
    )

    def __init__(self, value=None, increment=None, min=None, max=None,
            choice_method='value', choices=[], bit_length=32):
        super(IntegerField, self).__init__(choice_method)

        self.value = value
        self.choices = choices
        self.min = min
        self.max = max
        self.increment = increment
        self.bit_length = bit_length

        if value != None:
            self.value = int(value)

        if self.max != None:
            self.max += 1 # include the endpoint in range calculations

    def format(self, item, output_format='txt'):
        if output_format == 'txt':
            return str(item)
        elif output_format == 'hex':
            return (item).to_bytes(self.bit_length, 'big').hex()
        elif output_format == 'bin':
            return (item).to_bytes(self.bit_length, 'big')
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))
