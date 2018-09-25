
from . import Field
from . import StringField
from . import IntegerField
from . import IPAddressField

class FieldFactory:
    @classmethod
    def build_field(cls, typ, name, strategy, arguments):
        registered_types = list(StringField.supported_types) + \
                           list(IntegerField.supported_types) + \
                           list(IPAddressField.supported_types)

        if typ not in registered_types:
            raise ValueError('Unknown type found: {}. Valid types: {}.'.format(
                typ, registered_types))

        if typ in StringField.supported_types:
            return StringField(name, typ, strategy, arguments)
        elif typ in IntegerField.supported_types:
            return IntegerField(name, typ, strategy, arguments)
        elif typ in IPAddressField.supported_types:
            return IPAddressField(name, typ, strategy, arguments)
        else:
            raise TypeError('Unrecognized type: {}.'.format(typ))
