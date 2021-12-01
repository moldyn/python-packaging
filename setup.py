# -*- coding: utf-8 -*-
import pathlib

import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# This call to setup() does all the work
setuptools.setup(
    name='slowpca',
    version='0.0.1',
    description='Slow principal component analysis.',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords=[
        'data analysis',
        'template',
    ],
    author='braniii',
    url='https://github.com/moldyn/python-packaging',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.10.0',
        'click>=7.0.0',
    ],
)
