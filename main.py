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
fileTree = readFile("./evenOnEven2.txt")
#print(fileTree)
filterdFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function

print(filterdFileTree)
console_printing_INFO = lambda *args: print(*args, end="")
consoleInput = "10"

lex_output = lex(filterdFileTree, consoleInput)
#print(lex_output)
#print("lexed")

#tree = CodeBlock()#todo will be changed what not is allowed so change that code block only returns a list of statements, and this will not be changed
tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())#tree
#print("parsed")
#print(parse)
#print("begin run a block")
code, codePtr, state, output = runABlock(parsedCode, 0, ProgramState(), console_printing_INFO, parsedFunctions)
#print("output: ", output)
#print("output2: ", out2)
#runner(parse)
#fileTree.close()
print("end of program")