import re
from typing import List, Tuple
from tokens import *

def split(line : str):
    """Function to interpreter the Escape codes of the Dirst programming language
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

    Args:
        line (str): Line of the Dirst scripting programming language

    Returns:
        str:  String line of the Dirst programming language with intpreterd Escape Codes 
    """    
    line = line.replace('--','-')
    line = line.replace('-c',':')
    line = line.replace('-s','*')
    line = line.replace('-u','?')
    line = line.replace('-g','>')
    line = line.replace('-l','<')
    line = line.replace('-p','|')
    line = line.replace('-e','!')
    line = line.replace('-d','_')
    line = line.replace('-t'," ")
    line = line.replace('-r','\r')
    line = line.replace('\n',"") #remove newline from string.
    line = line.replace('-q','\"')
    return re.split(r'_|\.|\t', line)
    

def giveCorrectClass(operator : list, isInALoop : int):
    """Checks with class is correct by operator and returns the correct class

    Args:
        operator (list): List of strings with the operators needed to return the correct class used for lexing the language
        isInALoop (int): Number of how nested the function is 

    Returns:
        class: Returns the class assosiated with the operators given by given by call
    """    
    match operator:
        #DIRECTORY
        case ["fnc",operator1] if isInALoop > 0:
            return fnc(operator1, isInALoop)
        case ["dif", operator1] if isInALoop > 0:
            return dif_(operator1, isInALoop)
        case ["nif", operator1] if isInALoop > 0:
            return nif(operator1, isInALoop)
        case ["lpc", operator1] if isInALoop > 0:
            return lpc(operator1, isInALoop)
        case ["lpn", operator1] if isInALoop > 0:
            return lpn(operator1, isInALoop)
        case ["dlw", operator1] if isInALoop > 0:
            return dlw(operator1, isInALoop)
        case ["dlu", operator1] if isInALoop > 0:
            return dlu(operator1, isInALoop)
        #DAT
        case ["abs", operator1,operator2,Instruction_Subsets.DAT.value]:
            return abs(operator1,operator2,isInALoop)
        case ["neg", operator1,operator2,Instruction_Subsets.DAT.value]:
            return neg(operator1,operator2,isInALoop)
        case ["add", operator1,operator2,operator3,Instruction_Subsets.DAT.value]:
            return add(operator1,operator2,operator3,isInALoop)
        #case ["", operator1,operator2,Instruction_Subsets.DAT.value]:
        #    return (operator1,operator2,isInALoop)
        #case ["", operator1,operator2,operator3,Instruction_Subsets.DAT.value]:
        #    return (operator1,operator2,operator3,isInALoop)
    if operator[-1] == Instruction_Subsets.DAT.value:
        if operator[0] == "abs":
            return abs(operator[1],operator[2],isInALoop)
        elif operator[0] == "neg":
            return neg(operator[1],operator[2],isInALoop)
        elif operator[0] == "add":
            return add(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "sub":
            return sub_(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "mul":
            return mul(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "div":
            return div(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "mod":
            return mod(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "and":
            return and_(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "orb":
            return orb(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "xor":
            return xor(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "xad":
            return xad(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "nad":
            return nad(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "nor":
            return nor(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "not":
            return not_(operator[1],operator[2],isInALoop)
        elif operator[0] == "mor":
            return mor(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "les":
            return les(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "equ":
            return equ(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "neq":
            return neq(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "gets":
            return get(operator[1],operator[2],operator[3],isInALoop)    
        elif operator[0] == "let":
            return let(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "rdi":
            return rdi(operator[1],isInALoop)
        elif operator[0] == "ric":
            return ric(operator[1],isInALoop)
        elif operator[0] == "dsi":
            return dsi(operator[1],isInALoop)
        elif operator[0] == "dic":
            return dic(operator[1],isInALoop)
        elif operator[0] == "dic":
            return dic(operator[1],isInALoop)
        elif operator[0] == "set":
            return set(operator[1],operator[2],isInALoop)
        elif operator[0] == "max":
            return max(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "min":
            return min(operator[1],operator[2],operator[3],isInALoop)
    
    elif operator[-1] == Instruction_Subsets.TXT.value:
        if operator[0] == "rdc":
            return rdc(operator[1],isInALoop)
        elif operator[0] == "rds":
            return rds(operator[1],isInALoop) 
        elif operator[0] == "eof":
            return eof(operator[1],isInALoop)
        elif operator[0] == "dsc":
            return dsc(operator[1],operator[2],isInALoop)
        elif operator[0] == "dss":
           return dss(operator[1],isInALoop)
        elif operator[0] == "dsl":
           return dsl(operator[1],isInALoop)
        elif operator[0] == "dec":
           return dec(operator[1],operator[2],isInALoop)
        elif operator[0] == "des":
           return des(operator[1],isInALoop)
        elif operator[0] == "del":
           return del_(operator[1],isInALoop)
        elif operator[0] == "clr":
           return clr(operator[1],isInALoop)
        elif operator[0] == "cat":
           return cat(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "idx":
           return idx(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "ids":
           return ids(operator[1],operator[2],operator[3],operator[4],isInALoop)

    elif operator[-1] == Instruction_Subsets.CSV.value:
        if operator[0] == "csv":
            return csv(operator[1],isInALoop)       
        elif operator[0] == "civ":
            return civ(operator[1],isInALoop)
        elif operator[0] == "dsv":
            return dsv(operator[1],isInALoop)
        elif operator[0] == "div":
            return div(operator[1],isInALoop)
        elif operator[0] == "cfv":
            return cfv(operator[1],isInALoop)
        elif operator[0] == "dfv":
            return dfv(operator[1],isInALoop)
    elif operator[-1] == Instruction_Subsets.EXE.value:
        if operator[0] == "itf":
            return itf(operator[1], operator[2], isInALoop)
        elif operator[0] == "fti":
            return fti(operator[1], operator[2], isInALoop)
    elif operator[-1] == Instruction_Subsets.BIN.value:
        if operator[0] == "pwr":
            return pwr(operator[1], operator[2],operator[3], isInALoop)
        elif operator[0] == "dfv":
            return dfv(operator[1],isInALoop)
        elif operator[0] == "gte":
            return gte(operator[1], operator[2],operator[3], isInALoop)
    elif operator[-1] == Instruction_Subsets.LNK.value:
        if operator[0] == "run":
            return run(operator[1], operator[2],operator[3], isInALoop)
        elif operator[0] == "ifrtn":
            return ifrtn(operator[1], operator[2],operator[3], isInALoop)
        elif operator[0] == "rtn":
            return rtn(operator[1],isInALoop)
    return NotImplemented()


def recursiveInstructionClassList(argumentlist : list):
    """Recursive function used as a map function to build up a list of all the lexed code in the Dirst programming language

    Args:
        argumentlist (list): A list of lines of the scripting language of Dist

    Returns:
        list: A list of lexed classes of Dirst
    """    
    #isInALoop = 0
    isInALoop = argumentlist[0].count("")
    #print("inrecursive fun: ", argumentlist[0], "space: ", argumentlist[0].count(""), "test" )
    if argumentlist[0][0] == "":
        #print(argumentlist[0].count(""))
        #isInALoop = argumentlist[0].count("")
        #print(argumentlist[0])
        argumentlist[0] = list(filter(lambda str: (str != "") ,argumentlist[0]))
        #print(argumentlist[0])
       
        #del argumentlist[0][0]#remove tab from list and put a boolian expression in the place. only support for one loop
    if len(argumentlist) == 1:
        return [giveCorrectClass(argumentlist[0], isInALoop)]
    else:
        return [giveCorrectClass(argumentlist[0], isInALoop)] + recursiveInstructionClassList(argumentlist[1:])


def lex(file : list):
    """Function that lex the given file

    Args:
        file (list): A text file according to the Dist scripting language

    Returns:
        list: A list with all the correct classes and parameters(lexed of the Dirst scripting language)
    """    
    return recursiveInstructionClassList(list(map(split,file)))