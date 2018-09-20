
from .field import Field

class IntegerField(Field):
    supported_choice_methods = (
        'value', 'incremental_range', 'random_range', 'ordered_choice',
        'random_choice'
    )

    supported_types = (
        'int16', 'int32', 'int64', 'uint16', 'uint32', 'uint64'
    )

    def __init__(self, name, value=None, increment=None, min=None, max=None,
            method='value', choices=[], bit_length=32, signed=False):
        super(IntegerField, self).__init__(name, method)

        self.value = value
        self.choices = choices
        self.min = min
        self.max = max
        self.increment = increment
        self.bit_length = bit_length
        self.signed = signed

        if value != None:
            self.value = int(value)

        if self.max != None:
            self.max += 1 # include the endpoint in range calculations

    def __str__(self):
        return ('IntegerField(value={}, method={}, choices={}, increment={}, '
                'min={}, max={}, bit_length={}, signed={})').format(
                    self.value, self.method, self.choices, self.increment,
                    self.min, self.max, self.bit_length, self.signed)

    def format(self, item, output_format='txt'):
        if output_format == 'csv' or output_format == 'txt':
            return str(item)
        elif output_format == 'hex':
            return (item).to_bytes(int(self.bit_length/8), 'big').hex()
        elif output_format == 'bin':
            return (item).to_bytes(int(self.bit_length/8), 'big')
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))
