# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='racepredictor',
    version='0.0.1',
    description='RacePrediction of ultra-runners',
    author='Alexander Åstrand',
    author_email='alexander.astrandens@gmail.com',
    url='https://github.com/astrandens/RacePredictor',
    packages=find_packages(exclude=('tests', 'docs'))
)