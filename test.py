from typing import Tuple, List, Callable, Union, TypeVar, Optional
from functools import reduce
from tokens import *
from lexer import *
from runner import *
from Parser import *




test = dif_("test",1)

match test:
    case dif_():
        print("test")
    case _:
        print("fail")
