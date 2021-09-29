from typing import List, Tuple
from tokens import *
from lexer import *

#def parsen(tokens):
#    if len(tokens) == 0:
#        return None, code
#    token, *rest = tokens

class SimpleStatement:
    def __init__(self, name, num):
        self.name = name
        self.number = num

#repeatStr :: String -> Integer -> String
def repeatStr(s : str, i : int):
    if (i <= 0):
        return ""
    return s + repeatStr(s, i - 1)

class CodeBlock:
    def __init__(self, nest=0):
        self.statements = []
        self.nestlevel = nest

    #addStatement :: CodeBlock -> SimpleStatement -> CodeBlock
    def addStatement(self, statement : SimpleStatement):
        self.statements.append(statement)
        return self

    def __str__(self):
        return self.__repr__()

    #__repr__ :: CodeBlock -> String
    def __repr__(self) -> str:
        nstr = repeatStr("   ", self.nestlevel)
        statestr = ''.join(map(lambda st: nstr + str(st) + "\n", self.statements))
        return "Begin Block: \n" + statestr + repeatStr("   ", self.nestlevel - 1) + "End Block"

class Loop(SimpleStatement):
    def __init__(self, block):
        self.code = block

    #__repr__ :: Loop -> String
    def __repr__(self) -> str:
        s = self.code.__repr__()
        return s

class createVar(SimpleStatement):
    def __init__(self, name):
        self.name = name
        self.number = 1

    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "create var with name: " + str(self.name)

class setValue(SimpleStatement):
    def __init__(self, name, newValue):
        self.name = name
        self.newValue = newValue
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "Existing var with name: " + str(self.name) + " has new value: " + str(self.newValue)

class displayValue(SimpleStatement):
    def __init__(self, value):
        self.value = value
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "Display the value: " + str(self.value)


# parseCodeBlock :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parseCodeBlock(tokens: List[Token], code: CodeBlock) -> Tuple[List[Token], CodeBlock]:
    print(len(tokens))
    #print(len(code))
    print(code)
    if len(tokens) == 0:
        return None, code
    token, *rest = tokens
    #if (token.isInALoop == 0):
    #    return rest, code
    if isinstance(token, DAT):
        if (isinstance(token, dsi) | isinstance(token, dic)):
            return parseCodeBlock(rest, code.addStatement(displayValue(token.parameter1)))
        if isinstance(token, set):
            return parseCodeBlock(rest, code.addStatement(setValue(token.parameter1, token.parameter2)))
    elif isinstance(token, TXT):
        return None, code
        return parseCodeBlock(rest, code.addStatement())
    elif isinstance(token, BIN):
        return None, code
        return parseCodeBlock(rest, code.addStatement())
    elif isinstance(token, CSV):
        return parseCodeBlock(rest, code.addStatement(createVar(token.name)))   
    elif isinstance(token, Directory):
        newrest, block = parseCodeBlock(rest, CodeBlock(nest=code.nestlevel + 1))
        return parseCodeBlock(newrest, code.addStatement(Loop(block)))