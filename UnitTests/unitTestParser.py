import os
import sys
import unittest

from Lexer.lexer import *
from Lexer.tokens import *
from Parser.parser import *
from Runner.runner import *
from Tools.tools import *

class TestParser(unittest.TestCase):
    def test_parser(self):
        sys.setrecursionlimit(5000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))#todo add check if extention exitst
        #todo check voor niet bestaande functie
        consoleInput = "10"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "55")
        # self.assertEqual(codePtr, 0)
        # self.assertEqual(state.input, "10")
        # self.assertEqual(state.output, "55")
        # self.assertEqual(state.variables, {})
        # self.assertEqual(state.functions, {})
        # self.assertEqual(state.returnValues, {})
        # self.assertEqual(state.returnPointers, {})
        # self.assertEqual(state.returnValues, {})
        # self.assertEqual(state.returnPointers, {})
        # self.a