
from .field import Field

class IntegerField(Field):
    supported_strategies = (
        'value', 'incremental_range', 'random_range', 'ordered_choice',
        'random_choice'
    )

    supported_types = (
        'int16', 'int32', 'int64', 'uint16', 'uint32', 'uint64'
    )

    def __init__(self, name, typ, strategy='value', arguments=[]):
        super(IntegerField, self).__init__(name, typ, strategy, arguments)

        if typ not in self.supported_types:
            raise TypeError('Invalid integer type: {}'.format(typ))

        if typ.startswith('int'):
            signed = True
            bit_length = int(typ[3:])
        else:
            signed = False
            bit_length = int(typ[4:])

        self.bit_length = bit_length
        self.signed = signed

    def __str__(self):
        return ('IntegerField(strategy={}, arguments={}, bit_length={}, '
                'signed={})').format(
                    self.strategy, self.arguments, self.bit_length,
                    self.signed)

    def cast(self, item):
        return int(item)

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
