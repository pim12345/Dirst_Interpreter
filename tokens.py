from enum import Enum
import string
from typing import NamedTuple, Union

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

########## Tokens ###############
class Token:
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

    def __str__(self):
        return "Token"
##################################
########## Directory Tokens ######
class Directory(Token):
    def __str__(self):
        return "Handles looping, conditionals and code separation"

class fnc(Directory):
    def __init__(self, varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Execute all subitems in the directory"
class dif_(Directory):
    def __init__(self, varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is not zero"
class nif(Directory):
    def __init__(self, varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is zero"
class lpc(Directory):
    def __init__(self, varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is not zero"
class lpn(Directory):
    def __init__(self, varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is zero"
class dlw(Directory):
    def __init__(self,varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
class dlu(Directory):
    def __init__(self, varname, isInALoop):
        self.varname = varname
        super().__init__(isInALoop)
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is zero (loop at least once)"
##################################
########## DAT Tokens ############
class DAT(Token):
    def __str__(self):
        return "Contains all integer functionality and logic"
class abs(DAT):
    def __str__(self):
        return "Sets parameter 1: " + str(self.parameter1) + " to the absolute value of parameter 2: " + str(self.parameter2)
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class neg(DAT):
    def __str__(self):
        return "Sets parameter 1: to the negative value of parameter 2:"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class add(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: plus parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class sub_(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: minus parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class mul(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: times parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class div(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: divided by parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class mod(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: modulo parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class and_(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: bitwise and parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class orb(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: bitwise or parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class xor(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: bitwise xor parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class xad(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: bitwise xand parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class nad(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: bitwise nand parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class nor(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of parameter 2: bitwise nor parameter 3:"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class not_(DAT):
    def __str__(self):
        return "Sets parameter 1: to the value of the bitwise not of parameter 2:"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class mor(DAT):
    def __str__(self):
        return "Sets parameter 1: to -1 if parameter 2: is greater than parameter 3:, otherwise 0"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class les(DAT):
    def __str__(self):
        return "Sets parameter 1: to -1 if parameter 2: is less than parameter 3:, otherwise 0"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class equ(DAT):
    def __str__(self):
        return "Sets parameter 1: to -1 if parameter 2: is equal to parameter 3:, otherwise 0"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class neq(DAT):
    def __str__(self):
        return "Sets parameter 1: to -1 if parameter 2: is not equal to parameter 3:, otherwise 0"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class get(DAT):
    def __str__(self):
        return "Sets parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, otherwise 0"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class let(DAT):
    def __str__(self):
        return "Sets parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, otherwise 0"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class rdi(DAT):
    def __str__(self):
        return "Reads an integer from the console and sets the specified integer variable to the value. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
class ric(DAT):
    def __str__(self):
        return "Read a character from the console and sets the specified integer variable to the value. If EOF is encountered, the variable is set to -1."
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
class dsi(DAT):
    def __str__(self):
        return "Display the specified integer value to the console"
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
class dic(DAT):
    def __str__(self):
        return "Display the character specified by the integer value to the console"
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
class set(DAT):
    def __str__(self):
        return "Sets parameter 1 to the value of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class max(DAT):
    def __str__(self):
        return "Sets parameter 1 to the higher value out of parameter 2 and parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class min(DAT):
    def __str__(self):
        return "Sets parameter 1 to the lower value out of parameter 2 and parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

##################################
########## TXT Tokens ############
class TXT(Token):
    def __str__(self):
        return "Contains all string functionality and logic as well as advanced console IO"
class rdc(TXT):
    def __str__(self):
        return "Reads a character from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class rds(TXT):
    def __str__(self):
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class eof(TXT):
    def __str__(self):
        return "Sets the given integer variable to -1 it EOF has been reached, 0 otherwise"
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
class dsc(TXT):
    def __str__(self):
        return "Displays the character from string parameter 1 at index parameter 2 (base 0) to the console"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class dss(TXT):
    def __str__(self):
        return "Displays the given string variable to the console with no newline following"
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class dsl(TXT):
    def __str__(self):
        return "Displays the given string variable to the console followed by a newline"
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class dec(TXT):
    def __str__(self):
        return "Displays the character from string parameter 1 at index parameter 2 (base 0) to STDERR"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class des(TXT):
    def __str__(self):
        return "Displays the given string variable to STDERR with no newline following"
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class del_(TXT):
    def __str__(self):
        return "Displays the given string variable to STDERR followed by a newline"
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class clr(TXT):
    def __str__(self):
        return "Clears the given string variable: " + str(self.name)
    def __init__(self, name, isInALoop):
        self.name = name
        super().__init__(isInALoop)
class cat(TXT):
    def __str__(self):
        return "Concats parameter 2 and parameter 3 and sets parameter 1 to the result"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class idx(TXT):
    def __str__(self):
        return "Set parameter 1 to the index of the first occurrence of parameter 3 in parameter 2, or -1 if not found"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class ids(TXT):
    def __str__(self):
        return "Set parameter 1 to the index of the first occurrence of parameter 3 in parameter 2 after specified index parameter 4, or -1 if not found"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class lid(TXT):
    def __str__(self):
        return "Set parameter 1 to the index of the last occurrence of parameter 3 in parameter 2, or -1 if not found"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class rep(TXT):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2, replacing every occurrence of parameter 3 with parameter 4"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class sub(TXT):
    def __str__(self):
        return "Set parameter 1 to the substring of parameter 2 from index parameter 3 (base 0) of length parameter 4"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class rmv(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 removing characters from index parameter 3 (base 0) of length parameter 4"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class ins(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 inserting substring parameter 4 at index parameter 3 (base 0)"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class tou(TXT):
    def __str__(self):
        return "Set parameter 1 to the all uppercase value of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class tol(TXT):
    def __str__(self):
        return "Set parameter 1 to the all lowercase value of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
class pdl(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 padded on the left-hand side with spaces until length parameter 3 is reached"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class cpl(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 padded on the left-hand side with the character value parameter 4 until length parameter 3 is reached"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class pdr(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 padded on the right-hand side with spaces until length parameter 3 is reached"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class cpr(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 padded on the right-hand side with the character value parameter 4 until length parameter 3 is reached"
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        super().__init__(isInALoop)
class sam(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class dif(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is not equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class hiv(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is lexicographically after parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class lov(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is lexicographically before parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class hev(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is lexicographically after or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class lev(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is lexicographically before or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class ssw(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 starts with parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class sew(TXT):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 ends with parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class trm(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 trimming all leading and trailing occurrences of the characters in parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class tms(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 trimming all leading occurrences of the characters in parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class tme(TXT):
    def __str__(self):
        return "Set parameter 1 to parameter 2 trimming all trailing occurrences of the characters in parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class ses(TXT):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

##################################
########## BIN Tokens ############
class BIN(Token):
    def __str__(self):
        return "Contains all floating point functionality and logic as well as advanced math operations"

class pls(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2 plus parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class mns(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2 minus parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)   
class tms(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2 times parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
class dvb(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2 divided by parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class pwr(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2 to the power of parameter 3"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class sgn(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the sign of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class sqr(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the square root of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class sin(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the sine of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class cos(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the cosine of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class tan(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the tangent of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class snh(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the hyperbolic sine of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class csh(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the hyperbolic cosine of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)
    
class tnh(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the hyperbolic tangent of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class cil(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the ceiling of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class flr(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the floor of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class log(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the base 10 logarithm of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class lge(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the natural logarithm of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class lbq(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the base parameter 3 logarithm of parameter 2"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class epw(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of e to the power of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class avl(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of the absolute value of parameter 2"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class rnd(BIN):
    def __str__(self):
        return "Set the given float variable to a random value between 0.0 and 1.0 inclusive"
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class rou(BIN):
    def __str__(self):
        return "Set parameter 1 to the value of parameter 2 rounded to the nearest whole number"
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class asn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class acs(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class atn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class mks(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class fmx(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class fmn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class grt(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class lst(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class eqt(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class net(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class gte(BIN):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class lte(BIN):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, 0 otherwise. Wrong in original Dirst documentation."
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class rfv(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class dfv(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

##################################
########## ZIP Tokens ############
class ZIP(Token):
    def __str__(self):
        return "Manages arrays and array values"

class giv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class siv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class gsv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

#dubblicate siv class in original documenation

class gfv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class sfv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class fia(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class zia(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class fsa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class zsa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class ffa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class zfa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

#one dubble removed
##################################
########## EXE Tokens ############
class EXE(Token):
    def __str__(self):
        return "Handles type conversion and value/array transcoding"

class sia(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class ssa(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class sti(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class stf(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class stc(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)

class its(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class itf(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class ias(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class aif(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class fts(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class fti(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

class afi(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        super().__init__(isInALoop)

##################################
########## DLL Tokens ############
class DLL(Token):
    def __str__(self):
        return "Contains all extensions and specialized instructions, such as exception handling and abstract data structures"

class psh(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class pop(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class spk(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)


class ssz(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class enq(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class deq(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class qpk(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class qsz(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)

class tpl(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class tpr(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class tsv(DLL):
    def __str__(self):
        return ""
    def __init__(self,parameter1, isInALoop):
        super().__init__(isInALoop)
        self.parameter1 = parameter1

class tgv(DLL):
    def __str__(self):
        return ""
    def __init__(self,parameter1, isInALoop):
        super().__init__(isInALoop)
        self.parameter1 = parameter1

class gbe(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class gen(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class gef(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class lce(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class lcn(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class lcf(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

class ges(DLL):
    def __str__(self):
        return ""
    def __init__(self,parameter1 ,isInALoop):
        super().__init__(isInALoop)
        self.parameter1 = parameter1

class ces(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        super().__init__(isInALoop)

##################################
########## CSV Tokens used for variables and arrays ######
class CSV(Token):
    def __str__(self):
        return "Manages, creates, and destroys variables and arrays"

class cia(CSV):
    def __str__(self):
        return "Creates an integer array with the specified variable name"
class civ(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Creates an integer variable with the specified variable name"
class csa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Creates a string array with the specified variable name"
class csv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return self.name #Creates a string variable with the specified variable name
class cfa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Creates a float array with the specified variable name"
class cfv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Creates a float variable with the specified variable name"
class dia(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Deletes an integer array with the specified variable name"
class div(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Deletes an integer variable with the specified variable name"
class dsa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Deletes a string array with the specified variable name"
class dsv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Deletes a string variable with the specified variable name"
class dfa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        super().__init__(isInALoop)
    def __str__(self):
        return "Deletes a float array with the specified variable name"
class dfv(CSV):
    def __init__(self, parameter1,isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
    def __str__(self):
        return "Deletes a float variable with the specified variable name"

##################################
########## LNK Tokens are used for function calls and the like ######
class LNK(Token):
    def __str__(self):
        return "function calls and the like. Not in orignal Dirst"

class run(LNK):
    def __init__(self, result,argument,function,isInALoop):
        self.result = result
        self.argument = argument
        self.function = function
        super().__init__(isInALoop)
    def __str__(self):
        return "run a function with 1 argument(second parameter) and save the result to first parameter. third argument is filename of function to run"

class ifrtn(LNK):
    def __init__(self, parameter1,parameter2,parameter3,isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        super().__init__(isInALoop)
    def __str__(self):
        return "return parameter3 from a function if parameter1 is equal to parameter2"

class rtn(LNK):
    def __init__(self, parameter1,isInALoop):
        self.parameter1 = parameter1
        super().__init__(isInALoop)
    def __str__(self):
        return "return parameter 1 to function."