
import abc

from .choice_methods import ChoiceMethod
from ..errors import NotSupportedError

class Field(abc.ABC):
    '''
        Base class for fields.
    '''

    supported_choice_methods = ['value']

    def __init__(self, choice_method):
        if choice_method not in self.supported_choice_methods:
            raise NotSupportedError(
                "'{} is not a supported choice method, supported: {}'".format(
                    choice_method, self.supported_choice_methods))

        self.choice_method = ChoiceMethod.evaluate_choice_method(choice_method)

    def evaluate(self):
        '''
            Returns a generator that provides all expected values for this
            Field instance.
        '''
        return self.choice_method(self)()