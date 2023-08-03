import os
import sys
import unittest

from Lexer.lexer import *
from Lexer.tokens import *
from Parser.parser import *
from Runner.runner import *
from Tools.tools import *

class TestRunWithNoCodeTest(unittest.TestCase):
    def test_runWithNoCode(self):
        consolePrinting = PrintingOutput()
        code, codePtr, state, output, functions = runABlock(CodeBlock(), 0, ProgramState(), consolePrinting, CodeBlock())
        self.assertEqual(output.output, "")

class TestHelloWorld(unittest.TestCase):
    def test_helloWorld(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/hello-world.txt"))
        consoleInput = ""#no input needed for hello world
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "Hello, world!")

class TestDoubleRecursiveFunctions(unittest.TestCase):
    def odd(self, n: int) -> int:
        if n == 0:
            return False
        return self.even(n - 1)
    
    def even(self, n: int) -> int:
        if n == 0:
            return True
        return self.odd(n - 1)
    
    
    def test_doubleRecursiveFunctionTestEven0(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        consoleInput = "0"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        if output.output == "1":#bool type does not exist in dirst so 1 is true and 0 is false
            resultDirst = True
        elif output.output == "0":
            resultDirst = False
        else:
            raise Exception("output is not 1 or 0")
        self.assertEqual(resultDirst, self.even(int(consoleInput)))
        
    def test_doubleRecursiveFunctionTestOdd39(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        consoleInput = "39"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        if output.output == "1":#bool type does not exist in dirst so 1 is true and 0 is false
            resultDirst = True
        elif output.output == "0":
            resultDirst = False
        else:
            raise Exception("output is not 1 or 0")
        self.assertEqual(resultDirst, self.even(int(consoleInput)))
    
    def test_doubleRecursiveFunctionTestEven40(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        consoleInput = "40"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        if output.output == "1":#bool type does not exist in dirst so 1 is true and 0 is false
            resultDirst = True
        elif output.output == "0":
            resultDirst = False
        else:
            raise Exception("output is not 1 or 0")
        self.assertEqual(resultDirst, self.even(int(consoleInput)))
        
    def test_doubleRecursiveFunctionTestEven300(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/evenOdd.txt"))
        consoleInput = "300"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        if output.output == "1":#bool type does not exist in dirst so 1 is true and 0 is false
            resultDirst = True
        elif output.output == "0":
            resultDirst = False
        else:
            raise Exception("output is not 1 or 0")
        self.assertEqual(resultDirst, self.even(int(consoleInput)))

class TestLoopigeFuncties(unittest.TestCase):
    def SommigInPython(self, n: int) -> int:
            result = 0  
            while(n >= 1):
                result += n
                n -= 1
            return result
        
    def test_SommigeFunctie_0(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        consoleInput = "0"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
    
    def test_SommigeFunctie_Minus1(self):       
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        consoleInput = "-1"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
        
    def test_SommigeFunctie_1(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        consoleInput = "1"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))#0 is even 
        
    def test_SommigeFunctie_100(self):       
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        consoleInput = "100"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
        
    def test_SommigeFunctie_900(self):       
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/sommig.txt"))
        consoleInput = "900"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.SommigInPython(int(consoleInput)))
        
class TestFibonacciSequence(unittest.TestCase):
    def fibonacciSeqInPython(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fibonacciSeqInPython(n - 1) + self.fibonacciSeqInPython(n - 2)
    
    def test_Fibonacci_0(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        consoleInput = "0"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        
    def test_Fibonacci_1(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        consoleInput = "1"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        
    def test_Fibonacci_2(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        consoleInput = "2"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        
    def test_Fibonacci_3(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        consoleInput = "3"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
    
    def test_Fibonacci_4(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        consoleInput = "4"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
    
    def test_Fibonacci_5(self):
        sys.setrecursionlimit(10000)
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Fib_seq_console_input.txt"))
        consoleInput = "5"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(int(output.output), self.fibonacciSeqInPython(int(consoleInput)))
        

class TestGreeter(unittest.TestCase):
    def test_greeter(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/Greeter.txt"))  
        consoleInput = "Herman"
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
        self.assertEqual(output.output, "What is your name? Hello Herman!")
        
class TestErrorTestCase(unittest.TestCase):
    def test_ErrorFunctionNotExisted(self):
        fileTree = readFile(os.path.join(os.getcwd() , "UnitTests/TestCode/FunctionNotExistedTest.txt"))
        consoleInput = ""
        consolePrinting = PrintingOutput()
        lex_output = lex(fileTree, consoleInput)
        errorListTokens = list(filter(lambda x: isinstance(x, ERR), lex_output))
        if len(errorListTokens) != 0:
            errorMessages = list(map(lambda x: x.message, errorListTokens))
            print(errorMessages)
            return
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertRaises(Exception, runABlock, parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)


        
if __name__ == '__main__':
    unittest.main()