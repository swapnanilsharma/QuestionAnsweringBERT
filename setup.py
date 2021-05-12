# -*- coding: utf-8 -*-
"""
Created on Wed May 12 08:10:00 2021
@author: Swapnanil Sharma, https://github.com/swapnanilsharma
""" 

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="QuestionAnsweringBERT",
    version="0.1",
    description="BERT base question answering implementation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/swapnanilsharma/QuestionAnsweringBERT",
    author="Swapnanil Sharma",
    author_email="swapnanilsharma@gmail.com",
    license="MIT",
    keywords = ['Question Answering','BERT','BERT Embeddings','BERT Transformer', 'Transformer', 'Tensorflow'], 
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["QuestionAnsweringBERT"],
    include_package_data=True,
    install_requires=['numpy', 'tensorflow', 'transformers'],
)