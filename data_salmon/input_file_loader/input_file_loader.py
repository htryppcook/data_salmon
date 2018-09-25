
import abc

from data_salmon.fields import Field
from data_salmon.fields import IntegerField
from data_salmon.fields import StringField

class InputFileLoader(abc.ABC):
    '''
        Abstract base class for loading data_salmon input files.
    '''

    @abc.abstractmethod
    def load(self, input_file_path):
        raise NotImplementedError