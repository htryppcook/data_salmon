
from .field import Field

class StringField(Field):
    supported_choice_methods = ['value', 'ordered_choice', 'random_choice']

    def __init__(self, value=None, choice_method='value', choices=[]):
        super(StringField, self).__init__(choice_method)
        self.value = str(value)
        self.choices = [str(choice) for choice in choices]
