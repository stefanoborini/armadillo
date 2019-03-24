from setuptools import setup, find_packages

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
    classifiers=[],
    keywords=[],
    install_requires=[
        "PyQt5",
        "traitlets"
    ],
    extras_require={},
    entry_points={},
)
