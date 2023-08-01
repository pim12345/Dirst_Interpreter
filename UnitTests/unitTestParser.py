import os
import sys
import unittest

from Lexer.lexer import *
from Lexer.tokens import *
from Parser.parser import *
from Runner.runner import *
from Tools.tools import *

# class TestParser(unittest.TestCase):
#     def test_parser(self):
#         sys.setrecursionlimit(5000)
#         fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
#         consoleInput = "0"
#         consolePrinting = PrintingOutput()
#         lex_output = lex(fileTree, consoleInput)
#         tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
#         print()
     
# class TestParserDirectorySubset(unittest.TestCase):
#     def test_fnc_Directory(self):
#         sys.setrecursionlimit(5000)
#         fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/fnc_Directory.txt"))
#         consoleInput = "0"
#         consolePrinting = PrintingOutput()
#         lex_output = lex(fileTree, consoleInput)
#         tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
#         print()



class TestParser(unittest.TestCase):
    def test_test(self):
        sys.setrecursionlimit(5000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/test.txt"))
        consoleInput = "0"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        print()