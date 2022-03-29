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
    def __init__(self, isInALoop=0):
        self.isInALoop = isInALoop

    def __str__(self):
        return "Token"
##################################
########## Directory Tokens ######
class Directory(Token):
    def __str__(self):
        return "Looping"

class fnc(Directory):
    def __init__(self, varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Execute all subitems in the directory"

class fncT(NamedTuple):
    isInALoop: bool
    varName: str
class difT(NamedTuple):
    isInALoop: bool
    varName: str
class nifT(NamedTuple):
    isInALoop: bool
    varName: str
class lpcT(NamedTuple):
    isInALoop: bool
    varName: str
class lpnT(NamedTuple):
    isInALoop: bool
    varName: str
class dlwT(NamedTuple):
    isInALoop: bool
    varName: str
class dluT(NamedTuple):
    isInALoop: bool
    varName: str

directoryUnion = Union[fncT, difT, nifT, lpcT, lpnT, dlwT, dluT]

class dif_(Directory):
    def __init__(self, varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is not zero"
class nif(Directory):
    def __init__(self, varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Execute directory subitems only if the specified integer value is zero"
class lpc(Directory):
    def __init__(self, varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is not zero"
class lpn(Directory):
    def __init__(self, varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Loop through directory subitems while the specified integer value is zero"
class dlw(Directory):
    def __init__(self,varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
    def __str__(self):
        return "Do loop through directory subitems while the specified integer value is not zero (loop at least once)"
class dlu(Directory):
    def __init__(self, varname, isInALoop):
        self.isInALoop = isInALoop
        self.varname = varname
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
        return "neq classe"
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
        return "ric classe"
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
    def __init__(self, name, isInALoop):
        self.name = name
        self.isInALoop = isInALoop
class rds(TXT):
    def __str__(self):
        return "Reads a line from the console and appends to the specified string. If EOF is encountered, the variable is not modified and EOF is marked."
    def __init__(self, name, isInALoop):
        self.name = name
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
        return "dss classe"
    def __init__(self, name, isInALoop):
        self.name = name
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
    def __init__(self, name, isInALoop):
        self.name = name
        self.isInALoop = isInALoop
class del_(TXT):
    def __str__(self):
        return ""
    def __init__(self, name, isInALoop):
        self.name = name
        self.isInALoop = isInALoop
class clr(TXT):
    def __str__(self):
        return ""
    def __init__(self, name, isInALoop):
        self.name = name
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
        return "sub classe"
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
        return "Contains all floating point functionality and logic as well as advanced math operations"

class pls(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class mns(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
        
class tms(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class dvb(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class pwr(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class sgn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class sqr(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class sin(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class cos(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class tan(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class snh(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class csh(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop
    
class tnh(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class cil(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class flr(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class log(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class lge(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class lbq(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class epw(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class avl(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class rnd(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class rou(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class asn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class acs(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class atn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class mks(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class fmx(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class fmn(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class grt(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class lst(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class eqt(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class net(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class gte(BIN):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is greater than or equal to parameter 3, 0 otherwise"
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class lte(BIN):
    def __str__(self):
        return "Set parameter 1 to -1 if parameter 2 is less than or equal to parameter 3, 0 otherwise. Wrong in original Dirst documentation."
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class rfv(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class dfv(BIN):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

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
        self.isInALoop = isInALoop

class siv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class gsv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

#dubblicate siv class in original documenation

class gfv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class sfv(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class fia(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class zia(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class fsa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class zsa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class ffa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class zfa(ZIP):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

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
        self.isInALoop = isInALoop

class ssa(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class sti(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class stf(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class stc(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, parameter3, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop

class its(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class itf(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class ias(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class aif(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class fts(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class fti(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

class afi(EXE):
    def __str__(self):
        return ""
    def __init__(self, parameter1, parameter2, isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.isInALoop = isInALoop

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
        self.isInALoop = isInALoop

class pop(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class spk(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop


class ssz(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class enq(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class deq(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class qpk(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class qsz(DLL):
    def __str__(self):
        return ""
    def __init__(self, parameter1, isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop

class tpl(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class tpr(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class tsv(DLL):
    def __str__(self):
        return ""
    def __init__(self,parameter1, isInALoop):
        self.isInALoop = isInALoop
        self.parameter1 = parameter1

class tgv(DLL):
    def __str__(self):
        return ""
    def __init__(self,parameter1, isInALoop):
        self.isInALoop = isInALoop
        self.parameter1 = parameter1

class gbe(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class gen(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class gef(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class lce(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class lcn(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class lcf(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

class ges(DLL):
    def __str__(self):
        return ""
    def __init__(self,parameter1 ,isInALoop):
        self.isInALoop = isInALoop
        self.parameter1 = parameter1

class ces(DLL):
    def __str__(self):
        return ""
    def __init__(self, isInALoop):
        self.isInALoop = isInALoop

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
    def __init__(self, parameter1,isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
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
        self.isInALoop = isInALoop
    def __str__(self):
        return "run a function with 1 argument(second parameter) and save the result to first parameter. third argument is filename of function to run"

class ifrtn(LNK):
    def __init__(self, parameter1,parameter2,parameter3,isInALoop):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        self.isInALoop = isInALoop
    def __str__(self):
        return "return parameter3 from a function if parameter1 is equal to parameter2"

class rtn(LNK):
    def __init__(self, parameter1,isInALoop):
        self.parameter1 = parameter1
        self.isInALoop = isInALoop
    def __str__(self):
        return "return parameter 1 to function."