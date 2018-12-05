
import os

from setuptools import setup

setup(
    name='data_salmon',
    version='0.0.1',
    author='htryppcook',
    setup_requires=[],
    install_requires=[],
    packages=[
        'data_salmon',
        'data_salmon.cmd',
        'data_salmon.dataset',
        'data_salmon.errors',
        'data_salmon.fields',
        'data_salmon.input_file_loader',
        'data_salmon.input_file_loader.dsl_input_file_loader',
        'data_salmon.dataset_evaluator',
        'data_salmon.dataset_writer',
        'data_salmon.strategies',
        'data_salmon.tests',
        'data_salmon.tests.datasets',
        'data_salmon.tests.dataset',
        'data_salmon.tests.fields',
        'data_salmon.tests.input_file_loader',
        'data_salmon.tests.strategies'
    ],
    package_data={ 'data_salmon': [
            'tests/datasets/*.dsl',
            'tests/datasets/*.json',
            'tests/datasets/expected/*.bin',
            'tests/datasets/expected/*.csv',
            'tests/datasets/expected/*.hex',
            'tests/datasets/expected/*.txt',
            'tests/datasets/results/empty.txt'
        ]
    },
    entry_points={
        'console_scripts': [
            'data_salmon = data_salmon.cmd.cmd:main'
        ]
    }
)
