
import abc

class Strategy(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def evaluate_field(self, field):
        '''
            Evaluates a given field with the specified strategy.
            Returns a generator.
        '''