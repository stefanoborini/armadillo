import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

setup(
    name='armadillo',
    version="0.1.0",
    license='BSD 2-Clause License',
    description='The armadillo UI framework.',
    author='Stefano Borini',
    author_email='stefano.borini@gmail.com',
    url='https://github.com/stefanoborini/armadillo',
    packages=find_packages('src'),
    package_dir={'':'src'},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
    ],
    keywords=[
    ],
    install_requires=[
        "PyQt5",
        "traitlets"
    ],
    extras_require={
    },
    entry_points={
    },
)
