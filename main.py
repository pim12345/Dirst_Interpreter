from typing import List, Tuple
from tokens import *
from lexer import *
from runner import *
import functools
from Parser import *
#dectorator met decorator syntax toevoegen. hoofdstuk 3.5


fileTree = open("Fib_seq.txt", "r")


#print(fileTree.read())
#lambda x: x+x ,


lex_output = lex(fileTree)

tree = CodeBlock()
parse = parseCodeBlock(lex_output, tree)[1]
print(parse)
out = runABlock(parse, 0, ProgramState(), "")[1]
print(out)
#runner(parse)
fileTree.close()

