import os 
from typing import Callable

DEBUG_PRINTING = False

# readFile: str -> str
def readFile(filename : str) -> str:
    with open(filename, 'r') as f:
        return list(map(lambda line: line.replace("    ", "\t"), filter(lambda x: not x.isspace(), f.readlines())))#remove empty lines with only \n in them, filter is an higher order function also convert 4 spaces to 1 tab

class PrintingOutput:
    def __init__(self) -> None:
        self.output = ""
    
    def __call__(self, text):
        self.output += text
        return self.output
    
    def __str__(self) -> str:
        return self.output

# 
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

#add haskall notation todo
# def readFile(filename : str) -> str:
#     print("test")
#     print("Path at terminal when executing this file")
#     print(os.getcwd() + "\n")

#     print("This file path, relative to os.getcwd()")
#     print(__file__ + "\n")

#     print("This file full path (following symlinks)")
#     full_path = os.path.realpath(__file__)
#     print(full_path + "\n")

#     print("This file directory and name")
#     path, filename = os.path.split(full_path)
#     print(path + ' --> ' + filename + "\n")

#     print("This file directory only")
#     print(os.path.dirname(full_path))
#     print(2)
#     with open(os.path.join(os.getcwd() , filename), 'r') as f:
#         return f.readlines()