
from setuptools import setup

setup(
    name='data_salmon',
    version='0.0.1',
    author='htryppcook',
    setup_requires=[],
    install_requires=[],
    packages=[
        'data_salmon'
    ],
    entry_points={
        'console_scripts': [
            'data_salmon = data_salmon.cmd:main'
        ]
    }
)

