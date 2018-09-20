
from .field import Field

class StringField(Field):
    supported_choice_methods = ('value', 'ordered_choice', 'random_choice')

    supported_types = ('string',)

    def __init__(self, name, value=None, method='value', choices=[]):
        super(StringField, self).__init__(name, method)

        self.value = value
        self.choices = [str(choice) for choice in choices]

        if self.value != None:
            self.value = str(value)

    def __str__(self):
        return 'StringField(value={}, method={}, choices={})'.format(
              self.value, self.method, self.choices)

    def format(self, item, output_format='txt'):
        if output_format == 'csv' or output_format == 'txt':
            return item
        elif output_format == 'hex':
            return item.encode().hex()
        elif output_format == 'bin':
            return item.encode() # defaults to utf-8
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))