from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Working with arrays in Cython',
    ext_modules=cythonize("py_arr.pyx"),
    zip_safe=False,
)
