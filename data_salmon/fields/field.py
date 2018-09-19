
import abc

from .choice_methods import ChoiceMethod
from ..errors import NotSupportedError

class Field(abc.ABC):
    '''
        Base class for fields.
    '''

    supported_choice_methods = ('value')

    def __init__(self, name, method, value=None):
        if method not in self.supported_choice_methods:
            raise NotSupportedError(
                "'{} is not a supported choice method, supported: {}'".format(
                    method, self.supported_choice_methods))
        self.name = name
        self.value = value
        self.method = method

    def evaluate(self):
        '''
            Returns a generator that provides all expected values for this
            Field instance.
        '''
        gen = ChoiceMethod.evaluate_choice_method(self.method)(self)()

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
