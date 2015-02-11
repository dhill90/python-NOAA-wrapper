import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="python-NOAA-wrapper",
    version="0.1",
    author="Daniel Hill",
    author_email="dhill90@gmail.com",
    description=("A python wrapper for NOAA's NDFD API"),
    license="GPL v.3",
    keywords="python NOAA NDFD weather wrapper",
    url="https://github.com/dhill90",
    packages=['noaa-ndfd'],
    package_data={'noaa-ndfd': ['LICENSE.txt', 'README.md']},
    long_description=open('README.md').read(),
    #install_requires=['requests>=1.6'],
)
