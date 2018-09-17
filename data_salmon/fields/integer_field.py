
from .field import Field
from .choice_methods import ChoiceMethod

from ..errors import NotSupportedError

class IntegerField(Field):
    supported_choice_methods = [
        'value', 'incremental_range', 'random_range', 'ordered_choice',
        'random_choice'
    ]

    def __init__(self, value=None, increment=None, min=None, max=None,
            choice_method='value', choices=[]):
        super(IntegerField, self).__init__(choice_method)

        self.choices = choices
        self.min = min
        self.max = max
        self.increment = increment

        if value != None:
            self.value = int(value)

        if self.max != None:
            self.max += 1 # include the endpoint in range calculations

