import unittest

from Lexer.lexer import *
from Lexer.tokens import *
from Parser.parser import *
from Runner.runner import *
from Tools.tools import *


class TestNoCodeTest(unittest.TestCase):
    def test_parseWithNoCode(self):
        tokens, parsedCode, parsedFunctions = parseCodeBlock("", CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])
        self.assertIsInstance(parsedCode, CodeBlock)
        self.assertEqual(parsedCode.statements, [])
        self.assertEqual(parsedCode.nestLevel, 0)
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        
        
class TestParserDirectorySubset(unittest.TestCase):
    def test_fnc(self):
        dirstCode = ["\tfnc_function_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedCode, CodeBlock)
        self.assertEqual(parsedCode.statements, [])#only 1 function declared so no code in main block
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(len(parsedFunctions.statements), 1)
        self.assertIsInstance(parsedFunctions.statements[0], DeclareFunction)
        self.assertEqual(parsedFunctions.statements[0].functionName, "function")
        self.assertEqual(parsedFunctions.statements[0].functionInputVar, "n")
        self.assertIsInstance(parsedFunctions.statements[0].block, CodeBlock)
        self.assertEqual(parsedFunctions.statements[0].block.statements, [])
        self.assertEqual(parsedFunctions.statements[0].block.nestLevel, 1)
    
    def test_dif(self): 
        dirstCode = ["\tdif_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        self.assertEqual(len(parsedCode.statements), 1)
        self.assertIsInstance(parsedCode.statements[0], Loop)
        self.assertEqual(parsedCode.statements[0].varConditionName, "n")
        
    def test_nif(self): 
        dirstCode = ["\tnif_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        self.assertEqual(len(parsedCode.statements), 1)
        self.assertIsInstance(parsedCode.statements[0], Loop)
        self.assertEqual(parsedCode.statements[0].varConditionName, "n")
        
    def test_lpc(self): 
        dirstCode = ["\tlpc_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        self.assertEqual(len(parsedCode.statements), 1)
        self.assertIsInstance(parsedCode.statements[0], Loop)
        self.assertEqual(parsedCode.statements[0].varConditionName, "n")
        
    def test_lpn(self): 
        dirstCode = ["\tlpn_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        self.assertEqual(len(parsedCode.statements), 1)
        self.assertIsInstance(parsedCode.statements[0], Loop)
        self.assertEqual(parsedCode.statements[0].varConditionName, "n")
        
    def test_dlw(self): 
        dirstCode = ["\tdlw_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        self.assertEqual(len(parsedCode.statements), 1)
        self.assertIsInstance(parsedCode.statements[0], Loop)
        self.assertEqual(parsedCode.statements[0].varConditionName, "n")
        
    def test_dlu(self): 
        dirstCode = ["\tdlu_n"]
        consoleInput = ""
        lex_output = lex(dirstCode, consoleInput)
        tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
        self.assertEqual(tokens, [])#parse code must loop trough all tokens, so it must return an empty list
        self.assertIsInstance(parsedFunctions, CodeBlock)
        self.assertEqual(parsedFunctions.statements, [])
        self.assertEqual(parsedFunctions.nestLevel, 0)
        self.assertEqual(len(parsedCode.statements), 1)
        self.assertIsInstance(parsedCode.statements[0], Loop)
        self.assertEqual(parsedCode.statements[0].varConditionName, "n")
        
