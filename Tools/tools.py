import os 
from typing import Callable, Self

DEBUG_PRINTING = False

# readFile: string -> string
def readFile(filename : str) -> str:
    with open(filename, 'r') as f:
        return list(map(lambda line: line.replace("    ", "\t"), filter(lambda x: not x.isspace(), f.readlines())))#remove empty lines with only \n in them, filter is an higher order function also convert 4 spaces to 1 tab

class PrintingOutput:
    def __init__(self, output: str="") -> None:
        self.output = output
    
    # __call__ : PrintingOutput -> string -> PrintingOutput
    def __call__(self, text: str) -> Self:
        return PrintingOutput(self.output+text)#return a new PrintingOutput object with the new output, because of functional programming
    
    # __str__ : PrintingOutput -> string
    def __str__(self) -> str:
        return self.output
    
    # __repr__ : PrintingOutput -> string
    def __repr__(self) -> str:
        return self.output

# function_debug_printing : Callable -> Callable
def function_debug_printing(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Before calling " + func.__name__ + "\n with args: " + str(args) + "\n and kwargs: " + str(kwargs) + "\n")
        results = func(*args, **kwargs)
        print("After calling " + func.__name__ + "\n with args: " + str(args) + "\n and kwargs: " + str(kwargs) + "\n")
        return results
    
    if DEBUG_PRINTING:
        return wrapper
    else:
        return func
