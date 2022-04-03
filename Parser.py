#from ast import operator
#from re import L
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
    def __init__(self, block, varname, whileZero: bool, loopAtLeastOnce : bool, onlyOneTime : bool):
        self.block = block
        self.varname = varname
        self.whileZero = whileZero
        self.loopAtLeastOnce = loopAtLeastOnce
        self.onlyOneTime = onlyOneTime

    #__repr__ :: Loop -> String
    def __repr__(self) -> str:
        s = self.block.__repr__()
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
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "Existing var with name: " + str(self.parameter1) + " has new value: " + str(self.parameter2)

class DisplayOptions(Enum):
    INT = "INT"
    CHAR = "CHAR"
    STRING = "STRING"
    NEWLINE = "NEWLINE"
    NONEWLINE = "NONEWLINE"


class displayValue(SimpleStatement):
    def __init__(self, value : int, isChar: bool):
        self.value = value
        self.isChar = isChar
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        if self.isChar == True:
            return "Display the char: " + chr((self.value))
        else:
            return "Display the value: " + str(self.value)

class addValue(SimpleStatement):
    def __init__(self, parameter1, parameter2, parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " and " + str(self.parameter3)

class operatorsList(Enum):
    plus = 1
    minus = 2
    multiply = 3
    divide = 4
    modulo = 5
    andOp = 6
    orb = 7
    xor = 8
    xad = 9
    nad = 10
    nor = 11

class operators(SimpleStatement):
    def __init__(self, parameter1, parameter2, parameter3, operatorType: operatorsList ):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.operatorType = operatorType
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        match self.operatorType:
            case operatorsList.plus:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " plus " + str(self.parameter3)
            case operatorsList.minus:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " minus " + str(self.parameter3)
            case operatorsList.multiply:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " times " + str(self.parameter3)
            case operatorsList.divide:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " devided by " + str(self.parameter3)
            case operatorsList.modulo:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " modulo " + str(self.parameter3)
            case operatorsList.andOp:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise and " + str(self.parameter3)
            case operatorsList.orb:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise or " + str(self.parameter3)
            case operatorsList.xor:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise xor " + str(self.parameter3)
            case operatorsList.xad:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise xand " + str(self.parameter3)
            case operatorsList.nad:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise nand " + str(self.parameter3)
            case operatorsList.nor:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise nor " + str(self.parameter3)
            case _:
                return "Operator not supported or not found."

class valuePosConv(SimpleStatement):
    def __init__(self, parameter1, parameter2,toABS=True):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.toABS = toABS
    
    # __repr__ :: IncrementPointer -> String
    def __repr__(self) -> str:
        if self.toABS == True:
            return "parameter1: " + str(self.parameter1) + " wil have the absolute value of parameter 2: " + str(self.parameter2)
        else:
            return "parameter1: " + str(self.parameter1) + " wil have the negative value of parameter 2: " + str(self.parameter2)

class IfStatement(SimpleStatement):
    #__match_args__ = ('condition')
    def __init__(self, parameter1, parameter2, parameter3, condition):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.condition = condition
    # __repr__ :: IfStatement -> String
    def __repr__(self):
        return "IfStatement"
    
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

class NotImplemented(SimpleStatement):
    #def __init__(self):
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "function not implemented"
    
class ReturnFunction(SimpleStatement):
    def __init__(self, parameter1):
       self.parameter1 = parameter1
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "return a variable after running a function"

class MaxValue(SimpleStatement):
    def __init__(self, parameter1,parameter2,parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "Sets parameter1: " + str(self.parameter1) + " to the higher value out of parameter2: " + str(self.parameter2) + "and parameter3: " + str(self.parameter3)

class MinValue(SimpleStatement):
    def __init__(self, parameter1,parameter2,parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "Sets parameter1: " + str(self.parameter1) + " to the lower value out of parameter2: " + str(self.parameter2) + "and parameter3: " + str(self.parameter3)

class ReturnIFFunction(SimpleStatement):
    def __init__(self, parameter1,parameter2,parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: LoopOpen -> String
    def __repr__(self):
        return "return parameter3 from a function if parameter1 is equal to parameter2"


# parseCodeBlock :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parseCodeBlock(tokens: List[Token], code: CodeBlock) -> Tuple[List[Token], CodeBlock]:
    #print(code)
    if tokens == None or len(tokens) == 0:
        #print("end")
        return None, code
    token, *rest = tokens
    #print(token)
    #print(token.isInALoop)
    if isinstance(token, Directory):
        #print(token.isInALoop)
        newrest, block = parseCodeBlock(rest, CodeBlock(nest=token.isInALoop))
        if isinstance(token,fnc):
            code.addStatement(Loop(block, token.varname,False,True,True))
        elif isinstance(token,dif):
            code.addStatement(Loop(block, token.varname,False,False,True))
        elif isinstance(token,nif):
            code.addStatement(Loop(block, token.varname,True,False,True))
        elif isinstance(token,lpc):
            code.addStatement(Loop(block, token.varname,False,False,False))
        elif isinstance(token,lpn):
            code.addStatement(Loop(block, token.varname,True,False,False))
        elif isinstance(token,dlw):
            code.addStatement(Loop(block, token.varname,False,True,False))
        elif isinstance(token,dlu):
            code.addStatement(Loop(block, token.varname,True,True,False))
        return parseCodeBlock(newrest, code)
        
    if isinstance(token, DAT):
        if isinstance(token, abs):
            code.addStatement(valuePosConv(token.parameter1,token.parameter2, True))
        elif isinstance(token, neg):
            code.addStatement(valuePosConv(token.parameter1,token.parameter2, False))
        elif isinstance(token, add):
            #code.addStatement(addValue(token.parameter1, token.parameter2, token.parameter3))
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.plus))#maybe in other class not in same class ass bitwise
        elif isinstance(token, sub_):
            #code.addStatement(subValue(token.parameter1, token.parameter2, token.parameter3))
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.minus))#maybe in other class not in same class ass bitwise
        elif isinstance(token, mul):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.multiply))#maybe in other class not in same class ass bitwise
        elif isinstance(token, div):#check for interferance
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.divide))#maybe in other class not in same class ass bitwise
        elif isinstance(token, mod):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.modulo))#maybe in other class not in same class ass bitwise
        elif isinstance(token, and_):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.andOp))
        elif isinstance(token, orb):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.orb))
        elif isinstance(token, xor):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.xor))
        elif isinstance(token, xad):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.xad))
        elif isinstance(token, nad):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.nad))
        elif isinstance(token, nor):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.nor))
        elif isinstance(token, not_):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3,operatorsList.nor))
        elif isinstance(token, mor):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, ">"))
        elif isinstance(token, les):
            #code.addStatement(valueCompare(token.parameter1, token.parameter2, token.parameter3))
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, "<"))
        elif isinstance(token, equ):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, "=="))
        elif isinstance(token, neq):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, "!="))#maybe enum
        elif isinstance(token, get):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, ">="))
        elif isinstance(token, let):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, "<="))
        elif isinstance(token, rdi):
            code.addStatement(NotImplemented())
        elif isinstance(token, ric):
            code.addStatement(NotImplemented())
            #code.addStatement(displayValue(token.parameter1))#temp moet nog functie aan hangen die goed overeenkomt met standaard
        elif isinstance(token, dsi):
            code.addStatement(displayValue(token.parameter1, False))
        elif isinstance(token, dic):
            code.addStatement(displayValue(token.parameter1, True))
        elif isinstance(token, set):
            code.addStatement(setValue(token.parameter1, token.parameter2))
        elif isinstance(token, max):
            code.addStatement(MaxValue(token.parameter1,token.parameter2, token.parameter3))
        elif isinstance(token, min):
            code.addStatement(MinValue(token.parameter1,token.parameter2, token.parameter3))
    elif isinstance(token, TXT):
        if isinstance(token, rdc):
            code.addStatement(NotImplemented())
        elif isinstance(token, rds):
            code.addStatement(NotImplemented())
        elif isinstance(token, eof):
            code.addStatement(NotImplemented())
        elif isinstance(token, dsc):
            pass
        elif isinstance(token, dss):
            pass
        elif isinstance(token, dsl):
            pass
        elif isinstance(token, dec):
            pass
        elif isinstance(token, del_):
            pass
        elif isinstance(token, clr):
            pass
        elif isinstance(token, cat):
            pass
        elif isinstance(token, idx):
            pass
        elif isinstance(token, ids):
            pass
        elif isinstance(token, lid):
            pass
        elif isinstance(token, rep):
            pass
        elif isinstance(token, sub_):#check if correct class
            pass
        elif isinstance(token, rmv):
            pass
        elif isinstance(token, ins):
            pass
        elif isinstance(token, tou):
            pass
        elif isinstance(token, tol):
            pass
        
        
        code.addStatement(displayValue(token.name))
    elif isinstance(token, BIN):
        #print("bin")
        #return rest, code
        if isinstance(token, gte):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, ">="))
        else:
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
            #print("adding: ", token.name)
            code.addStatement(createVar(token.name))
    elif isinstance(token, LNK):
        if isinstance(token,run):
            code.addStatement(RunFunction(token.result,token.argument,token.function))
        if isinstance(token,rtn):
            code.addStatement(ReturnFunction(token.parameter1))
        if isinstance(token,ifrtn):
            code.addStatement(ReturnIFFunction(token.parameter1,token.parameter2,token.parameter3))
    #print("things")
    
    if len(tokens) >= 2:
        #print("(rest[0].isInALoop) - (token.isInALoop): ",((rest[0].isInALoop) - (token.isInALoop)))
        #print("token.isInALoop: ",token.isInALoop)
        #print("tokens[0].isInALoop: ",rest[0].isInALoop)
        if (rest[0].isInALoop) - (token.isInALoop) < 0:
            return rest,code
    return parseCodeBlock(rest, code)   
        