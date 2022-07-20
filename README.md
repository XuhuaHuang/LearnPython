# LearnPython
 This repository contains code written in Python and Cython.

## Set a Method of a Class to be Pure Virtual
Secret attribute `__isabstract__` of function object; this can be declared and used as a decorator.
```Python
def abstractmethod(f):
    f.__isabstract__ = True
    return f
```

## Function parameters `args` and `kwargs`
```Python
def func_args(arg1=None, arg2=None, arg3=None):
	print(arg1, arg2, arg3)


def func_kwargs(arg1=None, arg2=None, arg3=None):
	print(arg1, arg2, arg3)


args_list = [1, 2, 3]
kwargs_dict = {"arg2": 2, "arg1": 1, "arg3": 3}

func_args(*args_list)
func_kwargs(**kwargs_dict)
```

## Working with Parametrized `pytest`
```Python
import pytest

@pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])
def test_string_is_digit(item):
    assert item.isdigit()
```
