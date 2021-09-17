from enum import Enum

class Instruction_Subsets(Enum):
    DAT = "dat"
    TXT = "txt"
    BIN = "bin"
    ZIP = "zip"
    EXE = "exe"
    DLL = "dll"
    CSV = 'csv'
    DIRECTORY = ""

########## Tokens ###############
class Token:
    def __init__(self):
        self.test = 0

    def __str__(self):
        return "Token"
##################################
########## Directory Tokens ######
class Directory(Token):
    def __str__(self):
        return "Looping"

class fnc(Directory):
    def __init__(self, type):
        type.name = type
    def __str__(self):
        return "Execute all subitems in the directory"
class dif(Directory):
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is not zero"
class nif(Directory):
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is zero"
class lpc(Directory):
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is not zero"
class lpn(Directory):
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is zero"
class dlw(Directory):
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
class dlu(Directory):
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is zero (loop at least once)"
##################################
########## CSV Tokens used for variables and arrays ######
class Csv(Token):
    def __str__(self):
        return "Manages, creates, and destroys variables and arrays"

class cia(Csv):
    def __str__(self):
        return "Creates an integer array with the specified variable name"
class civ(Csv):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Creates an integer variable with the specified variable name"
class csa(Csv):
    def __str__(self):
        return "Creates a string array with the specified variable name"
class csv(Csv):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name #Creates a string variable with the specified variable name
class cfa(Csv):
    def __str__(self):
        return "Creates a float array with the specified variable name"
class cfv(Csv):
    def __str__(self):
        return "Creates a float variable with the specified variable name"
class dia(Csv):
    def __str__(self):
        return "Deletes an integer array with the specified variable name"
class div(Csv):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Deletes an integer variable with the specified variable name"
class dsa(Csv):
    def __str__(self):
        return "Deletes a string array with the specified variable name"
class dsv(Csv):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Deletes a string variable with the specified variable name"
class dfa(Csv):
    def __str__(self):
        return "Deletes a float array with the specified variable name"
class dfv(Csv):
    def __str__(self):
        return "Deletes a float variable with the specified variable name"
##################################
########## DAT Tokens ############
class DAT(Token):
    def __str__(self):
        return ""
    
class set(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2



##################################
########## TXT Tokens ############
class TXT(Token):
    def __str__(self):
        return "Contains all string functionality and logic as well as advanced console IO"

class dss(TXT):
    def __str__(self):
        return "Displays the given string variable to the console with no newline following"
    def __init__(self, name):
        self.name = name

class rds(TXT):
    def __str__(self):
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, name):
        self.name = name
    