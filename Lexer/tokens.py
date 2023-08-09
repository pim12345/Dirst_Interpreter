from enum import Enum
import string
from typing import NamedTuple, Union

class Instruction_Variable_Type(Enum):
    #an enum to describe an instruction var type
    Unknown = '0'#TODO convert str functies van elk statement i.p.v van str convert naar goede type voor debug 
    Integer = 'int'
    String = "str"
    Float = "float"
    Function = "function"
    
    #ListValues :: () -> [String]
    @staticmethod
    def ListValues() -> list:#return list of all values of this enum
        return list(map(lambda instruction: instruction.value, Instruction_Variable_Type))
    
    #ListNames :: () -> [String]
    @staticmethod
    def ListNames() -> list:
        return list(map(lambda instruction: instruction.name, Instruction_Variable_Type))
    
    #__str__ :: Instruction_Variable_Type -> String    
    def __str__(self) -> str:
        return self.__repr__()   
    
    # __repr__ :: Instruction_Variable_Type -> String
    def __repr__(self) -> str:
        return self.name

class Instruction_Subsets(Enum):
    DAT = "dat"
    TXT = "txt"
    BIN = "bin"
    ZIP = "zip"
    EXE = "exe"
    DLL = "dll"
    CSV = 'csv'
    LNK = 'lnk'
    DIRECTORY = "directory"
    
    #ListValues :: () -> [String]
    @staticmethod
    def ListValues() -> list:#return list of all values of this enum
        return list(map(lambda instruction: instruction.value, Instruction_Subsets))
    
    #ListNames :: () -> [String]
    @staticmethod
    def ListNames() -> list:
        return list(map(lambda instruction: instruction.name, Instruction_Subsets))
    
    #__str__ :: Instruction_Subsets -> String    
    def __str__(self) -> str:
        return self.__repr__()   
    
    # __repr__ :: Instruction_Subsets -> String
    def __repr__(self) -> str:
        return self.name

########## Tokens ###############
class Token:
    def __init__(self, isInALoop : int):
        self.isInALoop = isInALoop
    
    #__repr__ :: Token -> String
    def __repr__(self) -> str:
        return "Token class"
    
    # __str__ :: Token -> String
    def __str__(self) -> str:
        return self.__repr__()

##################################
########## Directory Tokens ######
class Directory(Token):
    #__repr__ :: Directory -> String
    def __repr__(self) -> str:
        return "Directory token, Handles looping, conditionals and code separation"
    
    def __str__(self) -> str:
        return self.__repr__()

class fnc(Directory):
    def __init__(self, parameter1: str, functionInput: str, isInALoop : int):
        self.parameter1 = parameter1
        self.functionInput = functionInput
        super().__init__(isInALoop)
        
    #__repr__ :: fnc -> String
    def __repr__(self) -> str:
        return "Execute all subitems in the directory"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dif_directory(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
         
    #__repr__ :: dif_ -> String
    def __repr__(self) -> str:
        return "Execute directory subitems only if the specified integer value is not zero"
    def __str__(self) -> str:
        return self.__repr__()
class nif(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: nif -> String
    def __repr__(self) -> str:
        return "Execute directory subitems only if the specified integer value is zero"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class lpc(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
         
    #__repr__ :: lpc -> String
    def __repr__(self) -> str:
        return "Loop through directory subitems while the specified integer value is not zero"
    def __str__(self) -> str:
        return self.__repr__()
    
class lpn(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: lpn -> String
    def __repr__(self) -> str:
        return "Loop through directory subitems while the specified integer value is zero"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dlw(Directory):
    def __init__(self,parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dlw -> String
    def __repr__(self) -> str:
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
    
    def __str__(self) -> str:
        return self.__repr__()
class dlu(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dlu -> String
    def __repr__(self) -> str:
        return "Do loop through directory subitems while the specified integer value is zero (loop at least once)"
    
    def __str__(self) -> str:
        return self.__repr__()

##################################
########## DAT Tokens ############
class DAT(Token):
    #__repr__ :: DAT -> String
    def __repr__(self) -> str:
        return "DAT token, Contains all integer functionality and logic"
    
    def __str__(self) -> str:
        return self.__repr__()

class abs(DAT):
    #__repr__ :: abs -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: " + str(self.parameter1) + " to the absolute value of parameter 2: " + str(self.parameter2)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class neg(DAT):
    #__repr__ :: neg -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the negative value of parameter 2:"
    
    def __str__(self) -> str:
        return self.__repr__()

    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class add(DAT):
    #__repr__ :: add -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: plus parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sub_dat(DAT):
    #__repr__ :: sub_ -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: minus parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class mul(DAT):
    #__repr__ :: mul -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: times parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class div_dat(DAT):
    #__repr__ :: div -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: divided by parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class mod(DAT):
    #__repr__ :: mod -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: modulo parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        

class and_(DAT):
    #__repr__ :: and_ -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise and parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
        
class orb(DAT):
    #__repr__ :: orb -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise or parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class xor_dat(DAT):
    #__repr__ :: xor -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise xor parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class xad(DAT):
    #__repr__ :: xad -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise xand parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class nad(DAT):
    #__repr__ :: nad -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise nand parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class nor(DAT):
    #__repr__ :: nor -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise nor parameter 3:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class not_(DAT):
    #__repr__ :: not_ -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to the value of the bitwise not of parameter 2:"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class mor(DAT):
    #__repr__ :: mor -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is greater than parameter 3:, otherwise 0"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class les(DAT):
    #__repr__ :: les -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is less than parameter 3:, otherwise 0"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class equ(DAT):
    #__repr__ :: equ -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is equal to parameter 3:, otherwise 0"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class neq(DAT):
    #__repr__ :: neq -> String
    def __repr__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is not equal to parameter 3:, otherwise 0"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class get(DAT):
    #__repr__ :: get -> String
    def __repr__(self) -> str:
        return "Sets parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, otherwise 0"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class let(DAT):
    #__repr__ :: let -> String
    def __repr__(self) -> str:
        return "Sets parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, otherwise 0"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class rdi(DAT):
    #__repr__ :: rdi -> String
    def __repr__(self) -> str:
        return "Reads an integer from the console and sets the specified integer variable to the value. If EOF is encountered, the variable is not modified and EOF is marked."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class ric(DAT):
    #__repr__ :: ric -> String
    def __repr__(self) -> str:
        return "Read a character from the console and sets the specified integer variable to the value. If EOF is encountered, the variable is set to -1."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class dsi(DAT):
    #__repr__ :: dsi -> String
    def __repr__(self) -> str:
        return "Display the specified integer value to the console"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dic(DAT):
    #__repr__ :: dic -> String
    def __repr__(self) -> str:
        return "Display the character specified by the integer value to the console"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class set(DAT):
    #__repr__ :: set -> String
    def __repr__(self) -> str:
        return "Sets parameter 1 to the value of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class max_(DAT):#is max_ because max is a python function
    #__repr__ :: max -> String
    def __repr__(self) -> str:
        return "Sets parameter 1 to the higher value out of parameter 2 and parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class min_(DAT):#is min_ because min is a python function
    #__repr__ :: min -> String
    def __repr__(self) -> str:
        return "Sets parameter 1 to the lower value out of parameter 2 and parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        

##################################
########## TXT Tokens ############
class TXT(Token):
    #__repr__ :: TXT -> String
    def __repr__(self) -> str:
        return "TXT token, Contains all string functionality and logic as well as advanced console IO"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class rdc(TXT):
    #__repr__ :: rdc -> String
    def __repr__(self) -> str:
        return "Reads a character from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class rds(TXT):
    #__repr__ :: rds -> String
    def __repr__(self) -> str:
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class eof(TXT):
    #__repr__ :: eof -> String
    def __repr__(self) -> str:
        return "Sets the given integer variable to -1 it EOF has been reached, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dsc(TXT):
    #__repr__ :: dsc -> String
    def __repr__(self) -> str:
        return "Displays the character from string parameter 1 at index parameter 2 (base 0) to the console"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class dss(TXT):
    #__repr__ :: dss -> String
    def __repr__(self) -> str:
        return "Displays the given string variable to the console with no newline following"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dsl(TXT):
    #__repr__ :: dsl -> String
    def __repr__(self) -> str:
        return "Displays the given string variable to the console followed by a newline"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dec(TXT):
    #__repr__ :: dec -> String
    def __repr__(self) -> str:
        return "Displays the character from string parameter 1 at index parameter 2 (base 0) to STDERR"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class des(TXT):
    #__repr__ :: des -> String
    def __repr__(self) -> str:
        return "Displays the given string variable to STDERR with no newline following"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class del_(TXT):
    #__repr__ :: del_ -> String
    def __repr__(self) -> str:
        return "Displays the given string variable to STDERR followed by a newline"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class clr(TXT):
    #__repr__ :: clr -> String
    def __repr__(self) -> str:
        return "Clears the given string variable: " + str(self.parameter1)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class cat(TXT):
    #__repr__ :: cat -> String
    def __repr__(self) -> str:
        return "Concats parameter 2 and parameter 3 and sets parameter 1 to the result"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class idx(TXT):
    #__repr__ :: idx -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the index of the first occurrence of parameter 3 in parameter 2, or -1 if not found"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class ids(TXT):
    #__repr__ :: ids -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the index of the first occurrence of parameter 3 in parameter 2 after specified index parameter 4, or -1 if not found"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class lid(TXT):
    #__repr__ :: lid -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the index of the last occurrence of parameter 3 in parameter 2, or -1 if not found"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class rep(TXT):
    #__repr__ :: rep -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2, replacing every occurrence of parameter 3 with parameter 4"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class sub_txt(TXT):
    #__repr__ :: sub -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the substring of parameter 2 from index parameter 3 (base 0) of length parameter 4"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class rmv(TXT):
    #__repr__ :: rmv -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 removing characters from index parameter 3 (base 0) of length parameter 4"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class ins(TXT):
    #__repr__ :: ins -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 inserting substring parameter 4 at index parameter 3 (base 0)"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class tou(TXT):
    #__repr__ :: tou -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the all uppercase value of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class tol(TXT):
    #__repr__ :: tol -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the all lowercase value of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class pdl(TXT):
    #__repr__ :: pdl -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the left-hand side with spaces until length parameter 3 is reached"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class cpl(TXT):
    #__repr__ :: cpl -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the left-hand side with the character value parameter 4 until length parameter 3 is reached"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class pdr(TXT):
    #__repr__ :: pdr -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the right-hand side with spaces until length parameter 3 is reached"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class cpr(TXT):
    #__repr__ :: cpr -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the right-hand side with the character value parameter 4 until length parameter 3 is reached"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class sam(TXT):
    #__repr__ :: sam -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is equal to parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class dif_txt(TXT):
    #__repr__ :: dif -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is not equal to parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class hiv(TXT):
    #__repr__ :: hiv -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically after parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lov(TXT):
    #__repr__ :: lov -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically before parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class hev(TXT):
    #__repr__ :: hev -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically after or equal to parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lev(TXT):
    #__repr__ :: lev -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically before or equal to parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class ssw(TXT):
    #__repr__ :: ssw -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 starts with parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sew(TXT):
    #__repr__ :: sew -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 ends with parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class trm(TXT):
    #__repr__ :: trm -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 trimming all leading and trailing occurrences of the characters in parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class tms(TXT):
    #__repr__ :: tms -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 trimming all leading occurrences of the characters in parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class tme(TXT):
    #__repr__ :: tme -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to parameter 2 trimming all trailing occurrences of the characters in parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class ses(TXT):
    #__repr__ :: ses -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        

##################################
########## BIN Tokens ############
class BIN(Token):
    #__repr__ :: BIN -> String
    def __repr__(self) -> str:
        return "Contains all floating point functionality and logic as well as advanced math operations"
    
    def __str__(self) -> str:
        return self.__repr__()
    

class pls(BIN):
    #__repr__ :: pls -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 plus parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class mns(BIN):
    #__repr__ :: mns -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 minus parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
           
class tms(BIN):
    #__repr__ :: tms -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 times parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class dvb(BIN):
    #__repr__ :: dvb -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 divided by parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class pwr(BIN):
    #__repr__ :: pwr -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 to the power of parameter 3"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sgn(BIN):
    #__repr__ :: sgn -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the sign of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class sqr(BIN):
    #__repr__ :: sqr -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the square root of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class sin(BIN):
    #__repr__ :: sin -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the sine of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class cos(BIN):
    #__repr__ :: cos -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the cosine of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class tan(BIN):
    #__repr__ :: tan -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the tangent of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class snh(BIN):
    #__repr__ :: snh -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the hyperbolic sine of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class csh(BIN):
    #__repr__ :: csh -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the hyperbolic cosine of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class tnh(BIN):
    #__repr__ :: tnh -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the hyperbolic tangent of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class cil(BIN):
    #__repr__ :: cil -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the ceiling of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class flr(BIN):
    #__repr__ :: flr -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the floor of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class log(BIN):
    #__repr__ :: log -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the base 10 logarithm of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class lge(BIN):
    #__repr__ :: lge -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the natural logarithm of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class lbq(BIN):
    #__repr__ :: lbq -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the base parameter 3 logarithm of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class epw(BIN):
    #__repr__ :: epw -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of e to the power of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class avl(BIN):
    #__repr__ :: avl -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the absolute value of parameter 2"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class rnd(BIN):
    #__repr__ :: rnd -> String
    def __repr__(self) -> str:
        return "Set the given float variable to a random value between 0.0 and 1.0 inclusive"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class rou(BIN):
    #__repr__ :: rou -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 rounded to the nearest whole number"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class asn(BIN):
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
    #__repr__ :: asn -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the inverse sine of parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
class acs(BIN):
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
    #__repr__ :: acs -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the inverse cosine of parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
class atn(BIN):
    #__repr__ :: atn -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of the inverse tangent of parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class mks(BIN):
    #__repr__ :: mks -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fmx(BIN):
    #__repr__ :: fmx -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the greater value of either parameter 2 or parameter 3 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class fmn(BIN):
    #__repr__ :: fmn -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the lesser value of either parameter 2 or parameter 3 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class grt(BIN):
    #__repr__ :: grt -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is greater than parameter 3, 0 otherwise "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lst(BIN):
    #__repr__ :: lst -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is less than parameter 3, 0 otherwise "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class eqt(BIN):
    #__repr__ :: eqt -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is equal to parameter 3, 0 otherwise "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class net(BIN):
    #__repr__ :: net -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is not equal to parameter 3, 0 otherwise "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class gte(BIN):
    #__repr__ :: gte -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, 0 otherwise"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lte(BIN):
    #__repr__ :: lte -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, 0 otherwise. Wrong in original Dirst documentation."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class rfv(BIN):
    #__repr__ :: rfv -> String
    def __repr__(self) -> str:
        return "Reads a floating point value from the console and sets the specified float variable to the value. If EOF is encountered, the variable is not modified and EOF is marked. "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class dfv_bin(BIN):
    #__repr__ :: dfv -> String
    def __repr__(self) -> str:
        return "Display the specified float value to the console "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        

##################################
########## ZIP Tokens ############
class ZIP(Token):
    #__repr__ :: ZIP -> String
    def __repr__(self) -> str:
        return "Manages arrays and array values"
    
    def __str__(self) -> str:
        return self.__repr__()
    
        
class giv(ZIP):
    #__repr__ :: giv -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the integer value in array parameter 2 at index parameter 3 (base 0) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class siv(ZIP):
    #__repr__ :: siv -> String
    def __repr__(self) -> str:
        return "Set an integer value in array parameter 1 at index parameter 2 (base 0) to the value of parameter 3 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class gsv(ZIP):
    #__repr__ :: gsv -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the string value in array parameter 2 at index parameter 3 (base 0) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
#dubblicate siv class in original documenation
class gfv(ZIP):
    #__repr__ :: gfv -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the float value in array parameter 2 at index parameter 3 (base 0) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sfv(ZIP):
    #__repr__ :: sfv -> String
    def __repr__(self) -> str:
        return "Set an float value in array parameter 1 at index parameter 2 (base 0) to the value of parameter 3 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class fia(ZIP):
    #__repr__ :: fia -> String
    def __repr__(self) -> str:
        return "Resizes the integer array in parameter 1 to the size parameter 2 (base 0), preserving data "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class zia(ZIP):
    #__repr__ :: zia -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the size of the integer array in parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fsa(ZIP):
    #__repr__ :: fsa -> String
    def __repr__(self) -> str:
        return "Resizes the string array in parameter 1 to the size parameter 2 (base 0), preserving data "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class zsa(ZIP):
    #__repr__ :: zsa -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the size of the string array in parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class ffa(ZIP):
    #__repr__ :: ffa -> String
    def __repr__(self) -> str:
        return "Resizes the float array in parameter 1 to the size parameter 2 (base 0), preserving data "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class zfa(ZIP):
    #__repr__ :: zfa -> String
    def __repr__(self) -> str:
        return "Set parameter 1 to the size of the float array in parameter 2 "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        

##################################
########## EXE Tokens ############
class EXE(Token):
    #__repr__ :: EXE -> String
    def __repr__(self) -> str:
        return "Handles type conversion and value/array transcoding"
    
    def __str__(self) -> str:
        return self.__repr__()
    

class sia(EXE):
    #__repr__ :: sia -> String
    def __repr__(self) -> str:
        return "Converts the string value in parameter 2 into the integer array in parameter 1 where each integer represents a character code "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class ssa(EXE):
    #__repr__ :: ssa -> String
    def __repr__(self) -> str:
        return "Converts the string value in parameter 2 into the string array in parameter 1 by splitting it using the string value parameter 3 as a delimiter "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sti(EXE):
    #__repr__ :: sti -> String
    def __repr__(self) -> str:
        return "Converts the string value in parameter 2 into the integer variable in parameter 1 by interpreting the base 10 value represented by the string "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class stf(EXE):
    #__repr__ :: stf -> String
    def __repr__(self) -> str:
        return "Converts the string value in parameter 2 into the float variable in parameter 1 by interpreting the decimal value represented by the string "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class stc(EXE):
    #__repr__ :: stc -> String
    def __repr__(self) -> str:
        return "Converts the string value in parameter 2 into the integer variable in parameter 1 by retrieving the character code of the character at index parameter 3 (base 0) in the string "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class its(EXE):
    #__repr__ :: its -> String
    def __repr__(self) -> str:
        return "Converts the integer value in parameter 2 into the string variable in parameter 1 by converting it into a base 10 string representation "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class itf(EXE):
    #__repr__ :: itf -> String
    def __repr__(self) -> str:
        return "Converts the integer value in parameter 2 into the float variable in parameter 1 using equivalence"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class ias(EXE):
    #__repr__ :: ias -> String
    def __repr__(self) -> str:
        return "Converts the integer array in parameter 2 into the string variable in parameter 1 by converting each integer element of the array into a character with the character code specified by the value "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class aif(EXE):
    #__repr__ :: aif -> String
    def __repr__(self) -> str:
        return "Converts the integer array in parameter 2 into the float array in parameter 1 by transforming each element using equivalence "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fts(EXE):
    #__repr__ :: fts -> String
    def __repr__(self) -> str:
        return "Converts the float value in parameter 2 into the string variable in parameter 1 by converting it into a standard format decimal string representation "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fti(EXE):
    #__repr__ :: fti -> String
    def __repr__(self) -> str:
        return "Converts the float value in parameter 2 into the integer variable in parameter 1 using equivalence "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class afi(EXE):
    #__repr__ :: afi -> String
    def __repr__(self) -> str:
        return "Converts the float array in parameter 2 into the integer array in parameter 1 by transforming each element using equivalence "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        

##################################
########## DLL Tokens ############
class DLL(Token):
    #__repr__ :: DLL -> String
    def __repr__(self) -> str:
        return "DLL token, Contains all extensions and specialized instructions, such as exception handling and abstract data structures"
    
    def __str__(self) -> str:
        return self.__repr__()
    

class psh(DLL):
    #__repr__ :: psh -> String
    def __repr__(self) -> str:
        return "Pushes the integer value onto the stack "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class pop(DLL):
    #__repr__ :: pop -> String
    def __repr__(self) -> str:
        return "Set the specified integer variable to the value popped from the stack. An exception is thrown if the stack is empty."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class spk(DLL):
    #__repr__ :: spk -> String
    def __repr__(self) -> str:
        return "Set the specified integer variable to the value peeked from the stack. An exception is thrown if the stack is empty. "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class ssz(DLL):
    #__repr__ :: ssz -> String
    def __repr__(self) -> str:
        return "Set the specified integer variable to the value of the size of the stack "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class enq(DLL):
    #__repr__ :: enq -> String
    def __repr__(self) -> str:
        return "Enqueues the specified integer value in the queue "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class deq(DLL):
    #__repr__ :: deq -> String
    def __repr__(self) -> str:
        return "Set the specified integer variable to the value dequeued from the queue. An exception is thrown if the queue is empty. "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class qpk(DLL):
    #__repr__ :: qpk -> String
    def __repr__(self) -> str:
        return "Set the specified integer variable to the value peeked from the queue. An exception is thrown if the queue is empty. "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class qsz(DLL):
    #__repr__ :: qsz -> String
    def __repr__(self) -> str:
        return "Set the specified integer variable to the value of the size of the queue "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class tpl(DLL):
    #__repr__ :: tpl -> String
    def __repr__(self) -> str:
        return "Moves the tape left "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class tpr(DLL):
    #__repr__ :: tpr -> String
    def __repr__(self) -> str:
        return "Moves the tape right "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class tsv(DLL):
    #__repr__ :: tsv -> String
    def __repr__(self) -> str:
        return "Sets the current element of the tape to the specified integer value "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        super().__init__(isInALoop)
        
        self.parameter1 = parameter1
class tgv(DLL):
    #__repr__ :: tgv -> String
    def __repr__(self) -> str:
        return "Sets the specified integer variable to the value of the current element of the tape "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1: str, isInALoop : int):
        super().__init__(isInALoop)
        self.parameter1 = parameter1
class gbe(DLL):
    #__repr__ :: gbe -> String
    def __repr__(self) -> str:
        return "Changes the error handling mode to global "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class gen(DLL):
    #__repr__ :: gen -> String
    def __repr__(self) -> str:
        return "Turns global errors on (exception handling off) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class gef(DLL):
    #__repr__ :: gef -> String
    def __repr__(self) -> str:
        return "Turns global errors off (exception handling on) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class lce(DLL):
    #__repr__ :: lce -> String
    def __repr__(self) -> str:
        return "Changes the error handling mode to local "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class lcn(DLL):
    #__repr__ :: lcn -> String
    def __repr__(self) -> str:
        return "Turns local errors on (exception handling off) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class lcf(DLL):
    #__repr__ :: lcf -> String
    def __repr__(self) -> str:
        return "Turns local errors off (exception handling on) "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class ges(DLL):
    #__repr__ :: ges -> String
    def __repr__(self) -> str:
        return "Sets the specified string variable to the error message from the last caught exception in the given scope "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, parameter1 : str, isInALoop : int):
        super().__init__(isInALoop)
        
        self.parameter1 = parameter1
class ces(DLL):
    #__repr__ :: ces -> String
    def __repr__(self) -> str:
        return "Clears the error string in the given scope "
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        

##################################
########## CSV Tokens used for variables and arrays ######
class CSV(Token):
    #__repr__ :: CSV -> String
    def __repr__(self) -> str:
        return "CSV token, Manages, creates, and destroys variables and arrays"
    
    def __str__(self) -> str:
        return self.__repr__()
    

class cia(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: cia -> String
    def __repr__(self) -> str:
        return "Creates an integer array with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class civ(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: civ -> String
    def __repr__(self) -> str:
        return "Creates an integer variable with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class csa(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: csa -> String
    def __repr__(self) -> str:
        return "Creates a string array with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class csv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: csv -> String
    def __repr__(self) -> str:
        return "Creates a string variable with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()    
    
class cfa(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: cfa -> String
    def __repr__(self) -> str:
        return "Creates a float array with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class cfv(CSV):
    def __init__(self, parameter1: str ,isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: cfv -> String
    def __repr__(self) -> str:
        return "Creates a float variable with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dia(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dia -> String
    def __repr__(self) -> str:
        return "Deletes an integer array with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class div_csv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: div -> String
    def __repr__(self) -> str:
        return "Deletes an integer variable with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dsa(CSV):
    def __init__(self, parameter1 : str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dsa -> String
    def __repr__(self) -> str:
        return "Deletes a string array with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dsv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dsv -> String
    def __repr__(self) -> str:
        return "Deletes a string variable with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dfa(CSV):
    def __init__(self, parameter1:str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dfa -> String
    def __repr__(self) -> str:
        return "Deletes a float array with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    
class dfv_csv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: dfv -> String
    def __repr__(self) -> str:
        return "Deletes a float variable with the specified variable name"
    
    def __str__(self) -> str:
        return self.__repr__()
    

##################################
########## LNK Tokens are used for function calls and the like ######
class LNK(Token):
    #__repr__ :: LNK -> String
    def __repr__(self) -> str:
        return "function calls and the like. Not in original Dirst added for requirement for ATP school project"
    
    def __str__(self) -> str:
        return self.__repr__()
    

class run(LNK):
    def __init__(self, functionName: str, parameterVar: str, returnVar: str ,isInALoop : int) -> None:
        self.functionName = functionName
        self.parameterVar = parameterVar
        self.returnVar = returnVar
        super().__init__(isInALoop)
        
    #__repr__ :: run -> String
    def __repr__(self) -> str:
        return "call function with name functionName and pass parameterVar as parameter and save result to returnVar"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    
class rtn(LNK):
    def __init__(self, parameter1: str, isInALoop : int) -> None:
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__repr__ :: rtn -> String
    def __repr__(self) -> str:
        return "return parameter 1 to function, the value of variable of parameter 1 is: " + str(self.parameter1)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    
##################################
########## ERR Tokens ############
class ERR(Token):
    def __init__(self, message: str) -> None:
        super().__init__(-1)#needed for uper class to work, but not used, because this is an error
        self.message = message
    #__repr__ :: LNK -> String
    def __repr__(self) -> str:
        return "Error: " + self.message
    
    def __str__(self) -> str:
        return self.__repr__()
    
