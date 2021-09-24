from enum import Enum


#nog toevoegen __repr__ ook toevoegen denk i.p.v __str__
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
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Execute all subitems in the directory"
class dif_(Directory):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is not zero"
class nif(Directory):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is zero"
class lpc(Directory):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is not zero"
class lpn(Directory):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is zero"
class dlw(Directory):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
class dlu(Directory):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is zero (loop at least once)"
##################################
########## DAT Tokens ############
class DAT(Token):
    def __str__(self):
        return ""
class abs(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class neg(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class add(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class sub_(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class mul(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class div(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class mod(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class and_(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class orb(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class xor(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class xad(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class nad(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class nor(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class not_(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class mor(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class less(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class equ(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class neq(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class get(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class let(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class rdi(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class ric(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class dsi(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class dic(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class set(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class max(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class min(DAT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

##################################
########## TXT Tokens ############
class TXT(Token):
    def __str__(self):
        return "Contains all string functionality and logic as well as advanced console IO"
class rdc(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class rds(TXT):
    def __str__(self):
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class eof(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class dsc(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInAloop = isInALoop
class dss(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class dsl(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class dec(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInAloop = isInALoop
class des(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class del_(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class clr(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInAloop = isInALoop
class cat(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class idx(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class ids(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class lid(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class rep(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class sub(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class rmv(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class ins(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class tou(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInAloop = isInALoop
class tol(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInAloop = isInALoop
class pdl(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class cpl(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class pdr(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class cpr(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInAloop = isInALoop
class sam(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class dif(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class hiv(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class lov(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class hev(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class lev(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class ssw(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class sew(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class trm(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class tms(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class tme(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInAloop = isInALoop
class ses(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInAloop = isInALoop

##################################
########## BIN Tokens ############
class BIN(Token):
    def __str__(self):
        return ""

##################################
########## ZIP Tokens ############
class ZIP(Token):
    def __str__(self):
        return ""

##################################
########## EXE Tokens ############
class EXE(Token):
    def __str__(self):
        return ""

##################################
########## DLL Tokens ############
class DLL(Token):
    def __str__(self):
        return ""

##################################
########## CSV Tokens used for variables and arrays ######
class Csv(Token):
    def __str__(self):
        return "Manages, creates, and destroys variables and arrays"

class cia(Csv):
    def __str__(self):
        return "Creates an integer array with the specified variable name"
class civ(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates an integer variable with the specified variable name"
class csa(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates a string array with the specified variable name"
class csv(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return self.name #Creates a string variable with the specified variable name
class cfa(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates a float array with the specified variable name"
class cfv(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates a float variable with the specified variable name"
class dia(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes an integer array with the specified variable name"
class div(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes an integer variable with the specified variable name"
class dsa(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a string array with the specified variable name"
class dsv(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a string variable with the specified variable name"
class dfa(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a float array with the specified variable name"
class dfv(Csv):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a float variable with the specified variable name"