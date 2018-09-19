
from ..dataset.output_formats import output_formats

from .field import Field

class StringField(Field):
    supported_choice_methods = ('value', 'ordered_choice', 'random_choice')

    def __init__(self, value=None, choice_method='value', choices=[]):
        super(StringField, self).__init__(choice_method)

        self.value = value
        self.choices = [str(choice) for choice in choices]

        if self.value != None:
            self.value = str(value)

    def format(self, item, output_format='txt'):
        if output_format == 'txt':
            return item
        elif output_format == 'hex':
            return item.encode().hex()
        elif output_format == 'bin':
            return item.encode() # defaults to utf-8
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))