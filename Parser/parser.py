from lib2to3.pgen2.token import EQUAL, GREATER, GREATEREQUAL, LESS, LESSEQUAL, NOTEQUAL
from typing import List, Tuple
import copy#todo check if this lib is needed and if included in requirements.txt

from numpy import greater_equal, not_equal
from Lexer.tokens import *
from Lexer.lexer import *


class SimpleStatement:
    """statement that every statement is inherted
    """    
    def __init__(self):
        pass

#repeatStr :: String -> Integer -> String
def repeatStr(s : str, i : int):
    if (i <= 0):
        return ""
    return s + repeatStr(s, i - 1)

class CodeBlock:
    """Function that holds a code block of subsets of Dirst
    """    
    def __init__(self, nest : int =0):
        self.statements : list = []
        """Creates a empty list used for statements of Dist code"""        
        self.nestlevel : int = nest
        """Interger used to track how nested this block of Dirst code is"""   
        

    #addStatement :: CodeBlock -> SimpleStatement -> CodeBlock
    def addStatement(self, statement : SimpleStatement):
        """"Function used to add statement to the code block

        Args:
            statement (SimpleStatement): A statement that is inherted from simplestatement that you need to add

        Returns:
            CodeBlock: Returns itself(CodeBlock) after adding a statement
        """        
        self.statements.append(statement)
        return self
        
    #__repr__ :: CodeBlock -> String
    def __str__(self):
        return self.__repr__()

    #__repr__ :: CodeBlock -> String
    def __repr__(self) -> str:
        nstr = repeatStr("   ", self.nestlevel)
        statestr = ''.join(map(lambda st: nstr + str(st) + "\n", self.statements))
        return "Begin Block: \n" + statestr + repeatStr("   ", self.nestlevel - 1) + " End Block"

class DeclareFunction(SimpleStatement):
    """class that holds a function what is callable by the call syntax
        will run so long that the function is not returned
    """
    def __init__(self, block : CodeBlock, functionName : str, functionInputVar : str):
        self.block = block
        self.functionName = functionName
        self.functionInputVar = functionInputVar
    
    #__repr__ :: Function -> String
    def __repr__(self) -> str:
        s = "declare an function with name: " + self.functionName + " and input: " + self.functionInputVar + "\n" + "with code block: \n"
        s += self.block.__repr__()
        return s
        
class CallFunction(SimpleStatement):
    """class that holds a function call what is callable by the call syntax
    """
    def __init__(self, functionName : str, functionInputVar : str, functionReturnVar : str):
        self.functionName = functionName
        self.functionInputVar = functionInputVar
        self.functionReturnVar = functionReturnVar
        
    #__repr__ :: CallFunction -> String
    def __repr__(self) -> str:
        return "call function: " + self.functionName + " with input: " + self.functionInputVar + " and return var: " + self.functionReturnVar

class Loop(SimpleStatement):
    """a loop statement used to as the Directory subset of Dirst
    """    
    def __init__(self, block : CodeBlock, varname : str, whileZero: bool, loopAtLeastOnce : bool, onlyOneTime : bool):
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

    # __repr__ :: createVar -> String
    def __repr__(self) -> str:
        return "create var with name: " + str(self.name)

class deleteVar(SimpleStatement):
    """Class that is used for deleting a certain variable from memory and set the register to zero
    """    
    def __init__(self, name: str):
        """Name of the variable that needs deleting"""   
        self.name = name

    # __repr__ :: deleteVar -> String
    def __repr__(self) -> str:
        return "delete var with name: " + str(self.name)

class setValue(SimpleStatement):
    """Class that is used to set a variable to a value of to a value of a other variable.
    """    
    def __init__(self, parameter1 : string, parameter2):
        """parameter 1 is a name of the variable and is used to get the correct spot in memory"""
        self.parameter1 = parameter1
        """can be a integer or a variable name"""
        self.parameter2 = parameter2
    
    # __repr__ :: setValue -> String
    def __repr__(self) -> str:
        return "Existing var with name: " + str(self.parameter1) + " has new value: " + str(self.parameter2)

class DisplayOptions(Enum):
    """Enum of all the display options that displaying can have used by the 'displayValue' class"""    
    INT = "INT"
    CHAR = "CHAR"
    STRING = "STRING"
    NEWLINE = "NEWLINE"
    NONEWLINE = "NONEWLINE"


class displayValue(SimpleStatement):
    """class used to display string or integer from an variable to the console."""    
    def __init__(self, nameVar : int, newLine: bool):
        
        """the name of the variable that needs to be displayed"""
        self.nameVar = nameVar
        
        """ if True it will display a new line after the value is displayed"""
        self.newLine = newLine
        
    # __repr__ :: displayValue -> String
    def __repr__(self) -> str:
        if self.newLine == True:
            return "Display the string or integer of the var with the name: " + self.name + " with a new line"
        else:
            return "Display the string or integer of the var with the name: " + self.name 

class roundValue(SimpleStatement):
    """Class that is used to round a variable to ceiling or floor.
    """    
    def __init__(self, parameter1 : string, parameter2, roundToCeiling : bool):
        """parameter 1 is a name of the variable and is used to get the correct spot in memory"""
        self.parameter1 = parameter1
        """the value that needs to be rounded"""
        self.parameter2 = parameter2
        """Boolean if True it rounds to the ceiling if False it rounds to the floor"""
        self.roundToCeiling = roundToCeiling
    
    def __repr__(self) -> str:
        if self.roundToCeiling == True:
            return "Existing var with name: " + str(self.parameter1) + " will be rounded to the ceiling of: " + str(self.parameter2)
        else:
            return "Existing var with name: " + str(self.parameter1) + " will be rounded to the floor of: " + str(self.parameter2)
class operatorsList(Enum):
    """Enum used by the 'operators' class to give to correct operator
    """    
    plus = 1#add subset in Dirst
    minus = 2#sub subset in Dirst
    multiply = 3#mul subset in Dirst
    divide = 4#div subset in Dirst
    modulo = 5#mod subset in Dirst
    andOp = 6#and subset in Dirst
    orb = 7#orb subset in Dirst
    xor = 8#xor subset in Dirst
    xad = 9#xad subset in Dirst
    nad = 10#nad subset in Dirst
    nor = 11#nor subset in Dirst
    maxVal = 12#max in dat subset in Dirst
    minVal = 13#min in dat subset in Dirst

class operators(SimpleStatement):
    """Class used to calculate a value using the operators from operatorList
    """    
    def __init__(self, parameter1 : string, parameter2, parameter3, operatorType: operatorsList ):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.operatorType = operatorType
    
    # __repr__ :: operators -> String
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
            case operatorsList.maxVal:
                return "Sets parameter1: " + str(self.parameter1) + " to the higher value out of parameter2: " + str(self.parameter2) + " and parameter3: " + str(self.parameter3)
            case operatorsList.minVal:
                return "Sets parameter1: " + str(self.parameter1) + " to the lower value out of parameter2: " + str(self.parameter2) + " and parameter3: " + str(self.parameter3)
            case _:
                return "Operator not supported or not found."

class valuePosConv(SimpleStatement):
    def __init__(self, parameter1 : string, parameter2,toABS: bool =True):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.toABS  = toABS
    
    # __repr__ :: valuePosConv -> String
    def __repr__(self) -> str:
        if self.toABS == True:
            return "parameter1: " + str(self.parameter1) + " wil have the absolute value of parameter 2: " + str(self.parameter2)
        else:
            return "parameter1: " + str(self.parameter1) + " wil have the negative value of parameter 2: " + str(self.parameter2)


class IfStatementsList(Enum):#enum class not working in match statement? so now it is half inplemented
    """All if statement operators that can be used by the 'IfStatement' class
    """    
    GREATER = '>'
    LESS = '<'
    EQUAL = '=='
    NOTEQUAL = '!='
    GREATEREQUAL = '>='
    LESSEQUAL = '<='

class IfStatement(SimpleStatement):
    """Class used for if statements with a operator from enum: 'ifStatementList'
    """    
    def __init__(self, parameter1 : string, parameter2, parameter3, condition : IfStatementsList):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.condition : IfStatementsList = condition

    # __repr__ :: IfStatement -> String
    def __repr__(self):
        return "IfStatement: " + str(self.parameter1) + " will have the value of -1 if: " + str(self.parameter2) + str(self.condition) + str(self.parameter3) + " otherwise has the value of: 0"

class RunFunction(SimpleStatement):
    def __init__(self, result : str, argument, function : str):
        self.result = result
        self.argument = argument
        self.function = function
    
    # __repr__ :: RunFunction -> String
    def __repr__(self):
        return "run a function in an other file"

class NotImplemented(SimpleStatement):
    #def __init__(self):
    
    # __repr__ :: NotImplemented -> String
    def __repr__(self):
        return "function not implemented"
    
class ReturnFunction(SimpleStatement):
    def __init__(self, parameter1):
       self.parameter1 = parameter1
    
    # __repr__ :: ReturnFunction -> String
    def __repr__(self):
        return "return a variable after running a function"

class ReturnIFFunction(SimpleStatement):
    def __init__(self, parameter1: string, parameter2, parameter3):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
    
    # __repr__ :: ReturnIFFunction -> String
    def __repr__(self):
        return "Return parameter3 from a function if parameter1 is equal to parameter2"


#parseCodeBlock :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parseCodeBlock(tokens: List[Token], code: CodeBlock, functions: CodeBlock) -> Tuple[List[Token], CodeBlock, CodeBlock]:
    """Function used to parse a block of code to correct function to be used by the runner

    Args:
        tokens (List[Token]): list of tokens used to 
        code (CodeBlock): block of code

    Returns:
        Tuple[List[Token], CodeBlock]: the list of tokens and the block of code
    """
 #   print("test")

    
    if tokens == None or len(tokens) == 0:
        return None, code, functions
    token, *rest = tokens
    
    
    if isinstance(token, fnc) and code.nestlevel == 1 and token.isInALoop == 1:
        #an other function is declared, but not be added to the current function
        return tokens, code, functions
    
    if isinstance(token, Directory):
        newrest, block, functions_ = parseCodeBlock(rest, CodeBlock(nest=token.isInALoop), functions)
        if isinstance(token,fnc):
            functions_.addStatement(DeclareFunction(block, token.varname, token.functionInput))
        elif isinstance(token,dif_):
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
        return parseCodeBlock(newrest, code, functions_)
    
    if token.isInALoop is not code.nestlevel:
        return tokens, code, functions
      
    elif isinstance(token, DAT):
        if isinstance(token, abs):
            code.addStatement(valuePosConv(token.parameter1,token.parameter2, True))
        elif isinstance(token, neg):
            code.addStatement(valuePosConv(token.parameter1,token.parameter2, False))
        elif isinstance(token, add):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.plus))#maybe in other class not in same class ass bitwise
        elif isinstance(token, sub_):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.minus))#maybe in other class not in same class ass bitwise
        elif isinstance(token, mul):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.multiply))#maybe in other class not in same class ass bitwise
        elif isinstance(token, div):#check for interferance
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.divide))#maybe in other class not in same class ass bitwise
        elif isinstance(token, mod):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.modulo))#maybe in other class not in same class ass bitwise
        elif isinstance(token, and_):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.andOp))
        elif isinstance(token, orb):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.orb))
        elif isinstance(token, xor):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.xor))
        elif isinstance(token, xad):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.xad))
        elif isinstance(token, nad):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.nad))
        elif isinstance(token, nor):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.nor))
        elif isinstance(token, not_):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.nor))
        elif isinstance(token, mor):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.GREATER))
        elif isinstance(token, les):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.LESS))
        elif isinstance(token, equ):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.EQUAL))
        elif isinstance(token, neq):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.NOTEQUAL))
        elif isinstance(token, get):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.GREATEREQUAL))
        elif isinstance(token, let):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.LESSEQUAL))
        elif isinstance(token, rdi):
            code.addStatement(setValue(token.name, token.consoleInput))
        elif isinstance(token, ric):
            code.addStatement(setValue(token.name, token.consoleInput))#set to -1 if eof not implemented
        elif isinstance(token, dsi):
            code.addStatement(displayValue(token.name, False))
        elif isinstance(token, dic):
            code.addStatement(displayValue(token.name, False))
            # code.addStatement(displayValue(token.name))
        elif isinstance(token, set):
            code.addStatement(setValue(token.parameter1, token.parameter2))
        elif isinstance(token, max_):
            code.addStatement(operators(token.parameter1,token.parameter2, token.parameter3, operatorsList.maxVal))
        elif isinstance(token, min_):
            code.addStatement(operators(token.parameter1,token.parameter2, token.parameter3, operatorsList.minVal))
    elif isinstance(token, TXT):
        if isinstance(token, rdc):
            code.addStatement(NotImplemented())
        elif isinstance(token, rds):#no input from console beacause of functional programming is that not allowed
            code.addStatement(setValue(token.name, token.consoleInput))
        elif isinstance(token, eof):
            code.addStatement(NotImplemented())
        elif isinstance(token, dsc):
            #code.addStatement(displayValue(token.name, True))#implent now good according to spec @todo
            code.addStatement(NotImplemented())
        elif isinstance(token, dss):
            code.addStatement(displayValue(token.name, False))#implent
        elif isinstance(token, dsl):
            code.addStatement(displayValue(token.name, True))
        elif isinstance(token, dec):
            code.addStatement(NotImplemented())
        elif isinstance(token, des):
            code.addStatement(displayValue(token.name, False))
        elif isinstance(token, del_):
            code.addStatement(displayValue(token.name, True))
        elif isinstance(token, clr):
            code.addStatement(deleteVar(token.name))# verang door var op 0 te zetten of nullptr
        elif isinstance(token, cat):
            code.addStatement(NotImplemented())
        elif isinstance(token, idx):
            code.addStatement(NotImplemented())
        elif isinstance(token, ids):
            code.addStatement(NotImplemented())
        elif isinstance(token, lid):
            code.addStatement(NotImplemented())
        elif isinstance(token, rep):
            code.addStatement(NotImplemented())
        elif isinstance(token, sub):#check if correct class
            code.addStatement(NotImplemented())
        elif isinstance(token, rmv):
            code.addStatement(NotImplemented())
        elif isinstance(token, ins):
            code.addStatement(NotImplemented())
        elif isinstance(token, tou):
            code.addStatement(NotImplemented())
        elif isinstance(token, tol):
            code.addStatement(NotImplemented())
        elif isinstance(token, pdl):
            code.addStatement(NotImplemented())
        elif isinstance(token, cpl):
            code.addStatement(NotImplemented())
        elif isinstance(token, pdr):
            code.addStatement(NotImplemented())
        elif isinstance(token, cpr):
            code.addStatement(NotImplemented())
        elif isinstance(token, sam):
            code.addStatement(NotImplemented())
        elif isinstance(token, dif):#check if correct dif class also in lexer
            code.addStatement(NotImplemented())
        elif isinstance(token, hiv):
            code.addStatement(NotImplemented())
        elif isinstance(token, lov):
            code.addStatement(NotImplemented())
        elif isinstance(token, hev):
            code.addStatement(NotImplemented())
        elif isinstance(token, lev):
            code.addStatement(NotImplemented())
        elif isinstance(token, ssw):
            code.addStatement(NotImplemented())
        elif isinstance(token, sew):
            code.addStatement(NotImplemented())
        elif isinstance(token, trm):
            code.addStatement(NotImplemented())
        elif isinstance(token, tms):
            code.addStatement(NotImplemented())
        elif isinstance(token, tme):
            code.addStatement(NotImplemented())
        elif isinstance(token, ses):
            code.addStatement(NotImplemented())
        
        #code.addStatement(displayValue(token.name))
    elif isinstance(token, BIN):
        if isinstance(token, pls):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.plus))
        elif isinstance(token, mns):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.minus))
        elif isinstance(token, tms):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.multiply))
        elif isinstance(token, dvb):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.divide))
        elif isinstance(token, pwr):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.power))
        elif isinstance(token, sgn):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.sign))#parameter 3 niet nodig kijk of error geeft
        elif isinstance(token, sqr):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.square))
        elif isinstance(token, sin):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.sin))
        elif isinstance(token, cos):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.cos))
        elif isinstance(token, tan):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.tan))
        elif isinstance(token, snh):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.sinh))
        elif isinstance(token, csh):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.cosh))
        elif isinstance(token, tnh):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.tanh))
        elif isinstance(token, cil):
            code.addStatement(roundValue(token.parameter1, token.parameter2, True))
        elif isinstance(token, flr):
            code.addStatement(roundValue(token.parameter1, token.parameter2, False))
        elif isinstance(token, log):
            code.addStatement(NotImplemented())
        elif isinstance(token, lge):
            code.addStatement(NotImplemented())
        elif isinstance(token, lbq):
            code.addStatement(NotImplemented())
        elif isinstance(token, epw):
            code.addStatement(NotImplemented())
        elif isinstance(token, avl):
            code.addStatement(NotImplemented())
        elif isinstance(token, rnd):
            code.addStatement(NotImplemented())
        elif isinstance(token, rou):
            code.addStatement(NotImplemented())
        elif isinstance(token, asn):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.sini))
        elif isinstance(token, acs):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.cosi))
        elif isinstance(token, atn):
            code.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsList.tani))
        elif isinstance(token, mks):
            code.addStatement(setValue(token.parameter1, token.parameter2))#check if good?
        elif isinstance(token, fmx):
            code.addStatement(NotImplemented())
        elif isinstance(token, fmn):
            code.addStatement(NotImplemented())
        elif isinstance(token, grt):
            code.addStatement(NotImplemented())
        elif isinstance(token, lst):
            code.addStatement(NotImplemented())
        elif isinstance(token, eqt):
            code.addStatement(NotImplemented())
        elif isinstance(token, net):
            code.addStatement(NotImplemented())
        elif isinstance(token, gte):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.GREATEREQUAL))
        elif isinstance(token, lte):
            code.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementsList.LESS))
        elif isinstance(token, rfv):
            code.addStatement(NotImplemented())
        elif isinstance(token, dfv):
            code.addStatement(NotImplemented())
        #else: #properly not needed
        #    code.addStatement(NotImplemented())
        
    elif isinstance(token, ZIP):
        if isinstance(token, giv):
            code.addStatement(NotImplemented())
        elif isinstance(token, siv):
            code.addStatement(NotImplemented())
        elif isinstance(token, gsv):
            code.addStatement(NotImplemented())
        elif isinstance(token, siv):
            code.addStatement(NotImplemented())
        elif isinstance(token, gfv):
            code.addStatement(NotImplemented())
        elif isinstance(token, sfv):
            code.addStatement(NotImplemented())
        elif isinstance(token, fia):
            code.addStatement(NotImplemented())
        elif isinstance(token, zia):
            code.addStatement(NotImplemented())
        elif isinstance(token, fsa):
            code.addStatement(NotImplemented())
        elif isinstance(token, zsa):
            code.addStatement(NotImplemented())
        elif isinstance(token, ffa):
            code.addStatement(NotImplemented())
        elif isinstance(token, zfa):
            code.addStatement(NotImplemented())
        #code.addStatement(NotImplemented())
    elif isinstance(token, EXE):
        if isinstance(token, sia):
            code.addStatement(NotImplemented())
        elif isinstance(token, ssa):
            code.addStatement(NotImplemented())
        elif isinstance(token, sti):
            code.addStatement(NotImplemented())
        elif isinstance(token, stf):
            code.addStatement(NotImplemented())
        elif isinstance(token, stc):
            code.addStatement(NotImplemented())
        elif isinstance(token, its):
            code.addStatement(NotImplemented())
        elif isinstance(token, itf):
            code.addStatement(NotImplemented())
        elif isinstance(token, ias):
            code.addStatement(NotImplemented())
        elif isinstance(token, aif):
            code.addStatement(NotImplemented())
        elif isinstance(token, fts):
            code.addStatement(NotImplemented())
        elif isinstance(token, fti):
            code.addStatement(NotImplemented())
        elif isinstance(token, afi):
            code.addStatement(NotImplemented())
        #code.addStatement(NotImplemented())
    elif isinstance(token, DLL):
        if isinstance(token, psh):
            code.addStatement(NotImplemented())
        elif isinstance(token, pop):
            code.addStatement(NotImplemented())
        elif isinstance(token, spk):
            code.addStatement(NotImplemented())
        elif isinstance(token, ssz):
            code.addStatement(NotImplemented())
        elif isinstance(token, enq):
            code.addStatement(NotImplemented())
        elif isinstance(token, deq):
            code.addStatement(NotImplemented())
        elif isinstance(token, qpk):
            code.addStatement(NotImplemented())
        elif isinstance(token, qsz):
            code.addStatement(NotImplemented())
        elif isinstance(token, tpl):
            code.addStatement(NotImplemented())
        elif isinstance(token, tpr):
            code.addStatement(NotImplemented())
        elif isinstance(token, tsv):
            code.addStatement(NotImplemented())
        elif isinstance(token, tgv):
            code.addStatement(NotImplemented())
        elif isinstance(token, gbe):
            code.addStatement(NotImplemented())
        elif isinstance(token, gen):
            code.addStatement(NotImplemented())
        elif isinstance(token, gef):
            code.addStatement(NotImplemented())
        elif isinstance(token, lce):
            code.addStatement(NotImplemented())
        elif isinstance(token, lcn):
            code.addStatement(NotImplemented())
        elif isinstance(token, lcf):
            code.addStatement(NotImplemented())
        elif isinstance(token, ges):
            code.addStatement(NotImplemented())
        elif isinstance(token, ces):
            code.addStatement(NotImplemented())
        #code.addStatement(NotImplemented())
    elif isinstance(token, CSV):
        if isinstance(token, cia):
            code.addStatement(NotImplemented())
        elif isinstance(token, civ):
            code.addStatement(createVar(token.name))
        elif isinstance(token, csa):
            code.addStatement(NotImplemented())
        elif isinstance(token, csv):
            code.addStatement(createVar(token.name))#string and var now no differrence dont know if a problem
        elif isinstance(token, cfa):
            code.addStatement(NotImplemented())
        elif isinstance(token, cfv):
            code.addStatement(createVar(token.name))#float and var now no differrence dont know if a problem
        elif isinstance(token, dia):
            code.addStatement(NotImplemented())
        elif isinstance(token, div):
            code.addStatement(deleteVar(token.name))
        elif isinstance(token, dsa):
            code.addStatement(NotImplemented())
        elif isinstance(token, dsv):
            code.addStatement(deleteVar(token.name))
        elif isinstance(token, dfa):
            code.addStatement(NotImplemented())
        elif isinstance(token, dfv): 
            code.addStatement(deleteVar(token.name))
            #code.addStatement(displayValue(token.parameter1, False))?????
        #else: 
        #    code.addStatement(createVar(token.name))
    elif isinstance(token, LNK):
        if isinstance(token, run):
            code.addStatement(CallFunction(token.functionName, token.parameterVar, token.returnVar))
        elif isinstance(token,rtn):
            code.addStatement(ReturnFunction(token.parameter1))    
    if len(tokens) >= 2:#needed because if loop closes 2 times it will not correctly work because it will not close the loop 2 times
        if (rest[0].isInALoop) - (token.isInALoop) < 0:
            return rest, code, functions
    return parseCodeBlock(rest, code, functions)