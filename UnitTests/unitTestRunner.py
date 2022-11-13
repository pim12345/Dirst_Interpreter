import unittest
from tokens import *
from lexer import *
from runner import *
from Parser import *




class TestSubroutine(unittest.TestCase):
    def dubbleRecursiveFunctionTest(self):
        fileTree = open("../TestCode/loopigeFunction/sommigExample.txt", "r")
        console_printing_INFO = lambda *args: print(*args)
        lex_output = lex(fileTree)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), console_printing_INFO)
        fileTree.close()
        # self.assertEqual