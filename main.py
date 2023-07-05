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

def get_segment_combinations(arr, num_segments):
    if num_segments == 1:
        return [[arr]]
    segment_options = []
    for i in range(1, len(arr) - num_segments + 2):
        segment = arr[:i]
        remaining_segments = get_segment_combinations(arr[i:], num_segments - 1)
        for seg in remaining_segments:
            segment_options.append([segment] + seg)
    return segment_options

my_array = [1, 2, 3, 4, 5]
num_segments = 3
segment_combinations = get_segment_combinations(my_array, num_segments)
print(segment_combinations)

file = "./TestCode/loopigeFunction/sommigExample.txt"
os.chdir('./TestCode/loopigeFunction/')
#fileTree = open("sommigExample.txt", "r")
fileTree = readFile("sommigExample.txt")
print(fileTree)
console_printing_INFO = lambda *args: print(*args)


lex_output = lex(fileTree)
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