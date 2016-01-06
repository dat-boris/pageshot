# -*- coding: utf-8 -*-
import sys

from setuptools import setup

requires = [
    "selenium",
    "Pillow"
]

setup(
    name="pageshot",
    version='0.0.0',
    description="",
    long_description="\n\n".join([open("README.md").read()]),
    author="Boris Lau",
    author_email="boris@mobify.com",
    url="https://github.com/mobify/pageshot",
    package=['pageshot'],
    install_requires=requires)
