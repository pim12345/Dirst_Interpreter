import os
import sys
import unittest

from Lexer.lexer import *
from Lexer.tokens import *
from Parser.parser import *
from Runner.runner import *
from Tools.tools import *


class TestHelloWorld(unittest.TestCase):
    def test_helloWorld(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/hello-world.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = ""#no input needed for hello world
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "Hello, world!")

class TestDoubleRecursiveFunctions(unittest.TestCase):
    def test_doubleRecursiveFunctionTestEven0(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "0"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "1")#0 is even
        
    def test_doubleRecursiveFunctionTestOdd39(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "39"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "0")
    
    def test_doubleRecursiveFunctionTestEven40(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "40"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "1")
        
    def test_doubleRecursiveFunctionTestEven300(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "300"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "1")

class TestLoopigeFuncties(unittest.TestCase):
    def SommigInPython(self,n: int ) -> int:
            result = 0  
            while(n >= 1):
                result += n
                n -= 1
            return result
        
    def test_SommigeFunctie_0(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "0"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))#0 is even 
    
    def test_SommigeFunctie_Minus1(self):       
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "-1"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
        
    def test_SommigeFunctie_1(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "1"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))#0 is even 
        
    def test_SommigeFunctie_100(self):       
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "100"
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
        
    def test_SommigeFunctie_900(self):       
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "900"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
        
class TestFibonacciSequence(unittest.TestCase):
    def fibonacciSeqInPython(self, n):
        if n <= 1:
            return n
        return self.fibonacciSeqInPython(n - 1) + self.fibonacciSeqInPython(n - 2)
    
    def test_Fibonacci_0(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "0"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        
    def test_Fibonacci_1(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "1"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        
    def test_Fibonacci_2(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "2"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        
    def test_Fibonacci_3(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "3"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
    
    def test_Fibonacci_4(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "4"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
    
    def test_Fibonacci_5(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "5"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        

class TestGreeter(unittest.TestCase):
    def test_greeter(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Greeter.txt"))
        filteredFileTree = list(filter(lambda x: x != "\n", fileTree))#remove empty lines with only \n in them, filter is an higher order function
        consoleInput = "Herman"#max recursion depth is default 1000,can be changed to an higher value, to support bigger functions
        consolePrinting = PrintingOutput()
        lex_output = lex(filteredFileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "What is your name? Hello Herman!")
        
        
if __name__ == '__main__':
    unittest.main()