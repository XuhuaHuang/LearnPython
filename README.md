# LearnPython
 This repository contains code written in Python and Cython.

## Set a Method of a Class to be Pure Virtual
Secret attribute `__isabstract__` of function object
```Python
def abstractmethod(f):
    f.__isabstract__ = True
    return f
```
