
import unittest
import shutil
import os
import random

from io import StringIO
from contextlib import redirect_stdout
from itertools import product

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
        input_formats = ['dsl', 'json']
        datasets = ['dataset_1', 'dataset_2', 'dataset_3', 'dataset_4']
        output_formats = ['txt', 'csv', 'hex', 'bin']
        p = product(input_formats, datasets, output_formats)
        test_cases = []

        for input_format, dataset, output_format in p:
            f = '{}_{}.{}'.format(input_format, dataset, output_format)
            test_cases.append({
                'filename': f,
                'input': [
                    '10',
                    '-i', 'tests/datasets/{}.{}'.format(dataset, input_format),
                    '--input-format={}'.format(input_format),
                    '--output-type=file',
                    '-o', '{}'.format(output_format),
                    '-f', 'tests/datasets/results/{}'.format(f)
                ],
                'expected': 'tests/datasets/expected/{}'.format(f)
            })

        for test_case in test_cases:
            # initialize random seed to 0, so tests are repeatable
            random.seed(0)
            try:
                os.remove(
                    'tests/datasets/results/{}'.format(test_case['filename']))
            except:
                pass

            captured = StringIO()
            with redirect_stdout(captured):
                main(test_case['input'])

            results_file = open('tests/datasets/results/{}'.format(
                test_case['filename']), 'rb')
            results = results_file.read()

            expected_file = open('tests/datasets/expected/{}'.format(
                test_case['filename']), 'rb')
            expected = expected_file.read()

            assert_true(len(results) > 0)
            assert_true(len(expected) > 0)
            assert_equals(len(results), len(expected))
            assert_equals(results, expected)

            assert_true(captured.getvalue() == '')

            results_file.close()
            expected_file.close()
