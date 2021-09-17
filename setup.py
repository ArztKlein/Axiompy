from setuptools import find_packages
from distutils.core import setup

setup(name='axiompy',
      version='0.1.1',
      description='Unit Conversions and other math',
      author='ArztKlein',
      author_email='',
      url='https://github.com/ArztKlein/Axiompy',
      keywords=['python','unit conversion', 'units'],
      setup_requires=['wheel'],
      python_requires='>3.6.1',
      packages=find_packages()
     )