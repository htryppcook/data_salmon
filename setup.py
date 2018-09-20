
from setuptools import setup

setup(
    name='data_salmon',
    version='0.0.1',
    author='htryppcook',
    setup_requires=[],
    install_requires=[],
    packages=[
        'data_salmon',
        'data_salmon.dataset',
        'data_salmon.errors',
        'data_salmon.fields',
        'data_salmon.input_file_loader',
        'data_salmon.input_file_loader.json_input_file_loader',
        'data_salmon.dataset_evaluator',
        'data_salmon.strategies'
    ],
    entry_points={
        'console_scripts': [
            'data_salmon = data_salmon.cmd:main'
        ]
    }
)

