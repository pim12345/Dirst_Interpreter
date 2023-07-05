import unittest

from Lexer.tokens import *
from Lexer.lexer import *
from Runner.runner import *
from Parser.parser import *
from Tools.tools import *

class TestRunner(unittest.TestCase):
    def dubbeleRecursiveFunctionTestEven0(self):
        fileTree = readFile("./TestCode/dubbleRecursiveFunction/test_even_0.txt")
        #console_printing_INFO = lambda *args: print(*args)
        test = ""
        lex_output = lex(fileTree)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), test)
        self.assertEqual(output, "0\n")
        
        
    def dubbeleRecursiveFunctionTestOdd39(self):
        fileTree = readFile("./TestCode/dubbleRecursiveFunction/test_odd_39.txt")
        console_printing_INFO = lambda *args: print(*args)
        lex_output = lex(fileTree)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), console_printing_INFO)
    
    def dubbeleRecursiveFunctionTestEven40(self):
        fileTree = readFile("./TestCode/dubbleRecursiveFunction/test_even_40.txt")
        console_printing_INFO = lambda *args: print(*args)
        lex_output = lex(fileTree)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), console_printing_INFO)