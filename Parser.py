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

class tempBinFunction(SimpleStatement):
    def __init__(self, parameter1,parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        #self.number = 1

    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "bin function: para1: " + str(self.parameter1) + " para2: " + str(self.parameter2)

class tempMissingValue(SimpleStatement):
    def __init__(self):
        pass
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "missing action"

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

class neq2_test(SimpleStatement):
    def __init__(self, name, newValue, parameter3):
        self.name = name
        self.newValue = newValue
        self.parameter3 = parameter3
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "testing"

class subValue(SimpleStatement):
    def __init__(self, parameter1, parameter2, parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "Sets parameter 1 to the value of parameter 2 minus parameter 3"

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

class LoopClosed(SimpleStatement):
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "closed loop"

class valueCompare(SimpleStatement):
    def __init__(self, parameter1, parameter2, parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3

    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "parameter1: " + str(self.parameter1) + " parameter2: " + str(self.parameter2) + " parameter3: " + str(self.parameter3)

class RunFunction(SimpleStatement):
    def __init__(self, result, argument, function):
        self.result = result
        self.argument = argument
        self.function = function
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "run a function in an other file"
    
class ReturnFunction(SimpleStatement):
    def __init__(self, parameter1):
       self.parameter1 = parameter1
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "return a variable after running a function"

class ReturnIFFunction(SimpleStatement):
    def __init__(self, parameter1,parameter2,parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "return parameter3 from a function if parameter1 is equal to parameter2"

def witchProgram(token):
    if isinstance(token, Directory):
        #print("loop")
        #code.addStatement(LoopOpen())
        print(token.isInALoop)
        print("test")
        #newrest, block = parseCodeBlock2(rest, CodeBlock(nest=token.isInALoop))
        #code.addStatement(Loop(block, token.varname))
        #return newrest, code
        #block.addStatement(LoopClosed())
        #code.addStatement(LoopClosed())
        #block.addStatement(LoopClosed())
        #return parseCodeBlock(newrest, code)
        #return newrest, code
        #print("test")
        #newrest, block = parseCodeBlock(rest, CodeBlock(nest=code.nestlevel + 1))
        #return parseCodeBlock(newrest, code.addStatement(Loop(block, token.varname)))

    if isinstance(token, DAT):
        #print("dat")
        if isinstance(token, add):
            return addValue(token.parameter1, token.parameter2, token.parameter3)
        if isinstance(token, ric):
            return displayValue(token.parameter1)#temp moet nog functie aan hangen die goed overeenkomt met standaard
        if isinstance(token, les):
            return valueCompare(token.parameter1, token.parameter2, token.parameter3)
        if (isinstance(token, dsi) or isinstance(token, dic)):
            return displayValue(token.parameter1)
        if isinstance(token, set):
            return setValue(token.parameter1, token.parameter2)
        if isinstance(token, neq) or isinstance(token, equ) or isinstance(token, sub_):
            return neq2_test(token.parameter1, token.parameter2, token.parameter3)
        
        
    elif isinstance(token, TXT):
        #print("txt")
        return displayValue(token.name)
    elif isinstance(token, BIN):
        return tempBinFunction(token.parameter1,token.parameter2)
    elif isinstance(token, ZIP):
        return tempMissingValue()
    elif isinstance(token, EXE):
        return tempMissingValue()
    elif isinstance(token, DLL):
        return tempMissingValue()
    elif isinstance(token, CSV):
        #print("csv")
        if isinstance(token,div):
            return deleteVar(token.name)
        elif isinstance(token,dfv): 
            return displayValue(token.parameter1)
        else: 
            print("adding: ", token.name)
            return createVar(token.name) 
    else: 
        print("things")
        #if len(rest) > 0:
        #    if rest[0] is not None:
        #        print(len(rest))
        #        if code.nestlevel > rest[0].isInALoop:
        #            return rest,code
        #print("else")
        return None


# parseCodeBlock :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parseCodeBlock2(tokens: List[Token], code: CodeBlock) -> Tuple[List[Token], CodeBlock]:
    #print(code)
    #if tokens == None or len(tokens) == 0:
    #    print("end")
    #    return None, code
    #token, *rest = tokens
    #print(token)
    #print(token.isInALoop)
    #if isinstance(token, Directory):
    #    newrest, block = parseCodeBlock(rest, CodeBlock(nest=token.isInALoop))
    #    code.addStatement(Loop(block, token.varname))
    #    return parseCodeBlock(newrest, code)
    # return witchProgram(token)
    if tokens == None or len(tokens) == 0:
        print("end")
        return None, code

    elif tokens[0].isInALoop - tokens[1].isInALoop:
        pass

    else:
        #code.addStatement(witchProgram(tokens[0]))
        return parseCodeBlock2(tokens[1:],code )



# parseCodeBlock :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parseCodeBlock(tokens: List[Token], code: CodeBlock) -> Tuple[List[Token], CodeBlock]:
    #print(code)
    if tokens == None or len(tokens) == 0:
        print("end")
        return None, code
    token, *rest = tokens
    print(token)
    print(token.isInALoop)
    if isinstance(token, Directory):
        print(token.isInALoop)
        print("test")
        newrest, block = parseCodeBlock(rest, CodeBlock(nest=token.isInALoop))
        code.addStatement(Loop(block, token.varname))
        #rest = newrest
        #if (newrest[0].isInALoop) - (token.isInALoop) < -1:
        #    return rest,code
        return parseCodeBlock(newrest, code)
        #return parseCodeBlock(newrest, code)

    if isinstance(token, DAT):
        #print("dat")
        if isinstance(token, add):
            code.addStatement(addValue(token.parameter1, token.parameter2, token.parameter3))
        elif isinstance(token, ric):
            code.addStatement(displayValue(token.parameter1))#temp moet nog functie aan hangen die goed overeenkomt met standaard
        elif isinstance(token, les):
            code.addStatement(valueCompare(token.parameter1, token.parameter2, token.parameter3))
        elif (isinstance(token, dsi) or isinstance(token, dic)):
            code.addStatement(displayValue(token.parameter1))
        elif isinstance(token, set):
            code.addStatement(setValue(token.parameter1, token.parameter2))
        elif isinstance(token, sub_):
            code.addStatement(subValue(token.parameter1, token.parameter2, token.parameter3))
        elif isinstance(token, neq) or isinstance(token, equ):
            code.addStatement(neq2_test(token.parameter1, token.parameter2, token.parameter3))
    elif isinstance(token, TXT):
        #print("txt")
        code.addStatement(displayValue(token.name))
    elif isinstance(token, BIN):
        #print("bin")
        #return rest, code
        code.addStatement(tempBinFunction(token.parameter1,token.parameter2))
    elif isinstance(token, ZIP):
        code.addStatement(tempMissingValue())
    elif isinstance(token, EXE):
        code.addStatement(tempMissingValue())
    elif isinstance(token, DLL):
        code.addStatement(tempMissingValue())
    elif isinstance(token, CSV):
        #print("csv")
        if isinstance(token,div):
            code.addStatement(deleteVar(token.name))
        elif isinstance(token,dfv): 
            code.addStatement(displayValue(token.parameter1))
        else: 
            print("adding: ", token.name)
            code.addStatement(createVar(token.name))
    elif isinstance(token, LNK):
        if isinstance(token,run):
            code.addStatement(RunFunction(token.result,token.argument,token.function))
        if isinstance(token,rtn):
            code.addStatement(ReturnFunction(token.parameter1))
        if isinstance(token,ifrtn):
            code.addStatement(ReturnIFFunction(token.parameter1,token.parameter2,token.parameter3))
    print("things")
    
    if len(tokens) >= 2:
        print("(rest[0].isInALoop) - (token.isInALoop): ",((rest[0].isInALoop) - (token.isInALoop)))
        print("token.isInALoop: ",token.isInALoop)
        print("tokens[0].isInALoop: ",rest[0].isInALoop)
        if (rest[0].isInALoop) - (token.isInALoop) < 0:
            return rest,code
    return parseCodeBlock(rest, code)   
        