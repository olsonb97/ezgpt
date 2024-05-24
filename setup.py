from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ezgpt',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai',
        'colorama'
    ],
    author='Brendan Olson',
    author_email='olsonb97@gmail.com',
    description='A simplified interface for the GPT API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/olsonb97/ezgpt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
