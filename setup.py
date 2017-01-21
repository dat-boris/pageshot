# -*- coding: utf-8 -*-
import sys

from setuptools import setup

requires = [
    "selenium",
    "Pillow"
]

setup(
    name="pageshot",
    version='0.0.1',
    description="",
    long_description="\n\n".join([open("README.md").read()]),
    author="Boris Lau",
    author_email="boris@techie.im",
    url="https://github.com/sketchytechky/pageshot",
    packages=['pageshot'],
    install_requires=requires)
