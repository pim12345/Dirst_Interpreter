from typing import Tuple, List, Callable, Union, TypeVar, Optional
from functools import reduce
from tokens import *
from lexer import *
from runner import *
from Parser import *
import logging
#dectorator met decorator syntax toevoegen. hoofdstuk 3.5

fileTree = open("sommigExample.txt", "r")
console_printing_INFO = lambda *args: print(*args)


lex_output = lex(fileTree)
print(lex_output)
print("lexed")

tree = CodeBlock()
parse = parseCodeBlock(lex_output, tree)[1]
print("parsed")
print(parse)
print("begin run a block")
code, codePtr, state, output = runABlock(parse, 0, ProgramState(), console_printing_INFO)
print("output: ", output)
#print("output2: ", out2)
#runner(parse)
fileTree.close()
print("end of program")