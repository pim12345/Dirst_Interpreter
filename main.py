from typing import Tuple, List, Callable, Union, TypeVar, Optional
from functools import reduce
from Lexer.tokens import *
from Lexer.lexer import *
from Runner.runner import *
from Parser.parser import *
from Tools.tools import *
import logging
import os
#dectorator met decorator syntax toevoegen. hoofdstuk 3.5
#function to remove last file from string path
# def removeLastFileFromPath(path: str) -> str:
#     for i in range(len(path) - 1, 0, -1):
#         if path[i] == "/":
#             return path[:i]
#     return path


file = "./TestCode/loopigeFunction/sommigExample.txt"
#os.chdir('./TestCode/loopigeFunction/')
#fileTree = open("sommigExample.txt", "r")
#fileTree = readFile("./UnitTests/TestCode/loopigeFunction/sommigExample.txt")
fileTree = readFile("./Greeter.txt")
print(fileTree)
console_printing_INFO = lambda *args: print(*args)
consoleInput = {"pim", "test"}

lex_output = lex(fileTree, consoleInput)
#print(lex_output)
#print("lexed")

tree = CodeBlock()
parse = parseCodeBlock(lex_output, tree)[1]
#print("parsed")
#print(parse)
#print("begin run a block")
code, codePtr, state, output = runABlock(parse, 0, ProgramState(), console_printing_INFO)
#print("output: ", output)
#print("output2: ", out2)
#runner(parse)
#fileTree.close()
print("end of program")