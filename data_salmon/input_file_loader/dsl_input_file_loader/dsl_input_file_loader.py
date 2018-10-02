
from data_salmon.dataset import Dataset
from data_salmon.fields import FieldFactory

from .dsl_grammar import DSLGrammar

class DSLInputFileLoader:
    '''
        Loads a dsl file and transforms it into data_salmon's internal format.
    '''
    @staticmethod
    def build_dataset(tree):
        start = tree.children[0]
        name = start.children[0]
        # start.children[1] = Token('{')
        fields = start.children[2].children
        # start.children[2] = Token('}')

        dataset = Dataset(name.string)

        for field in fields:
            field_type = field.children[0].string
            field_name = field.children[1].string
            # field.children[2] = Token('=')
            strategy = field.children[3].string
            # field.children[4].string = Token('(')
            strategy_arguments = filter(lambda x: x.string != ',',
                field.children[5].children)
            # field.children[6].string = Token(')')

            stripped = []
            for arg in strategy_arguments:
                if arg.string.startswith('"') and arg.string.endswith('"'):
                    stripped.append(arg.string[1:len(arg.string)-1])
                else:
                    stripped.append(arg.string)

            dataset.append_field(FieldFactory.build_field(
                field_type, field_name, strategy, stripped))

        return dataset

    @classmethod
    def load(cls, input_stream):
        parsed = DSLGrammar().parse(input_stream.read())

        if not parsed.is_valid:
            raise ValueError('({}) Error at {}, expecting {}.'.format(
                input_stream.name, parsed.pos, parsed.expecting))

        return DSLInputFileLoader.build_dataset(parsed.tree)
