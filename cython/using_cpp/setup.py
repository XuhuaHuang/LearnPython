from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Working with C++ in Cython',
    ext_modules=cythonize("rect.pyx"),
    zip_safe=False,
)