
import abc

from ..strategies import StrategyEvaluationFactory
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

    def evaluate(self, output_format):
        '''
            Returns a generator that provides all expected values for this
            Field instance.
        '''
        gen = StrategyEvaluationFactory.evaluate_strategy(
                self.method).evaluate_field(self)()

        def format_generator():
            for item in gen:
                yield self.format(item, output_format)

        return format_generator()

    def format(self, item, output_format=None):
        if output_format == None:
            return item
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))
