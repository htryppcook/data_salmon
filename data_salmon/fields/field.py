
import abc

from ..strategies import StrategyEvaluationFactory
from ..errors import NotSupportedError

class Field(abc.ABC):
    '''
        Base class for fields.
    '''

    supported_strategies = ('value')

    def __init__(self, name, typ, strategy, arguments=[]):
        if strategy not in self.supported_strategies:
            raise NotSupportedError(
                "'{} is not a supported strategy, supported: {}'".format(
                    strategy, self.supported_strategies))
        self.name = name
        self.typ = typ
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

    @abc.abstractmethod
    def cast(self, item):
        '''
            Abstract method used to cast a primitive to the internal
            representation used by a specific field implementation.

            For example we could define an enum field like so:

            python3:
            class EnumField:
                def __init__(self):
                    self.enum = {'orange': 0, 'blue':1, 'green': 2}
                def cast(self, item):
                    return self.enum[item]

            along with the following DSL:
            enum_field field0 = random_choice('orange', 'blue', 'green')

            which would output a field with value 0-2 chosen at random.
        '''
        raise NotImplementedError(
            'Cast is not implemented for {}.'.format(type(self)))

    @abc.abstractmethod
    def format(self, item, output_format=None):
        '''
            Abstract method used to convert a fields internal representation to
            the requested output format.

            For example, uint16 0 is stored as an int in the IntegerField
            class, when the requested output format is hex, the string "0000"
            will be output, for string output the character '0' will be output,
            for binary two 0 bytes will be written.
        '''
        raise NotImplementedError(
            'Output format {} is not implemented for this {}.'.format(
                output_format, type(self)))
