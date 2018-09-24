
import unittest
import shutil
import os
import random

from io import StringIO
from contextlib import redirect_stdout

from nose.tools import assert_true
from nose.tools import assert_equals

from data_salmon.cmd import main

class MainTest(unittest.TestCase):
    def test_main_help(self):
        captured = StringIO()
        with redirect_stdout(captured):
            try:
                main(['--help'])
            except SystemExit:
                pass

        assert_true(captured.getvalue() != None)

    def test_main_file_output(self):
        datasets = ['dataset_1', 'dataset_2', 'dataset_3', 'dataset_4']
        output_formats = ['txt', 'csv', 'hex', 'bin']
        test_cases = []

        for dataset in datasets:
            for output_format in output_formats:
                f = '{}.{}'.format(dataset, output_format)
                test_cases.append({
                    'filename': f,
                    'input': [
                        'tests/datasets/{}.dsl'.format(dataset), '10',
                        '--output-type=file',
                        '--output-format={}'.format(output_format),
                        '--output-file=tests/datasets/results/{}'.format(f)
                    ],
                    'expected': 'tests/datasets/expected/{}'.format(f)
                })

        # initialize random seed to 0, so tests are repeatable
        random.seed(0)

        for test_case in test_cases:
            os.remove(
                'tests/datasets/results/{}'.format(test_case['filename']))
            captured = StringIO()
            with redirect_stdout(captured):
                main(test_case['input'])

            assert_equals(
                open('tests/datasets/results/{}'.format(
                    test_case['filename']), 'rb').read(),
                open('tests/datasets/expected/{}'.format(
                    test_case['filename']), 'rb').read())

            assert_true(captured.getvalue() == '')
