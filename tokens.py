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
    def __init__(self, isInALoop=0):
        self.isInALoop = isInALoop
        self.test = 0

    def __str__(self):
        return "Token"
##################################
########## Directory Tokens ######
class Directory(Token):
    def __str__(self):
        return "Looping"

class fnc(Directory):
    def __init__(self, value, isInALoop):
        self.isInALoop = isInALoop
        self.value = value
    def __str__(self):
        return "Execute all subitems in the directory"
class dif_(Directory):
    def __init__(self, value, isInALoop):
        self.isInALoop = isInALoop
        self.value = value
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is not zero"
class nif(Directory):
    def __init__(self, value, isInALoop):
        self.isInALoop = isInALoop
        self.value = value
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is zero"
class lpc(Directory):
    def __init__(self, value, isInALoop):
        self.isInALoop = isInALoop
        self.value = value
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is not zero"
class lpn(Directory):
    def __init__(self, value, isInALoop):
        self.isInALoop = isInALoop
        self.value = value
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is zero"
class dlw(Directory):
    def __init__(self,varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
class dlu(Directory):
    def __init__(self, value, isInALoop):
        self.isInALoop = isInALoop
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
class les(DAT):
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
        self.isInALoop = isInALoop
class rds(TXT):
    def __str__(self):
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class eof(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class dsc(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class dss(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class dsl(TXT):
    def __str__(self):
        return ""
    def __init__(self, name, isInALoop):
        self.name = name
        self.isInALoop = isInALoop
class dec(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class des(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class del_(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class clr(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
class cat(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class idx(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class ids(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class lid(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class rep(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class sub(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class rmv(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class ins(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class tou(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class tol(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
class pdl(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class cpl(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class pdr(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class cpr(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, parameter4, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.parameter4 = parameter4
        self.isInALoop = isInALoop
class sam(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class dif(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class hiv(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class lov(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class hev(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class lev(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class ssw(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class sew(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class trm(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class tms(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class tme(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
class ses(TXT):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

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
class CSV(Token):
    def __str__(self):
        return "Manages, creates, and destroys variables and arrays"

class cia(CSV):
    def __str__(self):
        return "Creates an integer array with the specified variable name"
class civ(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates an integer variable with the specified variable name"
class csa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates a string array with the specified variable name"
class csv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return self.name #Creates a string variable with the specified variable name
class cfa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates a float array with the specified variable name"
class cfv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Creates a float variable with the specified variable name"
class dia(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes an integer array with the specified variable name"
class div(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes an integer variable with the specified variable name"
class dsa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a string array with the specified variable name"
class dsv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a string variable with the specified variable name"
class dfa(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a float array with the specified variable name"
class dfv(CSV):
    def __init__(self, name,isInALoop):
        self.name = name
        self.isInALoop = isInALoop
    def __str__(self):
        return "Deletes a float variable with the specified variable name"