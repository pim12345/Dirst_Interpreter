from typing import List, Tuple
from tokens import *
from lexer import *

#def parsen(tokens):
#    if len(tokens) == 0:
#        return None, code
#    token, *rest = tokens

class SimpleStatement:
    def __init__(self, num=1):
        #self.name = name
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
    def __init__(self, block, varname):
        self.code = block
        self.varname = varname

    #__repr__ :: Loop -> String
    def __repr__(self) -> str:
        s = self.code.__repr__()
        return s

class createVar(SimpleStatement):
    def __init__(self, name):
        self.name = name
        #self.number = 1

    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "create var with name: " + str(self.name)

class deleteVar(SimpleStatement):
    def __init__(self, name):
        self.name = name
        #self.number = 1

    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "delete var with name: " + str(self.name)

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

class addValue(SimpleStatement):
    def __init__(self, parameter1, parameter2, parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " and " + str(self.parameter3)


class LoopOpen(SimpleStatement):
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "Open loop"


class valueCompare(SimpleStatement):
    def __init__(self, parameter1, parameter2, parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3

    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "parameter1: " + str(self.parameter1) + " parameter2: " + str(self.parameter2) + " parameter3: " + str(self.parameter3)

# parseCodeBlock :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parseCodeBlock(tokens: List[Token], code: CodeBlock) -> Tuple[List[Token], CodeBlock]:
    #print(code)
    if len(tokens) == 0:
        #print("end")
        return None, code
    #print(len(tokens))
    token, *rest = tokens
    if (token.isInALoop == 1 and rest[0].isInALoop == 0):#maak naar verschil is 1 en slaat nu 1 over. dus na deze statment nog 1 keer iets uitvoeren #(token.isInALoop == 1 and rest[0].isInALoop == 0):
        #print("activeerd!")
        #code aad huidige statement
        token.isInALoop = 0
        testlist = [token]
        test = parseCodeBlock(testlist, code)
        #print(test)
        return rest, code
    #if (token.isInALoop == 0):
    #    return rest, code
    if isinstance(token, Directory):
        #print("loop")
        code.addStatement(LoopOpen())
        newrest, block = parseCodeBlock(rest, CodeBlock(nest=code.nestlevel + 1))
        return parseCodeBlock(newrest, code.addStatement(Loop(block, token.varname)))
        #newrest, block = parseCodeBlock(rest, CodeBlock(nest=code.nestlevel + 1))
        #return parseCodeBlock(newrest, code.addStatement(Loop(block, token.varname)))
    if isinstance(token, DAT):
        #print("dat")
        if isinstance(token, add):
            return parseCodeBlock(rest, code.addStatement(addValue(token.parameter1, token.parameter2, token.parameter3)))
        if isinstance(token, les):
            return parseCodeBlock(rest, code.addStatement(valueCompare(token.parameter1, token.parameter2, token.parameter3)))
        if (isinstance(token, dsi) or isinstance(token, dic)):
            return parseCodeBlock(rest, code.addStatement(displayValue(token.parameter1)))
        if isinstance(token, set):
            return parseCodeBlock(rest, code.addStatement(setValue(token.parameter1, token.parameter2)))
    elif isinstance(token, TXT):
        #print("txt")
        return parseCodeBlock(rest, code.addStatement(displayValue(token.name)))
    elif isinstance(token, BIN):
        #print("bin")
        return rest, code
        return parseCodeBlock(rest, code.addStatement())
    elif isinstance(token, CSV):
        #print("csv")
        if isinstance(token,div):
            return parseCodeBlock(rest, code.addStatement(deleteVar(token.name)))   
        else: 
            return parseCodeBlock(rest, code.addStatement(createVar(token.name)))   
    else: 
        #print("else")
        return rest, code