
import abc

from ..strategies import StrategyEvaluationFactory
from ..errors import NotSupportedError

class Field(abc.ABC):
    '''
        Base class for fields.
    '''

    supported_strategies = ('value')

    def __init__(self, name, strategy, arguments=[]):
        if strategy not in self.supported_strategies:
            raise NotSupportedError(
                "'{} is not a supported choice method, supported: {}'".format(
                    strategy, self.supported_strategies))
        self.name = name
        self.strategy = strategy
        self.arguments = arguments

    def evaluate(self, output_format):
        '''
            Returns a generator that provides all expected values for this
            Field instance.
        '''
        gen = StrategyEvaluationFactory.evaluate_strategy(
                self.strategy).evaluate_field(self)()

        def format_generator():
            for item in gen:
                yield self.format(item, output_format)

        return format_generator()

    def format(self, item, output_format=None):
        raise NotImplementedError(
            'Output format {} is not implemented for this {}.'.format(
                output_format, type(self)))
