
from data_salmon.dataset import Dataset

from .dsl_grammar import DSLGrammar

class DSLInputFileLoader:
    @classmethod
    def build_dataset(cls, parse_tree):
        print(parse_tree)

    @classmethod
    def load(cls, input_file_path):
        with open(input_file_path, 'r') as f:
            parsed = DSLGrammar().parse(f.read())

        if not parsed.is_valid:
            raise ValueError('Error parsing {}.'.format(input_file_path))

        dataset = DSLInputFileLoader.build_dataset(parsed)

        return dataset