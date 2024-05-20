from setuptools import setup
from Cython.Build import cythonize

setup(
    name='More on Cython Functions',
    ext_modules=cythonize("cython_fn.py"),
    zip_safe=False,
)
