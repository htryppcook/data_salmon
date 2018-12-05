
import nose

from os import path

class TestSuite:
    @classmethod
    def run(cls):
        file_path = path.join(path.dirname(path.abspath(__file__)), 'tests')
        cover_packages = [
            'data_salmon.data_salmon',
            'data_salmon.cmd',
            'data_salmon.dataset',
            'data_salmon.dataset_evaluator',
            'data_salmon.dataset_writer',
            'data_salmon.errors',
            'data_salmon.fields',
            'data_salmon.input_file_loader',
            'data_salmon.strategies'
        ]
        nose.run(argv=[file_path, '--rednose', '--nologcapture',
            '--with-coverage', '--cover-erase']
            + ['--cover-package={}'.format(p) for p in cover_packages]
        )
