
import nose

from os import path

class TestSuite:
    @classmethod
    def run(cls):
        file_path = path.join('/', 'app', 'data_salmon')
        nose.run(argv=[file_path, '--rednose', '--nologcapture'])
