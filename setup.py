from setuptools import find_packages
from distutils.core import setup

setup(name='axiompy',
      version='0.2.1',
      description='Perform operations and conversions on units and values.',
      author='ArztKlein',
      author_email='',
      url='https://github.com/ArztKlein/Axiompy',
      keywords=['python','unit conversion', 'units'],
      setup_requires=['wheel', 'acfile'],
      python_requires='>3.6.1',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
            'acfile'
      ]
)