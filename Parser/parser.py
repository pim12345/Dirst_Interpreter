from lib2to3.pgen2.token import EQUAL, GREATER, GREATEREQUAL, LESS, LESSEQUAL, NOTEQUAL
from typing import List, Tuple
import copy#todo check if this lib is needed and if included in requirements.txt

from numpy import greater_equal, not_equal
from Lexer.tokens import *
from Lexer.lexer import *


class SimpleStatement:
    """statement that every statement is inherited
    """    
    def __init__(self, instructionType: Instruction_Variable_Type):
        self.instructionType = instructionType
        #pass

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
        self.nestLevel : int = nest
        """Integer used to track how nested this block of Dirst code is"""   

    #addStatement :: CodeBlock -> SimpleStatement -> CodeBlock
    def addStatement(self, statement : SimpleStatement):
        """"Function used to add statement to the code block

        Args:
            statement (SimpleStatement): A statement that is inherited from simpleStatement that you need to add

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
        nStr = repeatStr("   ", self.nestLevel)
        stateStr = ''.join(map(lambda st: nStr + str(st) + "\n", self.statements))
        return "Begin Block: \n" + stateStr + repeatStr("   ", self.nestLevel - 1) + " End Block"

class DeclareFunction(SimpleStatement):
    """class that holds a function what is callable by the call syntax
        will run so long that the function is not returned
    """
    def __init__(self, block : CodeBlock, functionName : str, functionInputVar : str):
        self.block = block
        self.functionName = functionName
        self.functionInputVar = functionInputVar
        super().__init__(Instruction_Variable_Type.Function)#not used, but because of inheritance it is needed
    
    #__repr__ :: DeclareFunction -> String
    def __repr__(self) -> str:
        s = "Declare an function with name: " + self.functionName + " and input: " + self.functionInputVar + "\n" + "with code block: \n"
        return s + self.block.__repr__()
        
class CallFunction(SimpleStatement):
    """class that holds a function call what is callable by the call syntax
    """
    def __init__(self, functionName : str, functionInputVar : str, functionReturnVar : str):
        self.functionName = functionName
        self.functionInputVar = functionInputVar
        self.functionReturnVar = functionReturnVar
        super().__init__(Instruction_Variable_Type.Function)#not used, but because of inheritance it is needed
        
    #__repr__ :: CallFunction -> String
    def __repr__(self) -> str:
        return "call function: " + self.functionName + " with input: " + self.functionInputVar + " and return var: " + self.functionReturnVar

class Loop(SimpleStatement):
    """a loop statement used to as the Directory subset of Dirst
    """    
    def __init__(self, block : CodeBlock, varConditionName : str, whileZero: bool, loopAtLeastOnce : bool, onlyOneTime : bool):
        self.block = block     
        self.varConditionName = varConditionName
        self.whileZero = whileZero
        self.loopAtLeastOnce = loopAtLeastOnce
        self.onlyOneTime = onlyOneTime
        super().__init__(Instruction_Variable_Type.Function)#not used, but because of inheritance it is needed

    #__repr__ :: Loop -> String
    def __repr__(self) -> str:
        s = self.block.__repr__()
        return s

class createVar(SimpleStatement):
    def __init__(self, name: str, instructionType: Instruction_Variable_Type):
        self.name = name
        super().__init__(instructionType)

    # __repr__ :: createVar -> String
    def __repr__(self) -> str:
        return "create var with name: " + str(self.name) + "with type: " + super().instructionType

class deleteVar(SimpleStatement):
    """Class that is used for deleting a certain variable from memory and set the register to zero
    """    
    def __init__(self, name: str, instructionType: Instruction_Variable_Type):
        """Name of the variable that needs deleting"""   
        self.name = name
        super().__init__(instructionType)

    # __repr__ :: deleteVar -> String
    def __repr__(self) -> str:
        return "delete var with name: " + str(self.name) + "with type: " + super().instructionType

class setValue(SimpleStatement):
    """Class that is used to set a variable to a value of to a value of a other variable.
    """    
    def __init__(self, parameter1 : str, parameter2: str, instructionType: Instruction_Variable_Type):
        """parameter 1 is a name of the variable and is used to get the correct spot in memory"""
        self.parameter1 = parameter1
        """can be a integer or a variable name"""
        self.parameter2 = parameter2
        super().__init__(instructionType)
    
    # __repr__ :: setValue -> String
    def __repr__(self) -> str:
        return "Existing var with name: " + str(self.parameter1) + " has new value: " + str(self.parameter2) + "with type: " + super().instructionType

class DisplayOptions(Enum):
    """Enum of all the display options that displaying can have used by the 'displayValue' class"""    
    INT = "INT"
    CHAR = "CHAR"
    STRING = "STRING"
    NEWLINE = "NEWLINE"
    NONEWLINE = "NONEWLINE"


class displayValue(SimpleStatement):
    """class used to display string or integer from an variable to the console."""    
    def __init__(self, nameVar : int, newLine: bool, instructionType: Instruction_Variable_Type):
        
        """the name of the variable that needs to be displayed"""
        self.nameVar = nameVar
        
        """ if True it will display a new line after the value is displayed"""
        self.newLine = newLine
        
        super().__init__(instructionType)
        
    # __repr__ :: displayValue -> String
    def __repr__(self) -> str:
        if self.newLine == True:
            return "Display the string or integer of the var with the name: " + self.name + " with a new line" + " with type: " + super().instructionType
        else:
            return "Display the string or integer of the var with the name: " + self.name + " without a new line" + " with type: " + super().instructionType


class roundValue(SimpleStatement):
    """Class that is used to round a variable to ceiling or floor.
    """    
    def __init__(self, parameter1 : str, parameter2, roundToCeiling : bool):
        """parameter 1 is a name of the variable and is used to get the correct spot in memory"""
        self.parameter1 = parameter1
        """the value that needs to be rounded"""
        self.parameter2 = parameter2
        """Boolean if True it rounds to the ceiling if False it rounds to the floor"""
        self.roundToCeiling = roundToCeiling
        super().__init__(Instruction_Variable_Type.Float)#because the function accepts floats
    
    # __repr__ :: roundValue -> String
    def __repr__(self) -> str:
        if self.roundToCeiling == True:
            return "Existing var with name: " + str(self.parameter1) + " will be rounded to the ceiling of: " + str(self.parameter2)
        else:
            return "Existing var with name: " + str(self.parameter1) + " will be rounded to the floor of: " + str(self.parameter2)
        
class operatorsType(Enum):
    """Enum used by the 'operators' class to give to correct operator
       operator can be used in the integer subset or the float subset of Dirst, 
       With type is used is determined by the instructionType of the 'operators' class
    """    
    plus = 1#add of the DAT subset in Dirst
    minus = 2#sub of the DAT subset in Dirst
    multiply = 3#mul of the DAT subset in Dirst
    divide = 4#div of the DAT subset in Dirst
    modulo = 5#mod of the DAT subset in Dirst
    andOp = 6#and of the DAT subset in Dirst
    orb = 7#orb of the DAT subset in Dirst
    xor = 8#xor of the DAT subset in Dirst
    xad = 9#xad of the DAT subset in Dirst
    nad = 10#nad of the DAT subset in Dirst
    nor = 11#nor of the DAT subset in Dirst
    maxVal = 12#max in DAT subset in Dirst
    minVal = 13#min in DAT subset in Dirst

class operators(SimpleStatement):
    """Class used to calculate a value using the operators from operatorList
    """    
    def __init__(self, parameter1 : str, parameter2: str, parameter3: str, operatorType: operatorsType, instructionType: Instruction_Variable_Type ):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.operatorType = operatorType
        super().__init__(instructionType)
    
    # __repr__ :: operators -> String
    def __repr__(self) -> str:
        match self.operatorType:
            case operatorsType.plus:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " plus " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.minus:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " minus " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.multiply:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " times " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.divide:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " divided by " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.modulo:
                return "parameter1: " + str(self.parameter1) + " has the value of: " + str(self.parameter2) + " modulo " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.andOp:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise and " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.orb:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise or " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.xor:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise xor " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.xad:
                return "parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise xand " + str(self.parameter3) + " with instruction type: " + super().instructionType #https://deepai.org/machine-learning-glossary-and-terms/xand
            case operatorsType.nad:
                return "parameter1: " + str(self.parameter1) + " to the value of the bitwise not of: " + str(self.parameter2) +" with instruction type: " + super().instructionType
            case operatorsType.nor:
                return "Sets parameter1: " + str(self.parameter1) + " has the value bitwise value of: " + str(self.parameter2) + " bitwise nor " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.maxVal:
                return "Sets parameter1: " + str(self.parameter1) + " to the higher value out of parameter2: " + str(self.parameter2) + " and parameter3: " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case operatorsType.minVal:
                return "Sets parameter1: " + str(self.parameter1) + " to the lower value out of parameter2: " + str(self.parameter2) + " and parameter3: " + str(self.parameter3) + " with instruction type: " + super().instructionType
            case _:
                return "Operator not supported or not found."

class MathFloatType(Enum):
    #all these are math functions. instructions only used in the float subset of Dirst(bin subset)
    power = 1#pwr in bin subset in Dirst
    sign = 2#sgn in bin subset in Dirst
    squareRoot = 3#sqr in bin subset in Dirst
    sin = 4#sin in bin subset in Dirst
    cos = 5#cos in bin subset in Dirst
    tan = 6#tan in bin subset in Dirst
    hyperbolicSin = 7#snh in bin subset in Dirst
    hyperbolicCos = 8#csh in bin subset in Dirst
    hyperbolicTan = 9#tnh in bin subset in Dirst
    #roundCeiling = 10#cil in bin subset in Dirst
    #roundFloor = 11#flr in bin subset in Dirst
    logBase10 = 12#log in bin subset in Dirst
    logNatural =13#lge in bin subset in Dirst
    log = 14#lbq in bin subset in Dirst
    eToPower = 15#epw in bin subset in Dirst
    #absoluteValue = 16#avl in bin subset in Dirst
    
    inverseSin = 17#asn in bin subset in Dirst
    inverseCos = 18#acs in bin subset in Dirst
    inverseTan = 19#atn in bin subset in Dirst
    
class mathFloatFunctions(SimpleStatement):
    def __init__(self, parameter1 : str, parameter2: str, parameter3: str, mathFunctionType: MathFloatType):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.mathFunctionType = mathFunctionType
        super().__init__(Instruction_Variable_Type.Float)#because the math functions in dirst only use floats
    
    def __init__(self, parameter1 : str, parameter2: str, mathFunctionType: MathFloatType):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.mathFunctionType = mathFunctionType
        super().__init__(Instruction_Variable_Type.Float)#because the math functions in dirst only use floats
        
    # __repr__ :: mathFloatFunctions -> String
    def __repr__(self) -> str:
        match self.mathFunctionType:
            case MathFloatType.power:
                return "Set " + self.parameter1 + " to the value of " + self.parameter2 + " to the power of " + self.parameter3 
            case MathFloatType.sign:
                return "Set " + self.parameter1 + " to the value of the sign of " + self.parameter2
            case MathFloatType.squareRoot:
                return "Set " + self.parameter1 + " to the value of the square root of " + self.parameter2
            case MathFloatType.sin:
                return "Set " + self.parameter1 + " to the value of the sin of " + self.parameter2
            case MathFloatType.cos:
                return "Set " + self.parameter1 + " to the value of the cos of " + self.parameter2
            case MathFloatType.tan:
                return "Set " + self.parameter1 + " to the value of the tan of " + self.parameter2
            case MathFloatType.hyperbolicSin:
                return "Set " + self.parameter1 + " to the value of the hyperbolic sin of " + self.parameter2
            case MathFloatType.hyperbolicCos:
                return "Set " + self.parameter1 + " to the value of the hyperbolic cos of " + self.parameter2
            case MathFloatType.hyperbolicTan:
                return "Set " + self.parameter1 + " to the value of the hyperbolic tan of " + self.parameter2
            case MathFloatType.logBase10:
                return "Set " + self.parameter1 + " to the value of the log base 10 of " + self.parameter2
            case MathFloatType.logNatural:
                return "Set " + self.parameter1 + " to the value of the log natural of " + self.parameter2
            case MathFloatType.log:
                return "Set " + self.parameter1 + " to the value of the base  " + self.parameter3 + " logarithm of " + self.parameter2
            case MathFloatType.eToPower:
                return "Set " + self.parameter1 + " to the value of e to the power of " + self.parameter2
            #case MathFloatType.absoluteValue:
            #    return "Set " + self.parameter1 + " to the value of the absolute value of " + self.parameter2
            case MathFloatType.inverseSin:
                return "Set " + self.parameter1 + " to the value of the inverse sin of " + self.parameter2
            case MathFloatType.inverseCos:
                return "Set " + self.parameter1 + " to the value of the inverse cos of " + self.parameter2
            case MathFloatType.inverseTan:
                return "Set " + self.parameter1 + " to the value of the inverse tan of " + self.parameter2
            case _:
                return "Math function not supported or not found., math type: " + self.mathFunctionType


class stringOperatorsType(Enum):
    firstOccurrence = 1#idx in str subset in Dirst
    firstOccurrenceFromSpecifiedIndex = 2#ids in str subset in Dirst
    lastOccurrence = 3#lid in str subset in Dirst
    replaceEveryOccurrence = 4#rep in str subset in Dirst#will not be implemented
    
#todo make string operators

class ConvertType(Enum):
    absolute = "absolute",
    negative = "negative",
    bitWiseNot = "bitWiseNot",
    #upperCase = "upperCase",

class valueConv(SimpleStatement):
    def __init__(self, parameter1 : str, parameter2: str, convertType: ConvertType, instructionType: Instruction_Variable_Type):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.convertType  = convertType
        super().__init__(instructionType)
    
    # __repr__ :: valuePosConv -> String
    def __repr__(self) -> str:
        match self.convertType:
            case ConvertType.absolute:
                return "parameter1: " + str(self.parameter1) + " wil have the absolute value of parameter 2: " + str(self.parameter2) + " with instruction type: " + super().instructionType
            case ConvertType.negative:
                return "parameter1: " + str(self.parameter1) + " wil have the negative value of parameter 2: " + str(self.parameter2) + " with instruction type: " + super().instructionType
            case ConvertType.bitWiseNot:
                return "parameter1: " + str(self.parameter1) + " wil have the bitwise not value of parameter 2: " + str(self.parameter2) + " with instruction type: " + super().instructionType
            case _:
                return "Convert type not supported or not found."


class IfStatementType(Enum):#enum class not working in match statement? so now it is half implemented
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
    def __init__(self, parameter1 : str, parameter2: str, parameter3: str, condition : IfStatementType, instructionType: Instruction_Variable_Type):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.condition : IfStatementType = condition
        super().__init__(instructionType)

    # __repr__ :: IfStatement -> String
    def __repr__(self):
        return "IfStatement: " + str(self.parameter1) + " will have the value of -1 if: " + str(self.parameter2)+ " " + str(self.condition) + " " + str(self.parameter3) + " otherwise has the value of: 0" + " with instruction type: " + super().instructionType

class RunFunction(SimpleStatement):
    def __init__(self, result : str, argument: str, function : str, instructionType: Instruction_Variable_Type):
        self.result = result
        self.argument = argument
        self.function = function
        super.__init__(instructionType)
    
    # __repr__ :: RunFunction -> String
    def __repr__(self):
        return "run function " + self.function + " with argument " + self.argument + " and store the result in " + self.result + " result will be of type: " + super().instructionType

class TapeAction(Enum):
    MoveLeft = "Moves the tape left"
    MoveRight = "Moves the tape right"
    ReadCurrentElementPosition = "Sets the current element of the tape to the specified integer value "
    WriteElementToCurrentPosition = "Sets the specified integer variable to the value of the current element of the tape"
    
class Tape(SimpleStatement):
    def __init__(self, tapeAction : TapeAction):
        self.tapeAction = tapeAction
        super().__init__(Instruction_Variable_Type.Integer)#tape only supports integer values
        
    def __init__(self, parameter1: str, tapeAction : TapeAction):
        self.tapeAction = tapeAction
        self.parameter1 = parameter1
        super().__init__(Instruction_Variable_Type.Integer)#tape only supports integer values

    # __repr__ :: Tape -> String
    def __repr__(self) -> str:
        return "tape action: " + str(self.tapeAction) if hasattr(self, 'parameter1') == False else + " with parameter: " + str(self.parameter1)
    
class NotImplemented(SimpleStatement):
    def __init__(self, ignore : bool = False):
        super.__init__(Instruction_Variable_Type.Unknown)
        self.ignore = ignore
    
    # __repr__ :: NotImplemented -> String
    def __repr__(self):
        if self.ignore == False:
            return "function not implemented, will not be ignored and will create an error"#will be used for critical code what not yet is implemented
        else:
            return "function not implemented, this instruction will not be runned and will be ignored and will not create an error"#used for instructions like ces for errors what not is used in this interpreter
        
    
class ReturnFunction(SimpleStatement):
    def __init__(self, parameter1: str):
       self.parameter1 = parameter1
       super().__init__(Instruction_Variable_Type.Function)
    
    # __repr__ :: ReturnFunction -> String
    def __repr__(self):
        return "return this function with the value of variable: " + self.parameter1


class Stack(SimpleStatement):
    def __init__(self, parameter1: str, parameter2: str):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(Instruction_Variable_Type.Integer)
        
    # __repr__ :: Stack -> String
    def __repr__(self):
        pass#todo implement stack and __repr__

def parseFunctionBlock(tokens: List[Token], code: CodeBlock, functions: CodeBlock) -> Tuple[List[Token], CodeBlock, CodeBlock]:
    pass

def parse(tokens: List[Token]) -> Tuple[CodeBlock, CodeBlock]:
    """Function used to parse a block of code to correct function to be used by the runner"""
    
    return map(parseCodeBlock(tokens, CodeBlock(), CodeBlock()))



#parseCodeBlock :: [Token] -> CodeBlock -> CodeBlock -> ([Token], CodeBlock, CodeBlock)
def parseCodeBlock(tokens: List[Token], code: CodeBlock, functions: CodeBlock) -> Tuple[List[Token], CodeBlock, CodeBlock]:
    """Function used to parse a block of code to correct function to be used by the runner

    Args:
        tokens (List[Token]): list of tokens used to 
        code (CodeBlock): block of code
        functions (CodeBlock): all the declared functions and there code

    Returns:
        Tuple[List[Token], CodeBlock]: the list of tokens and the block of code
    """
    
    if tokens == None or len(tokens) == 0:
        return None, code, functions
    token, *rest = tokens
    #newCode = copy.deepcopy(code)
    
    if isinstance(token, ERR):
        return tokens, code, functions
    if isinstance(token, fnc) and code.nestLevel == 1 and token.isInALoop == 1:
        #an other function is declared, but not be added to the current function
        return tokens, code, functions
    newCode = None
    if isinstance(token, Directory):
        newRest, block, functions_ = parseCodeBlock(rest, CodeBlock(nest=token.isInALoop), functions)
        if isinstance(token,fnc):
            newFunctions = copy.deepcopy(functions_).addStatement(DeclareFunction(block, token.parameter1, token.functionInput))#because of functional programming, idk how pure it was needed, but in pure it is not allowed also in local scale to overwrite an variable, deepcopy because otherwise the original object will be changed
            #functions_.addStatement(DeclareFunction(block, token.parameter1, token.functionInput))
            
            #return parseCodeBlock(newRest, code, newFunctions)
        elif isinstance(token,dif_directory):
            ##newCode.addStatement(Loop(block, token.parameter1,False,False,True))
            return parseCodeBlock(newRest, copy.deepcopy(code).addStatement(Loop(block, token.parameter1,False,False,True)), functions_)
        elif isinstance(token,nif):
            ##newCode.addStatement(Loop(block, token.parameter1,True,False,True))
            return parseCodeBlock(newRest, copy.deepcopy(code).addStatement(Loop(block, token.parameter1,True,False,True)), functions_)
        elif isinstance(token,lpc):
            ##newCode.addStatement(Loop(block, token.parameter1,False,False,False))
            return parseCodeBlock(newRest, copy.deepcopy(code).addStatement(Loop(block, token.parameter1,False,False,False)), functions_)
        elif isinstance(token,lpn):
            ##newCode.addStatement(Loop(block, token.parameter1,True,False,False))
            return parseCodeBlock(newRest, copy.deepcopy(code).addStatement(Loop(block, token.parameter1,True,False,False)), functions_)
        elif isinstance(token,dlw):
            ##newCode.addStatement(Loop(block, token.parameter1,False,True,False))
            return parseCodeBlock(newRest, copy.deepcopy(code).addStatement(Loop(block, token.parameter1,False,True,False)), functions_)
        elif isinstance(token,dlu):
            ##newCode.addStatement(Loop(block, token.parameter1,True,True,False))
            return parseCodeBlock(newRest, copy.deepcopy(code).addStatement(Loop(block, token.parameter1,True,True,False)), functions_)
    
    if token.isInALoop is not code.nestLevel:
        return tokens, code, functions
      
    elif isinstance(token, DAT):
        if isinstance(token, abs):
            #newCode.addStatement(valueConv(token.parameter1, token.parameter2, ConvertType.absolute, Instruction_Variable_Type.Integer))
            #return parseCodeBlock(rest, copy.deepcopy(code).addStatement(valueConv(token.parameter1, token.parameter2, ConvertType.absolute, Instruction_Variable_Type.Integer)), functions)
            #return rest, 
        elif isinstance(token, neg):
            #newCode.addStatement(valueConv(token.parameter1, token.parameter2, ConvertType.negative, Instruction_Variable_Type.Integer))
            return parseCodeBlock(rest, copy.deepcopy(code).addStatement(valueConv(token.parameter1, token.parameter2, ConvertType.negative, Instruction_Variable_Type.Integer)), functions)
        elif isinstance(token, add):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.plus, Instruction_Variable_Type.Integer))#todo maybe in other class not in same class ass bitwise
            return parseCodeBlock(rest, copy.deepcopy(code).addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.plus, Instruction_Variable_Type.Integer)), functions)#todo maybe in other class not in same class ass bitwise
        elif isinstance(token, sub_dat):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.minus, Instruction_Variable_Type.Integer))#maybe in other class not in same class ass bitwise
            return parseCodeBlock(rest, copy.deepcopy(code).addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.minus, Instruction_Variable_Type.Integer)), functions)
        elif isinstance(token, mul):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.multiply, Instruction_Variable_Type.Integer))#maybe in other class not in same class ass bitwise
            return parseCodeBlock(rest, copy.deepcopy(code).addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.multiply, Instruction_Variable_Type.Integer)), functions)
        elif isinstance(token, div_dat):#TODO: check for interference
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.divide, Instruction_Variable_Type.Integer))#maybe in other class not in same class ass bitwise
            return parseCodeBlock(rest, )
            
        elif isinstance(token, mod):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.modulo, Instruction_Variable_Type.Integer))#maybe in other class not in same class ass bitwise
        elif isinstance(token, and_):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.andOp, Instruction_Variable_Type.Integer))
        elif isinstance(token, orb):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.orb, Instruction_Variable_Type.Integer))
        elif isinstance(token, xor):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.xor, Instruction_Variable_Type.Integer))
        elif isinstance(token, xad):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.xad, Instruction_Variable_Type.Integer))
        elif isinstance(token, nad):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.nad, Instruction_Variable_Type.Integer))
        elif isinstance(token, nor):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.nor, Instruction_Variable_Type.Integer))
        elif isinstance(token, not_):
            #newCode.addStatement(valueConv(token.parameter1, token.parameter2, ConvertType.bitWiseNot, Instruction_Variable_Type.Integer))
        elif isinstance(token, mor):
            #newCode.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementType.GREATER, Instruction_Variable_Type.Integer))
        elif isinstance(token, les):
            #newCode.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementType.LESS, Instruction_Variable_Type.Integer))
        elif isinstance(token, equ):
            #newCode.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementType.EQUAL, Instruction_Variable_Type.Integer))
        elif isinstance(token, neq):
            ##newCode.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementType.NOTEQUAL, Instruction_Variable_Type.Integer))
        elif isinstance(token, get):
            ##newCode.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementType.GREATEREQUAL, Instruction_Variable_Type.Integer))
        elif isinstance(token, let):
            ##newCode.addStatement(IfStatement(token.parameter1,token.parameter2, token.parameter3, IfStatementType.LESSEQUAL, Instruction_Variable_Type.Integer))
        elif isinstance(token, rdi):
            ##newCode.addStatement(setValue(token.parameter1, token.consoleInput, Instruction_Variable_Type.Integer))
        elif isinstance(token, ric):
            ##newCode.addStatement(setValue(token.parameter1, token.consoleInput, Instruction_Variable_Type.Integer))#TODO: set to -1 if eof not implemented
        elif isinstance(token, dsi):
            #newCode.addStatement(displayValue(token.parameter1, False, Instruction_Variable_Type.Integer))
        elif isinstance(token, dic):
            #newCode.addStatement(displayValue(token.parameter1, False, Instruction_Variable_Type.Integer))#todo display char of int
            # #newCode.addStatement(displayValue(token.parameter1))
        elif isinstance(token, set):
            #newCode.addStatement(setValue(token.parameter1, token.parameter2, Instruction_Variable_Type.Integer))
        elif isinstance(token, max_):
            #newCode.addStatement(operators(token.parameter1,token.parameter2, token.parameter3, operatorsType.maxVal, Instruction_Variable_Type.Integer))
        elif isinstance(token, min_):
            #newCode.addStatement(operators(token.parameter1,token.parameter2, token.parameter3, operatorsType.minVal, Instruction_Variable_Type.Integer))
    elif isinstance(token, TXT):
        if isinstance(token, rdc):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, rds):#no input from console because of functional programming is that not allowed
            #newCode.addStatement(setValue(token.parameter1, token.consoleInput, Instruction_Variable_Type.String))
        elif isinstance(token, eof):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, dsc):
            ##newCode.addStatement(displayValue(token.parameter1, True))#implement now good according to spec @todo
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, dss):
            #newCode.addStatement(displayValue(token.parameter1, False, Instruction_Variable_Type.String))
        elif isinstance(token, dsl):
            #newCode.addStatement(displayValue(token.parameter1, True, Instruction_Variable_Type.String))
        elif isinstance(token, dec):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, des):
            #newCode.addStatement(NotImplemented())#error stream is using output #todo maybe implement error stream
        elif isinstance(token, del_):
            #newCode.addStatement(NotImplemented())#todo maybe implement error stream instead of using normal stream
        elif isinstance(token, clr):
            #newCode.addStatement(setValue(token.parameter1, "", Instruction_Variable_Type.String))# vervang door var op 0 te zetten of nullptr#TODO TEST of dit werkt nog niet getest
        elif isinstance(token, cat):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.plus, Instruction_Variable_Type.String))#concat in python is just string 1 plus string 2
        elif isinstance(token, idx):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ids):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, lid):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, rep):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, sub_txt):#check if correct class
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, rmv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ins):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, tou):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, tol):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, pdl):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, cpl):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, pdr):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, cpr):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, sam):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, dif_txt):#check if correct dif class also in lexer
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, hiv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, lov):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, hev):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, lev):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ssw):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, sew):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, trm):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, tms):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, tme):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ses):
            #newCode.addStatement(setValue(token.parameter1, token.parameter2, Instruction_Variable_Type.String))
        
        ##newCode.addStatement(displayValue(token.parameter1))
    elif isinstance(token, BIN):
        if isinstance(token, pls):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.plus, Instruction_Variable_Type.Float))
        elif isinstance(token, mns):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.minus, Instruction_Variable_Type.Float))
        elif isinstance(token, tms):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.multiply, Instruction_Variable_Type.Float))
        elif isinstance(token, dvb):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.divide, Instruction_Variable_Type.Float))
        elif isinstance(token, pwr):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, token.parameter3, MathFloatType.power))
        elif isinstance(token, sgn):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.sign))
        elif isinstance(token, sqr):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.squareRoot))
        elif isinstance(token, sin):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.sin))
        elif isinstance(token, cos):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.cos))
        elif isinstance(token, tan):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.tan))
        elif isinstance(token, snh):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.hyperbolicSin))
        elif isinstance(token, csh):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.hyperbolicCos))
        elif isinstance(token, tnh):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.hyperbolicTan))
        elif isinstance(token, cil):
            #newCode.addStatement(roundValue(token.parameter1, token.parameter2, True))
        elif isinstance(token, flr):
            #newCode.addStatement(roundValue(token.parameter1, token.parameter2, False))
        elif isinstance(token, log):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.logBase10))
        elif isinstance(token, lge):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.logNatural))
        elif isinstance(token, lbq):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.log))
        elif isinstance(token, epw):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.eToPower))
        elif isinstance(token, avl):
            #newCode.addStatement(valueConv(token.parameter1, token.parameter2, ConvertType.absolute, Instruction_Variable_Type.Float))
        elif isinstance(token, rnd):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, rou):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, asn):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.inverseSin))
        elif isinstance(token, acs):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.inverseCos))
        elif isinstance(token, atn):
            #newCode.addStatement(mathFloatFunctions(token.parameter1, token.parameter2, MathFloatType.inverseTan))
        elif isinstance(token, mks):
            #newCode.addStatement(setValue(token.parameter1, token.parameter2, Instruction_Variable_Type.Float))#check if good?
        elif isinstance(token, fmx):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.maxVal, Instruction_Variable_Type.Float))
        elif isinstance(token, fmn):
            #newCode.addStatement(operators(token.parameter1, token.parameter2, token.parameter3, operatorsType.minVal, Instruction_Variable_Type.Float))
        elif isinstance(token, grt):
            #newCode.addStatement(IfStatement(token.parameter1, token.parameter2, token.parameter3, IfStatementType.GREATER, Instruction_Variable_Type.Float))
        elif isinstance(token, lst):
            #newCode.addStatement(IfStatement(token.parameter1, token.parameter2, token.parameter3, IfStatementType.LESS, Instruction_Variable_Type.Float))
        elif isinstance(token, eqt):
            #newCode.addStatement(IfStatement(token.parameter1, token.parameter2, token.parameter3, IfStatementType.EQUAL, Instruction_Variable_Type.Float))
        elif isinstance(token, net):
            #newCode.addStatement(IfStatement(token.parameter1, token.parameter2, token.parameter3, IfStatementType.NOTEQUAL, Instruction_Variable_Type.Float))
        elif isinstance(token, gte):
            #newCode.addStatement(IfStatement(token.parameter1, token.parameter2, token.parameter3, IfStatementType.GREATEREQUAL, Instruction_Variable_Type.Float))
        elif isinstance(token, lte):
            #newCode.addStatement(IfStatement(token.parameter1, token.parameter2, token.parameter3, IfStatementType.LESSEQUAL, Instruction_Variable_Type.Float))#INSTRUCTION IS WRONG IN DOCUMENTATION ON WEBSITE, THERE IS GTE AND LTE both greater then or equal. But of course lte must be less then equal 
        elif isinstance(token, rfv):
            #newCode.addStatement(setValue(token.parameter1, token.consoleInput, Instruction_Variable_Type.Float))#todo fix console reading
        elif isinstance(token, dfv_bin):
            #newCode.addStatement(displayValue(token.parameter1, False, Instruction_Variable_Type.Float))#todo fix console reading
        
    elif isinstance(token, ZIP):
        if isinstance(token, giv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, siv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, gsv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, siv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, gfv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, sfv):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, fia):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, zia):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, fsa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, zsa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ffa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, zfa):
            #newCode.addStatement(NotImplemented())
        ##newCode.addStatement(NotImplemented())
    elif isinstance(token, EXE):
        if isinstance(token, sia):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ssa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, sti):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, stf):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, stc):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, its):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, itf):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ias):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, aif):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, fts):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, fti):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, afi):
            #newCode.addStatement(NotImplemented())
        ##newCode.addStatement(NotImplemented())
    elif isinstance(token, DLL):
        if isinstance(token, psh):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, pop):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, spk):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ssz):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, enq):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, deq):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, qpk):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, qsz):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, tpl):
            #newCode.addStatement(Tape(TapeAction.MoveLeft))
        elif isinstance(token, tpr):
            #newCode.addStatement(Tape(TapeAction.MoveRight))
        elif isinstance(token, tsv):
            #newCode.addStatement(Tape(token.parameter1, TapeAction.ReadCurrentElementPosition))
        elif isinstance(token, tgv):
            #newCode.addStatement(Tape(token.parameter1, TapeAction.WriteElementToCurrentPosition))
        elif isinstance(token, gbe):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, gen):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, gef):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, lce):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, lcn):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, lcf):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ges):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, ces):
            #newCode.addStatement(NotImplemented())
        ##newCode.addStatement(NotImplemented())
    elif isinstance(token, CSV):
        if isinstance(token, cia):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, civ):
            #newCode.addStatement(createVar(token.parameter1, Instruction_Variable_Type.Integer))
        elif isinstance(token, csa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, csv):
            #newCode.addStatement(createVar(token.parameter1, Instruction_Variable_Type.String))
        elif isinstance(token, cfa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, cfv):
            #newCode.addStatement(createVar(token.parameter1, Instruction_Variable_Type.Float))
        elif isinstance(token, dia):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, div_csv):
            #newCode.addStatement(deleteVar(token.parameter1, Instruction_Variable_Type.Integer))
        elif isinstance(token, dsa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, dsv):
            #newCode.addStatement(deleteVar(token.parameter1, Instruction_Variable_Type.String))
        elif isinstance(token, dfa):
            #newCode.addStatement(NotImplemented())
        elif isinstance(token, dfv_csv): 
            #newCode.addStatement(deleteVar(token.parameter1, Instruction_Variable_Type.Float))
            ##newCode.addStatement(displayValue(token.parameter1, False))?????
        #else: 
        #    #newCode.addStatement(createVar(token.parameter1))
    elif isinstance(token, LNK):
        if isinstance(token, run):
            #newCode.addStatement(CallFunction(token.functionName, token.parameterVar, token.returnVar))
        elif isinstance(token,rtn):
            #newCode.addStatement(ReturnFunction(token.parameter1))    
    if len(tokens) >= 2:#needed because if loop closes 2 times it will not correctly work because it will not close the loop 2 times
        if (rest[0].isInALoop) - (token.isInALoop) < 0:
            return rest, newCode, functions
    return parseCodeBlock(rest, newCode, functions)