from typing import List, Tuple
from tokens import *
from lexer import *
import functools
from Parser import *
#dectorator met decorator syntax toevoegen. hoofdstuk 3.5


fileTree = open("Fib_seq.txt", "r")


#print(fileTree.read())
#lambda x: x+x ,


lex_output = lex(fileTree)

#tree = CodeBlock()
parseCodeBlock(lex_output, CodeBlock)

fileTree.close()

