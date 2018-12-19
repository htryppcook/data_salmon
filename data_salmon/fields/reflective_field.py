
import abc

from .field import Field

class ReflectiveField(Field):
    @abc.abstractmethod
    def reflective_evaluate(self, fields):
        '''
            Abstract method used to evaluate this field against the entire set
            of generated fields for this record. This enables the generation of
            length fields that set their own value to the computed final
            lengths of other generated fields before the final record is
            written.
        '''
        raise NotImplementedError(
            'reflective_evaluate is not implemented for {}.'.format(
                type(self)))
