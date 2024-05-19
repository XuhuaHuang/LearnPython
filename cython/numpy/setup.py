from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Working with Numpy in .py and .pyx',
    ext_modules=cythonize("convolve_py.py"),
    zip_safe=False,
)
