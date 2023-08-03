import re
from typing import List, Tuple
from Lexer.tokens import *
from Tools.tools import *
import copy

#split :: String -> String
@function_debug_printing
def split(line : str) -> str:
    """Function to interpreter the Escape codes of the Dirst programming language, described also in the documentation: https://esolangs.org/wiki/Dirst#Fibonacci_Sequence#es
    +-------------+---------------+
    | Escape Code | Literal Value |
    +-------------+---------------+
    |     -u      |       ?       |
    +-------------+---------------+
    +-------------+---------------+
    |     -t      |      Tab      |
    +-------------+---------------+
    +-------------+---------------+
    |     -s      |       *       |
    +-------------+---------------+
    +-------------+---------------+
    |     -r      |Carriage Return|
    +-------------+---------------+
    +-------------+---------------+
    |     -q      |       "       |
    +-------------+---------------+
    +-------------+---------------+
    |     -p      |       |       |
    +-------------+---------------+
    +-------------+---------------+
    |     -n      |Newline/Linefeed|
    +-------------+---------------+
    +-------------+---------------+
    |     -l      |       <       |
    +-------------+---------------+
    +-------------+---------------+
    |     -g      |       >       |
    +-------------+---------------+
    +-------------+---------------+
    |     -e      |       !       |
    +-------------+---------------+
    +-------------+---------------+
    |     -d      |       _       |
    +-------------+---------------+
    +-------------+---------------+
    |     -c      |       :       |
    +-------------+---------------+
    +-------------+---------------+
    |     --      |       -       |
    +-------------+---------------+
    +-------------+---------------+
    |     -h      |       /       | this is added by this interpreter, not in original
    +-------------+---------------+

    Args:
        line (str): Line of the Dirst scripting programming language

    Returns:
        str:  String line of the Dirst programming language with interpreted Escape Codes 
    """
    newLine = line.replace('--','-')\
        .replace('-c',':')\
        .replace('-s','*')\
        .replace('-u','?')\
        .replace('-g','>')\
        .replace('-l','<')\
        .replace('-p','|')\
        .replace('-e','!')\
        .replace('-d','_')\
        .replace('-t'," ")\
        .replace('-r','\r')\
        .replace('\n',"")\
        .replace('-q','\"')\
        .replace('-h','\\')
    return re.split(r'_|\.|\t', newLine)
        
#giveCorrectClass :: [String] -> Int -> String -> Token
@function_debug_printing
def giveCorrectClass(operator : list[str], isInALoop : int, consoleInput : str) -> Token:
    """Checks with class is correct by operator and returns the correct class
       Not all classes are implemented yet.
    Args:
        operator (list): List of strings with the operators needed to return the correct class used for lexing the language
        isInALoop (int): Number of how nested the function is 
        consoleInput(string): the input given by the user, currently is given before running the function, because of constrains of side-effects of functional programming

    Returns:
        class: Returns the class associated with the operators given by given by call
    """    
    if len(operator) == 0:
        raise Exception("no instruction given")
    if len(operator) >= 7:
        raise Exception("an instruction has more or less then 7 instructions variables and file type, there is currently no instruction that has more or less then 7 instructions variables and file type")
    if len(operator[0]) > 3:
        # Instructions are three letters long, if longer the instruction is not valid
        #return ERR("an instruction is longer then 3 characters, so it is not an valid instruction")
        raise Exception("an instruction is longer then 3 characters, so it is not an valid instruction")
    elif operator[0] == "fnc" and isInALoop > 0:
        if isInALoop > 1:
            #return ERR("a function can not be called in a loop or an other function")
            raise Exception("a function can not be called in a loop or an other function")
        return fnc(operator[1], operator[2], isInALoop)
    elif operator[0] == "dif" and isInALoop > 0:
        return dif_directory(operator[1], isInALoop)
    elif operator[0] == "nif" and isInALoop > 0:
        return nif(operator[1], isInALoop)
    elif operator[0] == "lpc" and isInALoop > 0:
        return lpc(operator[1], isInALoop)
    elif operator[0] == "lpn" and isInALoop > 0:
        return lpn(operator[1], isInALoop)
    elif operator[0] == "dlw" and isInALoop > 0:
        return dlw(operator[1], isInALoop)
    elif operator[0] == "dlu" and isInALoop > 0:
        return dlu(operator[1], isInALoop)
    if operator[-1] not in Instruction_Subsets.ListValues():
        #if instruction is not an directory and not in the instruction subset enum or is missing, is it not an valid instruction, return an error
        #return ERR("instruction provided is not an valid instruction")
        raise Exception("instruction provided is not an valid instruction and not a folder instruction")

    if operator[-1] == Instruction_Subsets.DAT.value:
        if operator[0] == "abs":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for abs, only 4 arguments are allowed, including the instruction and file type")
            return abs(operator[1], operator[2], isInALoop)
        elif operator[0] == "neg":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for neg, only 4 arguments are allowed, including the instruction and file type")
            return neg(operator[1], operator[2], isInALoop)
        elif operator[0] == "add":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for add, only 5 arguments are allowed, including the instruction and file type")
            return add(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "sub":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for sub, only 5 arguments are allowed, including the instruction and file type")
            return sub_dat(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "mul":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for mul, only 5 arguments are allowed, including the instruction and file type")
            return mul(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "div":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for div, only 5 arguments are allowed, including the instruction and file type")
            return div_dat(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "mod":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for mod, only 5 arguments are allowed, including the instruction and file type")
            return mod(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "and":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for and, only 5 arguments are allowed, including the instruction and file type")
            return and_(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "orb":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for orb, only 5 arguments are allowed, including the instruction and file type")
            return orb(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "xor":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for xor, only 5 arguments are allowed, including the instruction and file type")
            return xor_dat(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "xad":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for xad, only 5 arguments are allowed, including the instruction and file type")
            return xad(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "nad":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for nad, only 5 arguments are allowed, including the instruction and file type")
            return nad(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "nor":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for nor, only 5 arguments are allowed, including the instruction and file type")
            return nor(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "not":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for not, only 4 arguments are allowed, including the instruction and file type")
            return not_(operator[1], operator[2], isInALoop)
        elif operator[0] == "mor":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for mor, only 5 arguments are allowed, including the instruction and file type")
            return mor(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "les":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for les, only 5 arguments are allowed, including the instruction and file type")
            return les(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "equ":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for equ, only 5 arguments are allowed, including the instruction and file type")
            return equ(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "neq":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for neq, only 5 arguments are allowed, including the instruction and file type")
            return neq(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "get":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for get, only 5 arguments are allowed, including the instruction and file type")
            return get(operator[1], operator[2], operator[3], isInALoop)    
        elif operator[0] == "let":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for let, only 5 arguments are allowed, including the instruction and file type")
            return let(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "rdi":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for rdi, only 3 arguments are allowed, including the instruction and file type")
            return rdi(operator[1], consoleInput, isInALoop)
        elif operator[0] == "ric":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for ric, only 3 arguments are allowed, including the instruction and file type")
            return ric(operator[1], consoleInput, isInALoop)
        elif operator[0] == "dsi":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dsi, only 3 arguments are allowed, including the instruction and file type")
            return dsi(operator[1], isInALoop)
        elif operator[0] == "dic":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dic, only 3 arguments are allowed, including the instruction and file type")
            return dic(operator[1], isInALoop)
        elif operator[0] == "set":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for set, only 5 arguments are allowed, including the instruction and file type")
            return set(operator[1], operator[2], isInALoop)
        elif operator[0] == "max":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for max, only 5 arguments are allowed, including the instruction and file type")
            return max_(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "min":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for min, only 5 arguments are allowed, including the instruction and file type")
            return min_(operator[1], operator[2], operator[3], isInALoop)
    
    elif operator[-1] == Instruction_Subsets.TXT.value:
        if operator[0] == "rdc":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for rdc, only 3 arguments are allowed, including the instruction and file type")
            return rdc(operator[1], consoleInput, isInALoop)
        elif operator[0] == "rds":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for rds, only 3 arguments are allowed, including the instruction and file type")
            return rds(operator[1], consoleInput, isInALoop) 
        elif operator[0] == "eof":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for eof, only 3 arguments are allowed, including the instruction and file type")
            return eof(operator[1], isInALoop)
        elif operator[0] == "dsc":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for dsc, only 4 arguments are allowed, including the instruction and file type")
            return dsc(operator[1], operator[2], isInALoop)
        elif operator[0] == "dss":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dss, only 3 arguments are allowed, including the instruction and file type")
            return dss(operator[1], isInALoop)
        elif operator[0] == "dsl":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dsl, only 3 arguments are allowed, including the instruction and file type")
            return dsl(operator[1], isInALoop)
        elif operator[0] == "dec":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for dec, only 4 arguments are allowed, including the instruction and file type")
            return dec(operator[1], operator[2], isInALoop)
        elif operator[0] == "des":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for des, only 3 arguments are allowed, including the instruction and file type")
            return des(operator[1], isInALoop)
        elif operator[0] == "del":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for del, only 3 arguments are allowed, including the instruction and file type")
            return del_(operator[1], isInALoop)
        elif operator[0] == "clr":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for clr, only 3 arguments are allowed, including the instruction and file type")
            return clr(operator[1], isInALoop)
        elif operator[0] == "cat":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for cat, only 5 arguments are allowed, including the instruction and file type")
            return cat(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "idx":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for idx, only 5 arguments are allowed, including the instruction and file type")
            return idx(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "ids":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for ids, only 6 arguments are allowed, including the instruction and file type")
            return ids(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "lid":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for lid, only 5 arguments are allowed, including the instruction and file type")
            return lid(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "rep":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for rep, only 6 arguments are allowed, including the instruction and file type")
            return rep(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "sub":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for sub, only 6 arguments are allowed, including the instruction and file type")
            return sub_txt(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "rmv":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for rmv, only 6 arguments are allowed, including the instruction and file type")
            return rmv(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "ins":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for ins, only 6 arguments are allowed, including the instruction and file type")
            return ins(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "tou":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for tou, only 4 arguments are allowed, including the instruction and file type")
            return tou(operator[1], operator[2], isInALoop)
        elif operator[0] == "tol":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for tol, only 4 arguments are allowed, including the instruction and file type")
            return tol(operator[1], operator[2], isInALoop)
        elif operator[0] == "pdl":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for pdl, only 5 arguments are allowed, including the instruction and file type")
            return pdl(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "cpl":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for cpl, only 6 arguments are allowed, including the instruction and file type")
            return cpl(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "pdr":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for pdr, only 5 arguments are allowed, including the instruction and file type")
            return pdr(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "cpr":
            if len(operator) != 6:
                raise Exception("more or less then 6 arguments given for cpr, only 6 arguments are allowed, including the instruction and file type")
            return cpr(operator[1], operator[2], operator[3], operator[4], isInALoop)
        elif operator[0] == "sam":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for sam, only 5 arguments are allowed, including the instruction and file type")
            return sam(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "dif":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for dif, only 5 arguments are allowed, including the instruction and file type")
            return dif_txt(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "hiv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for hiv, only 5 arguments are allowed, including the instruction and file type")
            return hiv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "lov":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for lov, only 5 arguments are allowed, including the instruction and file type")
            return lov(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "hev":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for hev, only 5 arguments are allowed, including the instruction and file type")
            return hev(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "lev":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for lev, only 5 arguments are allowed, including the instruction and file type")
            return lev(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "ssw":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for ssw, only 5 arguments are allowed, including the instruction and file type")
            return ssw(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "sew":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for sew, only 5 arguments are allowed, including the instruction and file type")
            return sew(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "trm":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for trm, only 5 arguments are allowed, including the instruction and file type")
            return trm(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "tms":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for tms, only 5 arguments are allowed, including the instruction and file type")
            return tms(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "tme":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for tme, only 5 arguments are allowed, including the instruction and file type")
            return tme(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "ses":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for ses, only 4 arguments are allowed, including the instruction and file type")
            return ses(operator[1], operator[2], isInALoop)

    elif operator[-1] == Instruction_Subsets.BIN.value:
        if operator[0] == "pls":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for pls, only 5 arguments are allowed, including the instruction and file type")
            return pls(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "mns":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for mns, only 5 arguments are allowed, including the instruction and file type")
            return mns(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "tms":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for tms, only 5 arguments are allowed, including the instruction and file type")
            return tms(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "dvb":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for dvb, only 5 arguments are allowed, including the instruction and file type")
            return dvb(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "pwr":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for pwr, only 5 arguments are allowed, including the instruction and file type")
            return pwr(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "sgn":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for sgn, only 4 arguments are allowed, including the instruction and file type")
            return sgn(operator[1], operator[2], isInALoop)
        elif operator[0] == "sqr":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for sqr, only 4 arguments are allowed, including the instruction and file type")
            return sqr(operator[1], operator[2], isInALoop)
        elif operator[0] == "sin":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for sin, only 4 arguments are allowed, including the instruction and file type")
            return sin(operator[1], operator[2], isInALoop)
        elif operator[0] == "cos":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for cos, only 4 arguments are allowed, including the instruction and file type")
            return cos(operator[1], operator[2], isInALoop)
        elif operator[0] == "tan":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for tan, only 4 arguments are allowed, including the instruction and file type")
            return tan(operator[1], operator[2], isInALoop)
        elif operator[0] == "snh":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for snh, only 4 arguments are allowed, including the instruction and file type")
            return snh(operator[1], operator[2], isInALoop)
        elif operator[0] == "csh":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for csh, only 4 arguments are allowed, including the instruction and file type")
            return csh(operator[1], operator[2], isInALoop)
        elif operator[0] == "tnh":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for tnh, only 4 arguments are allowed, including the instruction and file type")
            return tnh(operator[1], operator[2], isInALoop)
        elif operator[0] == "cil":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for cil, only 4 arguments are allowed, including the instruction and file type")
            return cil(operator[1], operator[2], isInALoop)
        elif operator[0] == "flr":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for flr, only 4 arguments are allowed, including the instruction and file type")
            return flr(operator[1], operator[2], isInALoop)
        elif operator[0] == "log":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for log, only 4 arguments are allowed, including the instruction and file type")
            return log(operator[1], operator[2], isInALoop)
        elif operator[0] == "lge":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for lge, only 4 arguments are allowed, including the instruction and file type")
            return lge(operator[1], operator[2], isInALoop)
        elif operator[0] == "lbq":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for lbq, only 5 arguments are allowed, including the instruction and file type")
            return lbq(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "epw":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for epw, only 4 arguments are allowed, including the instruction and file type")
            return epw(operator[1], operator[2], isInALoop)
        elif operator[0] == "avl":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for avl, only 4 arguments are allowed, including the instruction and file type")
            return avl(operator[1], operator[2], isInALoop)
        elif operator[0] == "rnd":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for rnd, only 3 arguments are allowed, including the instruction and file type")
            return rnd(operator[1], isInALoop)
        elif operator[0] == "rou":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for rou, only 4 arguments are allowed, including the instruction and file type")
            return rou(operator[1], operator[2], isInALoop)
        elif operator[0] == "asn":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for asn, only 4 arguments are allowed, including the instruction and file type")
            return asn(operator[1], operator[2], isInALoop)
        elif operator[0] == "acs":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for acs, only 4 arguments are allowed, including the instruction and file type")
            return acs(operator[1], operator[2], isInALoop)
        elif operator[0] == "atn":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for atn, only 4 arguments are allowed, including the instruction and file type")
            return atn(operator[1], operator[2], isInALoop)
        elif operator[0] == "mks":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for mks, only 4 arguments are allowed, including the instruction and file type")
            return mks(operator[1], operator[2], isInALoop)
        elif operator[0] == "fmx":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for fmx, only 5 arguments are allowed, including the instruction and file type")
            return fmx(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "fmn":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for fmn, only 5 arguments are allowed, including the instruction and file type")
            return fmn(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "grt":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for grt, only 5 arguments are allowed, including the instruction and file type")
            return grt(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "lst":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for lst, only 5 arguments are allowed, including the instruction and file type")
            return lst(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "eqt":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for eqt, only 5 arguments are allowed, including the instruction and file type")
            return eqt(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "net":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for net, only 5 arguments are allowed, including the instruction and file type")
            return net(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "gte":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for gte, only 5 arguments are allowed, including the instruction and file type")
            return gte(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "lte":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for lte, only 5 arguments are allowed, including the instruction and file type")
            return lte(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "rfv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for rfv, only 3 arguments are allowed, including the instruction and file type")
            return rfv(operator[1], consoleInput, isInALoop)
        elif operator[0] == "dfv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dfv, only 3 arguments are allowed, including the instruction and file type")
            return dfv_bin(operator[1], isInALoop)
    
    elif operator[-1] == Instruction_Subsets.ZIP.value:
        if operator[0] == "giv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for giv, only 5 arguments are allowed, including the instruction and file type")
            return giv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "siv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for siv, only 5 arguments are allowed, including the instruction and file type")
            return siv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "gsv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for gsv, only 5 arguments are allowed, including the instruction and file type")
            return gsv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "siv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for siv, only 5 arguments are allowed, including the instruction and file type")
            return siv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "gfv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for gfv, only 5 arguments are allowed, including the instruction and file type")
            return gfv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "sfv":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for sfv, only 5 arguments are allowed, including the instruction and file type")
            return sfv(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "fia":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for fia, only 4 arguments are allowed, including the instruction and file type")
            return fia(operator[1], operator[2], isInALoop)
        elif operator[0] == "zia":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for zia, only 4 arguments are allowed, including the instruction and file type")
            return zia(operator[1], operator[2], isInALoop)
        elif operator[0] == "fsa":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for fsa, only 4 arguments are allowed, including the instruction and file type")
            return fsa(operator[1], operator[2], isInALoop)
        elif operator[0] == "zsa":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for zsa, only 4 arguments are allowed, including the instruction and file type")
            return zsa(operator[1], operator[2], isInALoop)
        elif operator[0] == "ffa":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for ffa, only 4 arguments are allowed, including the instruction and file type")
            return ffa(operator[1], operator[2], isInALoop)
        elif operator[0] == "zfa":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for zfa, only 4 arguments are allowed, including the instruction and file type")
            return zfa(operator[1], operator[2], isInALoop)
        
    elif operator[-1] == Instruction_Subsets.EXE.value:
        if operator[0] == "sia":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for sia, only 4 arguments are allowed, including the instruction and file type")
            return sia(operator[1], operator[2], isInALoop)
        elif operator[0] == "ssa":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for ssa, only 5 arguments are allowed, including the instruction and file type")
            return ssa(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "sti":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for sti, only 4 arguments are allowed, including the instruction and file type")
            return sti(operator[1], operator[2], isInALoop)
        elif operator[0] == "stf":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for stf, only 4 arguments are allowed, including the instruction and file type")
            return stf(operator[1], operator[2], isInALoop)
        elif operator[0] == "stc":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for stc, only 5 arguments are allowed, including the instruction and file type")
            return stc(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "its":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for its, only 4 arguments are allowed, including the instruction and file type")
            return its(operator[1], operator[2], isInALoop)
        elif operator[0] == "itf":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for itf, only 4 arguments are allowed, including the instruction and file type")
            return itf(operator[1], operator[2], isInALoop)
        elif operator[0] == "ias":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for ias, only 4 arguments are allowed, including the instruction and file type")
            return ias(operator[1], operator[2], isInALoop)
        elif operator[0] == "aif":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for aif, only 4 arguments are allowed, including the instruction and file type")
            return aif(operator[1], operator[2], isInALoop)
        elif operator[0] == "fts":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for fts, only 4 arguments are allowed, including the instruction and file type")
            return fts(operator[1], operator[2], isInALoop)
        elif operator[0] == "fti":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for fti, only 4 arguments are allowed, including the instruction and file type")
            return fti(operator[1], operator[2], isInALoop)
        elif operator[0] == "afi":
            if len(operator) != 4:
                raise Exception("more or less then 4 arguments given for afi, only 4 arguments are allowed, including the instruction and file type")
            return afi(operator[1], operator[2], isInALoop)
        
    elif operator[-1] == Instruction_Subsets.DLL.value:
        if operator[0] == "psh":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for psh, only 3 arguments are allowed, including the instruction and file type")
            return psh(operator[1], isInALoop)
        elif operator[0] == "pop":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for pop, only 3 arguments are allowed, including the instruction and file type")
            return pop(operator[1], isInALoop)
        elif operator[0] == "spk":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for spk, only 3 arguments are allowed, including the instruction and file type")
            return spk(operator[1], isInALoop)
        elif operator[0] == "ssz":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for ssz, only 3 arguments are allowed, including the instruction and file type")
            return ssz(operator[1], isInALoop)
        elif operator[0] == "enq":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for enq, only 3 arguments are allowed, including the instruction and file type")
            return enq(operator[1], isInALoop)
        elif operator[0] == "deq":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for deq, only 3 arguments are allowed, including the instruction and file type")
            return deq(operator[1], isInALoop)
        elif operator[0] == "qpk":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for qpk, only 3 arguments are allowed, including the instruction and file type")
            return qpk(operator[1], isInALoop)
        elif operator[0] == "qsz":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for qsz, only 3 arguments are allowed, including the instruction and file type")
            return qsz(operator[1], isInALoop)
        elif operator[0] == "tpl":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for tpl, only 2 arguments are allowed, including the instruction and file type")
            return tpl(isInALoop)
        elif operator[0] == "tpr":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for tpr, only 2 arguments are allowed, including the instruction and file type")
            return tpr(isInALoop)
        elif operator[0] == "tsv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for tsv, only 3 arguments are allowed, including the instruction and file type")
            return tsv(operator[1], isInALoop)
        elif operator[0] == "tgv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for tgv, only 3 arguments are allowed, including the instruction and file type")
            return tgv(operator[1], isInALoop)
        elif operator[0] == "gbe":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for gbe, only 2 arguments are allowed, including the instruction and file type")
            return gbe(isInALoop)
        elif operator[0] == "gen":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for gen, only 2 arguments are allowed, including the instruction and file type")
            return gen(isInALoop)
        elif operator[0] == "gef":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for gef, only 2 arguments are allowed, including the instruction and file type")
            return gef(isInALoop)
        elif operator[0] == "lce":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for lce, only 2 arguments are allowed, including the instruction and file type")
            return lce(isInALoop)
        elif operator[0] == "lcn":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for lcn, only 2 arguments are allowed, including the instruction and file type")
            return lcn(isInALoop)
        elif operator[0] == "lcf":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for lcf, only 2 arguments are allowed, including the instruction and file type")
            return lcf(isInALoop)
        elif operator[0] == "ges":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for ges, only 3 arguments are allowed, including the instruction and file type")
            return ges(operator[1], isInALoop)
        elif operator[0] == "ces":
            if len(operator) != 2:
                raise Exception("more or less then 2 arguments given for ces, only 2 arguments are allowed, including the instruction and file type")
            return ces(isInALoop)
    
    elif operator[-1] == Instruction_Subsets.CSV.value: #complete not checked (array also extra check if good implementation)
        if operator[0] == "cia":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for cia, only 3 arguments are allowed, including the instruction and file type")
            return cia(operator[1], isInALoop)
        elif operator[0] == "civ":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for civ, only 3 arguments are allowed, including the instruction and file type")
            return civ(operator[1], isInALoop)
        elif operator[0] == "csa":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for csa, only 3 arguments are allowed, including the instruction and file type")
            return csa(operator[1], isInALoop)
        elif operator[0] == "csv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for csv, only 3 arguments are allowed, including the instruction and file type")
            return csv(operator[1], isInALoop)       
        elif operator[0] == "cfa":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for cfa, only 3 arguments are allowed, including the instruction and file type")
            return cfa(operator[1], isInALoop)
        elif operator[0] == "cfv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for cfv, only 3 arguments are allowed, including the instruction and file type")
            return cfv(operator[1], isInALoop)
        elif operator[0] == "dia":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dia, only 3 arguments are allowed, including the instruction and file type")
            return dia(operator[1], isInALoop)
        elif operator[0] == "div":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for div, only 3 arguments are allowed, including the instruction and file type")
            return div_csv(operator[1], isInALoop)
        elif operator[0] == "dsa":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dsa, only 3 arguments are allowed, including the instruction and file type")
            return dsa(operator[1], isInALoop)
        elif operator[0] == "dsv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dsv, only 3 arguments are allowed, including the instruction and file type")
            return dsv(operator[1], isInALoop)
        elif operator[0] == "dfa":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dfa, only 3 arguments are allowed, including the instruction and file type")
            return dfa(operator[1], isInALoop)
        elif operator[0] == "dfv":
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for dfv, only 3 arguments are allowed, including the instruction and file type")
            return dfv_csv(operator[1], isInALoop)
    
    elif operator[-1] == Instruction_Subsets.LNK.value:
        if operator[0] == "run":
            if len(operator) != 5:
                raise Exception("more or less then 5 arguments given for run, only 5 arguments are allowed, including the instruction and file type")
            return run(operator[1], operator[2], operator[3], isInALoop)
        elif operator[0] == "rtn":#todo check if good this and make 1 line in logic
            if len(operator) != 3:
                raise Exception("more or less then 3 arguments given for rtn, only 3 arguments are allowed, including the instruction and file type")
            return rtn(operator[1], isInALoop)
        
    #return NotImplemented()
    raise Exception("instruction provided is not a valid instruction, or is not implemented")

#recursiveInstructionClassList :: [String] -> String -> [Token]
@function_debug_printing
def recursiveInstructionClassList(argumentList: list[str], consoleInput : str) -> List[Token]:
    """Recursive function used as a map function to build up a list of all the lexed code in the Dirst programming language

    Args:
        argumentList (list): A list of lines of the scripting language of Dist

    Returns:
        list: A list of tokens of the Dirst scripting language
    """    
    newArgumentList = copy.deepcopy(argumentList)
    isInALoop = newArgumentList[0].count("")
    if newArgumentList[0][0] == "":
        newArgumentList[0] = list(filter(lambda str: (str != "") ,newArgumentList[0]))
    if len(newArgumentList) == 1:
        return [giveCorrectClass(newArgumentList[0], isInALoop, consoleInput)]
    else:
        return [giveCorrectClass(newArgumentList[0], isInALoop, consoleInput)] + recursiveInstructionClassList(newArgumentList[1:], consoleInput)

#lex :: [String] -> String -> [Token]
@function_debug_printing
def lex(file : list[str], consoleInput : str) -> List[Token]:
    """Function that lex the given file

    Args:
        file (list): A text file according to the Dist scripting language
        consoleInput (str): The input given by the user, currently is given before running the function, because of constrains of side-effects of functional programming, the downside of this is that is is only possible to give 1 input for the whole program

    Returns:
        list: A list with all the tokens of the Dirst scripting language
    """    
    return recursiveInstructionClassList(list(map(split,file)), consoleInput)