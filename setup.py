#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='recurrent-visual-attention',
    version='0.1a',
    description="""PyTorch implementation of Recurrent Models of Visual Attention: 
    Mnih, Volodymyr, Nicolas Heess, and Alex Graves.
    "Recurrent models of visual attention."
    Advances in neural information processing systems. 2014.https://arxiv.org/abs/1406.6247""",
    author='Kevin Zakka',
    author_email='https://github.com/kevinzakka/recurrent-visual-attention/issues',
    url='https://github.com/kevinzakka/recurrent-visual-attention',
    packages=find_packages(),
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ]
    )
