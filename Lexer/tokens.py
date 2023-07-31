from enum import Enum
import string
from typing import NamedTuple, Union

class Instruction_Variable_Type(Enum):
    #an enum to describe an instruction input type
    #this is made because there is a lot of dubble instruction like the add instruction (add 2 int together) and the pls instruction to add 2 floats together
    Unknown = '0'#todo convert str functies van elk statement i.p.v van str convert naar goede type voor debug 
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

#nog toevoegen __repr__ ook toevoegen denk i.p.v __str__
class Instruction_Subsets(Enum):
    DAT = "dat"
    TXT = "txt"
    BIN = "bin"
    ZIP = "zip"
    EXE = "exe"
    DLL = "dll"
    CSV = 'csv'
    LNK = 'lnk'
    DIRECTORY = ""
    
    #ListValues :: () -> [String]
    @staticmethod
    def ListValues() -> list:#return list of all values of this enum
        return list(map(lambda instruction: instruction.value, Instruction_Subsets))
    
    #ListNames :: () -> [String]
    @staticmethod
    def ListNames() -> list:
        return list(map(lambda instruction: instruction.name, Instruction_Subsets))

########## Tokens ###############
class Token:
    def __init__(self, isInALoop : int):
        self.isInALoop = isInALoop
    
    #__str__ :: Token -> String
    def __str__(self) -> str:
        return "Token class"

##################################
########## Directory Tokens ######
class Directory(Token):
    #__str__ :: Directory -> String
    def __str__(self) -> str:
        return "Directory token, Handles looping, conditionals and code separation"

class fnc(Directory):
    def __init__(self, parameter1: str, functionInput: str, isInALoop : int):
        self.parameter1 = parameter1
        self.functionInput = functionInput
        super().__init__(isInALoop)
        
    #__str__ :: fnc -> String
    def __str__(self) -> str:
        return "Execute all subitems in the directory"
    
class dif_directory(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
         
    #__repr__ :: dif_ -> String
    def __str__(self) -> str:
        return "Execute directory subitems only if the specified integer value is not zero"
class nif(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: nif -> String
    def __str__(self) -> str:
        return "Execute directory subitems only if the specified integer value is zero"
    
class lpc(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
         
    #__str__ :: lpc -> String
    def __str__(self) -> str:
        return "Loop through directory subitems while the specified integer value is not zero"
    
class lpn(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: lpn -> String
    def __str__(self) -> str:
        return "Loop through directory subitems while the specified integer value is zero"
class dlw(Directory):
    def __init__(self,parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dlw -> String
    def __str__(self) -> str:
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
class dlu(Directory):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dlu -> String
    def __str__(self) -> str:
        return "Do loop through directory subitems while the specified integer value is zero (loop at least once)"

##################################
########## DAT Tokens ############
class DAT(Token):
    #__str__ :: DAT -> String
    def __str__(self) -> str:
        return "DAT token, Contains all integer functionality and logic"

class abs(DAT):
    #__str__ :: abs -> String
    def __str__(self) -> str:
        return "Sets parameter 1: " + str(self.parameter1) + " to the absolute value of parameter 2: " + str(self.parameter2)
    
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class neg(DAT):
    #__str__ :: neg -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the negative value of parameter 2:"

    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class add(DAT):
    #__str__ :: add -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: plus parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sub_dat(DAT):
    #__str__ :: sub_ -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: minus parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class mul(DAT):
    #__str__ :: mul -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: times parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class div_dat(DAT):
    #__str__ :: div -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: divided by parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class mod(DAT):
    #__str__ :: mod -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: modulo parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        

class and_(DAT):
    #__str__ :: and_ -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise and parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
        
class orb(DAT):
    #__str__ :: orb -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise or parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class xor(DAT):
    #__str__ :: xor -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise xor parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class xad(DAT):
    #__str__ :: xad -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise xand parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class nad(DAT):
    #__str__ :: nad -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise nand parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class nor(DAT):
    #__str__ :: nor -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of parameter 2: bitwise nor parameter 3:"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class not_(DAT):
    #__str__ :: not_ -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to the value of the bitwise not of parameter 2:"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class mor(DAT):
    #__str__ :: mor -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is greater than parameter 3:, otherwise 0"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class les(DAT):
    #__str__ :: les -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is less than parameter 3:, otherwise 0"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class equ(DAT):
    #__str__ :: equ -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is equal to parameter 3:, otherwise 0"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class neq(DAT):
    #__str__ :: neq -> String
    def __str__(self) -> str:
        return "Sets parameter 1: to -1 if parameter 2: is not equal to parameter 3:, otherwise 0"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class get(DAT):
    #__str__ :: get -> String
    def __str__(self) -> str:
        return "Sets parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, otherwise 0"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class let(DAT):
    #__str__ :: let -> String
    def __str__(self) -> str:
        return "Sets parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, otherwise 0"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class rdi(DAT):
    #__str__ :: rdi -> String
    def __str__(self) -> str:
        return "Reads an integer from the console and sets the specified integer variable to the value. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class ric(DAT):
    #__str__ :: ric -> String
    def __str__(self) -> str:
        return "Read a character from the console and sets the specified integer variable to the value. If EOF is encountered, the variable is set to -1."
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class dsi(DAT):
    #__str__ :: dsi -> String
    def __str__(self) -> str:
        return "Display the specified integer value to the console"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dic(DAT):
    #__str__ :: dic -> String
    def __str__(self) -> str:
        return "Display the character specified by the integer value to the console"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class set(DAT):
    #__str__ :: set -> String
    def __str__(self) -> str:
        return "Sets parameter 1 to the value of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class max_(DAT):#is max_ because max is a python function
    #__str__ :: max -> String
    def __str__(self) -> str:
        return "Sets parameter 1 to the higher value out of parameter 2 and parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class min_(DAT):#is min_ because min is a python function
    #__str__ :: min -> String
    def __str__(self) -> str:
        return "Sets parameter 1 to the lower value out of parameter 2 and parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        

##################################
########## TXT Tokens ############
class TXT(Token):
    #__str__ :: TXT -> String
    def __str__(self) -> str:
        return "TXT token, Contains all string functionality and logic as well as advanced console IO"
class rdc(TXT):
    #__str__ :: rdc -> String
    def __str__(self) -> str:
        return "Reads a character from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class rds(TXT):
    #__str__ :: rds -> String
    def __str__(self) -> str:
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class eof(TXT):
    #__str__ :: eof -> String
    def __str__(self) -> str:
        return "Sets the given integer variable to -1 it EOF has been reached, 0 otherwise"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dsc(TXT):
    #__str__ :: dsc -> String
    def __str__(self) -> str:
        return "Displays the character from string parameter 1 at index parameter 2 (base 0) to the console"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class dss(TXT):
    #__str__ :: dss -> String
    def __str__(self) -> str:
        return "Displays the given string variable to the console with no newline following"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dsl(TXT):
    #__str__ :: dsl -> String
    def __str__(self) -> str:
        return "Displays the given string variable to the console followed by a newline"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class dec(TXT):
    #__str__ :: dec -> String
    def __str__(self) -> str:
        return "Displays the character from string parameter 1 at index parameter 2 (base 0) to STDERR"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class des(TXT):
    #__str__ :: des -> String
    def __str__(self) -> str:
        return "Displays the given string variable to STDERR with no newline following"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class del_(TXT):
    #__str__ :: del_ -> String
    def __str__(self) -> str:
        return "Displays the given string variable to STDERR followed by a newline"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class clr(TXT):
    #__str__ :: clr -> String
    def __str__(self) -> str:
        return "Clears the given string variable: " + str(self.parameter1)
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class cat(TXT):
    #__str__ :: cat -> String
    def __str__(self) -> str:
        return "Concats parameter 2 and parameter 3 and sets parameter 1 to the result"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class idx(TXT):
    #__str__ :: idx -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the index of the first occurrence of parameter 3 in parameter 2, or -1 if not found"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class ids(TXT):
    #__str__ :: ids -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the index of the first occurrence of parameter 3 in parameter 2 after specified index parameter 4, or -1 if not found"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class lid(TXT):
    #__str__ :: lid -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the index of the last occurrence of parameter 3 in parameter 2, or -1 if not found"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class rep(TXT):
    #__str__ :: rep -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2, replacing every occurrence of parameter 3 with parameter 4"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class sub_txt(TXT):
    #__str__ :: sub -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the substring of parameter 2 from index parameter 3 (base 0) of length parameter 4"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class rmv(TXT):
    #__str__ :: rmv -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 removing characters from index parameter 3 (base 0) of length parameter 4"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class ins(TXT):
    #__str__ :: ins -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 inserting substring parameter 4 at index parameter 3 (base 0)"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class tou(TXT):
    #__str__ :: tou -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the all uppercase value of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class tol(TXT):
    #__str__ :: tol -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the all lowercase value of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class pdl(TXT):
    #__str__ :: pdl -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the left-hand side with spaces until length parameter 3 is reached"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class cpl(TXT):
    #__str__ :: cpl -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the left-hand side with the character value parameter 4 until length parameter 3 is reached"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class pdr(TXT):
    #__str__ :: pdr -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the right-hand side with spaces until length parameter 3 is reached"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class cpr(TXT):
    #__str__ :: cpr -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 padded on the right-hand side with the character value parameter 4 until length parameter 3 is reached"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, parameter4, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
        
class sam(TXT):
    #__str__ :: sam -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class dif_txt(TXT):
    #__str__ :: dif -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is not equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class hiv(TXT):
    #__str__ :: hiv -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically after parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lov(TXT):
    #__str__ :: lov -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically before parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class hev(TXT):
    #__str__ :: hev -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically after or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lev(TXT):
    #__str__ :: lev -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is lexicographically before or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class ssw(TXT):
    #__str__ :: ssw -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 starts with parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sew(TXT):
    #__str__ :: sew -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 ends with parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class trm(TXT):
    #__str__ :: trm -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 trimming all leading and trailing occurrences of the characters in parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class tms(TXT):
    #__str__ :: tms -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 trimming all leading occurrences of the characters in parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class tme(TXT):
    #__str__ :: tme -> String
    def __str__(self) -> str:
        return "Set parameter 1 to parameter 2 trimming all trailing occurrences of the characters in parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class ses(TXT):
    #__str__ :: ses -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        

##################################
########## BIN Tokens ############
class BIN(Token):
    #__str__ :: BIN -> String
    def __str__(self) -> str:
        return "Contains all floating point functionality and logic as well as advanced math operations"

class pls(BIN):
    #__str__ :: pls -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 plus parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class mns(BIN):
    #__str__ :: mns -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 minus parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
           
class tms(BIN):
    #__str__ :: tms -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 times parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class dvb(BIN):
    #__str__ :: dvb -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 divided by parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class pwr(BIN):
    #__str__ :: pwr -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 to the power of parameter 3"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sgn(BIN):
    #__str__ :: sgn -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the sign of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class sqr(BIN):
    #__str__ :: sqr -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the square root of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class sin(BIN):
    #__str__ :: sin -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the sine of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class cos(BIN):
    #__str__ :: cos -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the cosine of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class tan(BIN):
    #__str__ :: tan -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the tangent of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class snh(BIN):
    #__str__ :: snh -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the hyperbolic sine of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class csh(BIN):
    #__str__ :: csh -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the hyperbolic cosine of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class tnh(BIN):
    #__str__ :: tnh -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the hyperbolic tangent of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class cil(BIN):
    #__str__ :: cil -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the ceiling of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class flr(BIN):
    #__str__ :: flr -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the floor of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class log(BIN):
    #__str__ :: log -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the base 10 logarithm of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class lge(BIN):
    #__str__ :: lge -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the natural logarithm of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class lbq(BIN):
    #__str__ :: lbq -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the base parameter 3 logarithm of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class epw(BIN):
    #__str__ :: epw -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of e to the power of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class avl(BIN):
    #__str__ :: avl -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the absolute value of parameter 2"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class rnd(BIN):
    #__str__ :: rnd -> String
    def __str__(self) -> str:
        return "Set the given float variable to a random value between 0.0 and 1.0 inclusive"
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class rou(BIN):
    #__str__ :: rou -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 rounded to the nearest whole number"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class asn(BIN):
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
    #__str__ :: asn -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the inverse sine of parameter 2 "
class acs(BIN):
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
    #__str__ :: acs -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the inverse cosine of parameter 2 "
class atn(BIN):
    #__str__ :: atn -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of the inverse tangent of parameter 2 "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class mks(BIN):
    #__str__ :: mks -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the value of parameter 2 "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fmx(BIN):
    #__str__ :: fmx -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the greater value of either parameter 2 or parameter 3 "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class fmn(BIN):
    #__str__ :: fmn -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the lesser value of either parameter 2 or parameter 3 "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class grt(BIN):
    #__str__ :: grt -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is greater than parameter 3, 0 otherwise "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lst(BIN):
    #__str__ :: lst -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is less than parameter 3, 0 otherwise "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class eqt(BIN):
    #__str__ :: eqt -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is equal to parameter 3, 0 otherwise "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class net(BIN):
    #__str__ :: net -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is not equal to parameter 3, 0 otherwise "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class gte(BIN):
    #__str__ :: gte -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class lte(BIN):
    #__str__ :: lte -> String
    def __str__(self) -> str:
        return "Set parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, 0 otherwise. Wrong in original Dirst documentation."
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class rfv(BIN):
    #__str__ :: rfv -> String
    def __str__(self) -> str:
        return "Reads a floating point value from the console and sets the specified float variable to the value. If EOF is encountered, the variable is not modified and EOF is marked. "
    def __init__(self, parameter1: str, consoleInput : str, isInALoop : int):
        self.parameter1 = parameter1
        self.consoleInput = consoleInput
        super().__init__(isInALoop)
        
class dfv_bin(BIN):
    #__str__ :: dfv -> String
    def __str__(self) -> str:
        return "Display the sepecified float value to the console "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        

##################################
########## ZIP Tokens ############
class ZIP(Token):
    #__str__ :: ZIP -> String
    def __str__(self) -> str:
        return "Manages arrays and array values"
        
class giv(ZIP):
    #__str__ :: giv -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the integer value in array parameter 2 at index parameter 3 (base 0) "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class siv(ZIP):
    #__str__ :: siv -> String
    def __str__(self) -> str:
        return "Set an integer value in array parameter 1 at index parameter 2 (base 0) to the value of parameter 3 "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class gsv(ZIP):
    #__str__ :: gsv -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the string value in array parameter 2 at index parameter 3 (base 0) "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
#dubblicate siv class in original documenation
class gfv(ZIP):
    #__str__ :: gfv -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the float value in array parameter 2 at index parameter 3 (base 0) "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sfv(ZIP):
    #__str__ :: sfv -> String
    def __str__(self) -> str:
        return "Set an float value in array parameter 1 at index parameter 2 (base 0) to the value of parameter 3 "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class fia(ZIP):
    #__str__ :: fia -> String
    def __str__(self) -> str:
        return "Resizes the integer array in parameter 1 to the size parameter 2 (base 0), preserving data "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class zia(ZIP):
    #__str__ :: zia -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the size of the integer array in parameter 2 "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fsa(ZIP):
    #__str__ :: fsa -> String
    def __str__(self) -> str:
        return "Resizes the string array in parameter 1 to the size parameter 2 (base 0), preserving data "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class zsa(ZIP):
    #__str__ :: zsa -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the size of the string array in parameter 2 "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class ffa(ZIP):
    #__str__ :: ffa -> String
    def __str__(self) -> str:
        return "Resizes the float array in parameter 1 to the size parameter 2 (base 0), preserving data "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class zfa(ZIP):
    #__str__ :: zfa -> String
    def __str__(self) -> str:
        return "Set parameter 1 to the size of the float array in parameter 2 "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        

#todo check ff of dat goed is: one dubble removed
##################################
########## EXE Tokens ############
class EXE(Token):
    #__str__ :: EXE -> String
    def __str__(self) -> str:
        return "Handles type conversion and value/array transcoding"

class sia(EXE):
    #__str__ :: sia -> String
    def __str__(self) -> str:
        return "Converts the string value in parameter 2 into the integer array in parameter 1 where each integer represents a character code "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class ssa(EXE):
    #__str__ :: ssa -> String
    def __str__(self) -> str:
        return "Converts the string value in parameter 2 into the string array in parameter 1 by splitting it using the string value parameter 3 as a delimiter "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class sti(EXE):
    #__str__ :: sti -> String
    def __str__(self) -> str:
        return "Converts the string value in parameter 2 into the integer variable in parameter 1 by interpreting the base 10 value represented by the string "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class stf(EXE):
    #__str__ :: stf -> String
    def __str__(self) -> str:
        return "Converts the string value in parameter 2 into the float variable in parameter 1 by interpreting the decimal value represented by the string "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class stc(EXE):
    #__str__ :: stc -> String
    def __str__(self) -> str:
        return "Converts the string value in parameter 2 into the integer variable in parameter 1 by retrieving the character code of the character at index parameter 3 (base 0) in the string "
    def __init__(self, parameter1: str, parameter2: str, parameter3: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
        
class its(EXE):
    #__str__ :: its -> String
    def __str__(self) -> str:
        return "Converts the integer value in parameter 2 into the string variable in parameter 1 by converting it into a base 10 string representation "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class itf(EXE):
    #__str__ :: itf -> String
    def __str__(self) -> str:
        return "Converts the integer value in parameter 2 into the float variable in parameter 1 using equivalence"
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class ias(EXE):
    #__str__ :: ias -> String
    def __str__(self) -> str:
        return "Converts the integer array in parameter 2 into the string variable in parameter 1 by converting each integer element of the array into a character with the character code specified by the value "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class aif(EXE):
    #__str__ :: aif -> String
    def __str__(self) -> str:
        return "Converts the integer array in parameter 2 into the float array in parameter 1 by transforming each element using equivalence "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fts(EXE):
    #__str__ :: fts -> String
    def __str__(self) -> str:
        return "Converts the float value in parameter 2 into the string variable in parameter 1 by converting it into a standard format decimal string representation "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class fti(EXE):
    #__str__ :: fti -> String
    def __str__(self) -> str:
        return "Converts the float value in parameter 2 into the integer variable in parameter 1 using equivalence "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        
class afi(EXE):
    #__str__ :: afi -> String
    def __str__(self) -> str:
        return "Converts the float array in parameter 2 into the integer array in parameter 1 by transforming each element using equivalence "
    def __init__(self, parameter1: str, parameter2: str, isInALoop : int):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
        

##################################
########## DLL Tokens ############
class DLL(Token):
    #__str__ :: DLL -> String
    def __str__(self) -> str:
        return "DLL token, Contains all extensions and specialized instructions, such as exception handling and abstract data structures"

class psh(DLL):
    #__str__ :: psh -> String
    def __str__(self) -> str:
        return "Pushes the integer value onto the stack "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class pop(DLL):
    #__str__ :: pop -> String
    def __str__(self) -> str:
        return "Set the specified integer variable to the value popped from the stack. An exception is thrown if the stack is empty."
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class spk(DLL):
    #__str__ :: spk -> String
    def __str__(self) -> str:
        return "Set the specified integer variable to the value peeked from the stack. An exception is thrown if the stack is empty. "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class ssz(DLL):
    #__str__ :: ssz -> String
    def __str__(self) -> str:
        return "Set the specified integer variable to the value of the size of the stack "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class enq(DLL):
    #__str__ :: enq -> String
    def __str__(self) -> str:
        return "Enqueues the specified integer value in the queue "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class deq(DLL):
    #__str__ :: deq -> String
    def __str__(self) -> str:
        return "Set the specified integer variable to the value dequeued from the queue. An exception is thrown if the queue is empty. "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class qpk(DLL):
    #__str__ :: qpk -> String
    def __str__(self) -> str:
        return "Set the specified integer variable to the value peeked from the queue. An exception is thrown if the queue is empty. "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class qsz(DLL):
    #__str__ :: qsz -> String
    def __str__(self) -> str:
        return "Set the specified integer variable to the value of the size of the queue "
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
class tpl(DLL):
    #__str__ :: tpl -> String
    def __str__(self) -> str:
        return "Moves the tape left "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class tpr(DLL):
    #__str__ :: tpr -> String
    def __str__(self) -> str:
        return "Moves the tape right "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class tsv(DLL):
    #__str__ :: tsv -> String
    def __str__(self) -> str:
        return "Sets the current element of the tape to the specified integer value "
    def __init__(self, parameter1: str, isInALoop : int):
        super().__init__(isInALoop)
        
        self.parameter1 = parameter1
class tgv(DLL):
    #__str__ :: tgv -> String
    def __str__(self) -> str:
        return "Sets the specified integer variable to the value of the current element of the tape "
    def __init__(self, parameter1: str, isInALoop : int):
        super().__init__(isInALoop)
        self.parameter1 = parameter1
class gbe(DLL):
    #__str__ :: gbe -> String
    def __str__(self) -> str:
        return "Changes the error handling mode to global "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class gen(DLL):
    #__str__ :: gen -> String
    def __str__(self) -> str:
        return "Turns global errors on (exception handling off) "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class gef(DLL):
    #__str__ :: gef -> String
    def __str__(self) -> str:
        return "Turns global errors off (exception handling on) "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class lce(DLL):
    #__str__ :: lce -> String
    def __str__(self) -> str:
        return "Changes the error handling mode to local "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class lcn(DLL):
    #__str__ :: lcn -> String
    def __str__(self) -> str:
        return "Turns local errors on (exception handling off) "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class lcf(DLL):
    #__str__ :: lcf -> String
    def __str__(self) -> str:
        return "Turns local errors off (exception handling on) "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        
class ges(DLL):
    #__str__ :: ges -> String
    def __str__(self) -> str:
        return "Sets the specified string variable to the error message from the last caught exception in the given scope "
    def __init__(self, parameter1 : str, isInALoop : int):
        super().__init__(isInALoop)
        
        self.parameter1 = parameter1
class ces(DLL):
    #__str__ :: ces -> String
    def __str__(self) -> str:
        return "Clears the error string in the given scope "
    def __init__(self, isInALoop : int):
        super().__init__(isInALoop)
        

##################################
########## CSV Tokens used for variables and arrays ######
class CSV(Token):
    #__str__ :: CSV -> String
    def __str__(self) -> str:
        return "CSV token, Manages, creates, and destroys variables and arrays"

class cia(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: cia -> String
    def __str__(self) -> str:
        return "Creates an integer array with the specified variable name"
class civ(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: civ -> String
    def __str__(self) -> str:
        return "Creates an integer variable with the specified variable name"
class csa(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: csa -> String
    def __str__(self) -> str:
        return "Creates a string array with the specified variable name"
class csv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: csv -> String
    def __str__(self) -> str:
        return self.parameter1 #Creates a string variable with the specified variable name
class cfa(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: cfa -> String
    def __str__(self) -> str:
        return "Creates a float array with the specified variable name"
class cfv(CSV):
    def __init__(self, parameter1: str ,isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: cfv -> String
    def __str__(self) -> str:
        return "Creates a float variable with the specified variable name"
class dia(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dia -> String
    def __str__(self) -> str:
        return "Deletes an integer array with the specified variable name"
class div_csv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: div -> String
    def __str__(self) -> str:
        return "Deletes an integer variable with the specified variable name"
class dsa(CSV):
    def __init__(self, parameter1 : str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dsa -> String
    def __str__(self) -> str:
        return "Deletes a string array with the specified variable name"
class dsv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dsv -> String
    def __str__(self) -> str:
        return "Deletes a string variable with the specified variable name"
class dfa(CSV):
    def __init__(self, parameter1:str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dfa -> String
    def __str__(self) -> str:
        return "Deletes a float array with the specified variable name"
class dfv_csv(CSV):
    def __init__(self, parameter1: str, isInALoop : int):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: dfv -> String
    def __str__(self) -> str:
        return "Deletes a float variable with the specified variable name"

##################################
########## LNK Tokens are used for function calls and the like ######
class LNK(Token):
    #__str__ :: LNK -> String
    def __str__(self) -> str:
        return "function calls and the like. Not in original Dirst added for requirement for ATP school project"

class run(LNK):#todo: add documentation and examples
    def __init__(self, functionName: str, parameterVar: str, returnVar: str ,isInALoop : int) -> None:
        self.functionName = functionName
        self.parameterVar = parameterVar
        self.returnVar = returnVar
        super().__init__(isInALoop)
        
    #__str__ :: run -> String
    def __str__(self) -> str:
        return "call function with name functionName and pass parameterVar as parameter and save result to returnVar"
    
class rtn(LNK):#todo: maybe change or remove
    def __init__(self, parameter1: str, isInALoop : int) -> None:
        self.parameter1 = parameter1
        super().__init__(isInALoop)
        
    #__str__ :: rtn -> String
    def __str__(self) -> str:
        return "return parameter 1 to function, the value of variable of parameter 1 is: " + str(self.parameter1)
    
##################################
########## ERR Tokens ############
class ERR(Token):
    def __init__(self, message: str) -> None:
        super().__init__(-1)#needed for uper class to work, but not used, because this is an error
        self.message = message
    #__str__ :: LNK -> String
    def __str__(self) -> str:
        return "Error: " + self.message
