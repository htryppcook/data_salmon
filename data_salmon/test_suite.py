
import nose

from os import path

class TestSuite:
    @classmethod
    def run(cls):
        file_path = path.join(path.dirname(path.abspath(__file__)), 'tests')
        nose.run(argv=[file_path, '--rednose', '--nologcapture',
            '--with-coverage', '--cover-erase',
            '--cover-package=data_salmon.data_salmon',
            '--cover-package=data_salmon.cmd',
            '--cover-package=data_salmon.dataset',
            '--cover-package=data_salmon.dataset_evaluator',
            '--cover-package=data_salmon.errors',
            '--cover-package=data_salmon.fields',
            '--cover-package=data_salmon.input_file_loader',
            '--cover-package=data_salmon.strategies'
        ])
