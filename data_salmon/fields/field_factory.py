
from . import Field
from . import StringField
from . import IntegerField

class FieldFactory:
    @classmethod
    def build_field(cls, typ, name, strategy, arguments):
        registered_types = list(StringField.supported_types) + \
                           list(IntegerField.supported_types)

        if typ not in registered_types:
            raise ValueError('Unknown type found: {}. Valid types: {}.'.format(
                typ, registered_types))

        if typ == 'string':
            return StringField(name, strategy, arguments)
        elif typ in IntegerField.supported_types:
            signed = False

            if typ.startswith('int'):
                signed = True
                bit_length = int(typ[3:])
            else:
                signed = False
                bit_length = int(typ[4:])

            return IntegerField(name, strategy, arguments, signed=signed,
                                bit_length=bit_length)
        else:
            return Field(name, strategy, arguments)
