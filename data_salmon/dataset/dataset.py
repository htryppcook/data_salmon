
from data_salmon.fields import Field

class Dataset:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def append_field(self, field):
        if isinstance(field, Field):
            self.fields.append(field)
        else:
            raise ValueError(('{} is not an instance of class Field or one of '
                'its subclasses').format(type(field)))
