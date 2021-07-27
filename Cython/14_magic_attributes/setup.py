from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Magic attributes demo',
    ext_modules=cythonize("magic_attr.py"),
    zip_safe=False,
)