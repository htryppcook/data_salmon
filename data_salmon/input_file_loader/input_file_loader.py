import abc

class InputFileLoader(abc.ABC):
    '''
        Abstract base class for loading data_salmon input files.
    '''
    @abc.abstractmethod
    def load(self, input_file_path):
        raise NotImplementedError