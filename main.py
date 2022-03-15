from typing import Tuple, List, Callable, Union, TypeVar, Optional
from functools import reduce
from tokens import *
from lexer import *
from runner import *
from Parser import *
#dectorator met decorator syntax toevoegen. hoofdstuk 3.5


fileTree = open("Fib_seq.txt", "r")


#print(fileTree.read())
#lambda x: x+x ,

print("start")
lex_output = lex(fileTree)
print(lex_output)
print("lexed")

tree = CodeBlock()
parse = parseCodeBlock(lex_output, tree)[1]
print("parsed")
print(parse)
#out = runABlock(parse, 0, ProgramState(), "")[1]
#print(out)
#runner(parse)
fileTree.close()

