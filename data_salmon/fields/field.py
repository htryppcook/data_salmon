
import abc

from .choice_methods import ChoiceMethod
from ..errors import NotSupportedError

class Field(abc.ABC):
    '''
        Base class for fields.
    '''

    supported_choice_methods = ('value')

    def __init__(self, choice_method, value=None):
        if choice_method not in self.supported_choice_methods:
            raise NotSupportedError(
                "'{} is not a supported choice method, supported: {}'".format(
                    choice_method, self.supported_choice_methods))
        self.value = value
        self.choice_method = choice_method

    def evaluate(self):
        '''
            Returns a generator that provides all expected values for this
            Field instance.
        '''
        gen = ChoiceMethod.evaluate_choice_method(self.choice_method)(self)()

        def format_generator():
            for item in gen:
                yield self.format(item)

        return format_generator()

    def format(self, item, output_format=None):
        if output_format == None:
            return item
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))
