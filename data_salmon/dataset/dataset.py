
from data_salmon.fields import Field
from data_salmon.fields import ReflectiveField

class Dataset:
    def __init__(self, name):
        self.name = name
        self.fields = list()
        self.reflective_fields = list()

    def append_field(self, field):
        if isinstance(field, ReflectiveField):
            self.reflective_fields.append(field)
            self.fields.append(field)
        elif isinstance(field, Field):
            self.fields.append(field)
        else:
            raise ValueError(('{} is not an instance of class Field or one of '
                'its subclasses.').format(type(field)))

    def __str__(self):
        output = "{}: [\n".format(self.name)

        for field in self.fields:
            output += "\t{} \n".format(field)
        output += "]"

        return output