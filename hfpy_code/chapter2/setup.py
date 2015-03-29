"""Setup you code
    Make publish file: use python setup.py sdist
    Install: python setup.py install
    Register: python setup.py register
    Upload: python setup.py sdist upload"""

from distutils.core import setup


setup(
    name='nester',
    version='1.0.0',
    author='arthor',
    author_email="arthor.cui@gmail.com",
    url='https://github.com/ArthorCui/PythonTrip/',
    description='A simple printer of nested lists',
)