
from os import path

class Datasets:
    input_dir = path.join(path.dirname(path.abspath(__file__)), 'input')
    expected_dir = path.join(
        path.dirname(path.abspath(__file__)), 'expected')
    results_dir = path.join(
        path.dirname(path.abspath(__file__)), 'results')

    @classmethod
    def input_file(cls, f):
        return path.join(cls.input_dir, f)

    @classmethod
    def expected_file(cls, f):
        return path.join(cls.expected_dir, f)

    @classmethod
    def results_file(cls, f):
        return path.join(cls.results_dir, f)
