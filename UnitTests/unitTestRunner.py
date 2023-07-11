import unittest

# from . import readFile
from Lexer.tokens import *
from Lexer.lexer import *
from Runner.runner import *
from Parser.parser import *
from Tools.tools import *
import os


class TestRunner(unittest.TestCase):
    
    def test_helloWorld(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/hello-world.txt"))
        consoleInput = ""
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), consolePrinting)
        self.assertEqual(output.output, "Hello, world!")#0 is even
        
    def test_dubbeleRecursiveFunctionTestEven0(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/test_even_0.txt"))
        consoleInput = ""
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), consolePrinting)
        self.assertEqual(output.output, "1\n")#0 is even
        
    def test_dubbeleRecursiveFunctionTestOdd39(self):
        fileTree = readFile("./TestCode/dubbleRecursiveFunction/test_odd_39.txt")
        consoleInput = ""
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), consolePrinting)
        self.assertEqual(output.output, "1\n")
    
    def test_dubbeleRecursiveFunctionTestEven40(self):
        fileTree = readFile("./TestCode/dubbleRecursiveFunction/test_even_40.txt")
        consoleInput = ""
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tree = CodeBlock()
        parse = parseCodeBlock(lex_output, tree)[1]
        code, codePtr, state, output = runABlock(parse, 0, ProgramState(), consolePrinting)
        self.assertEqual(output.output, "0\n")
        
        
# class TestSubroutine(unittest.TestCase):
#     def dubbleRecursiveFunctionTest(self):
#         fileTree = open("../TestCode/loopigeFunction/sommigExample.txt", "r")
#         console_printing_INFO = lambda *args: print(*args)
#         lex_output = lex(fileTree)
#         tree = CodeBlock()
#         parse = parseCodeBlock(lex_output, tree)[1]
#         code, codePtr, state, output = runABlock(parse, 0, ProgramState(), console_printing_INFO)
#         fileTree.close()
#         # self.assertEqual 
        
# if __name__ == '__main__':
#     unittest.main()