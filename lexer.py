import re
from typing import List, Tuple
from tokens import *

def split(line):
    line = line.replace('\n',"") #remove newline from string.
    line = line.replace('-c',':')
    line = line.replace('-s','*')
    line = line.replace('-u','?')
    line = line.replace('-g','>')
    line = line.replace('-l','<')
    line = line.replace('-p','|')
    line = line.replace('-e','!')
    #line = line.replace('-d','_')
    #line = line.replace('-t'," ")
    #line = line.replace('-r','\r')
    #line = line.replace('-n','\n')
    #line = line.replace('-q','\"')
    line = line.replace('--','-')
    #print(re.split(r'([\t\._])', line))#met de punten en _ in de lijst 
    #print(re.split(r'_|\.|\t', line))#zonder punten en _ in de lijst
    return re.split(r'_|\.|\t', line)
    

def giveCorrectClass(operator, isInALoop):
    if isInALoop > 0:
        #removed \t a stap back
        if operator[0] == "fnc":
            return fnc(operator[1], isInALoop)
        if operator[0] == "dif":
            return dif_(operator[1], isInALoop)
        if operator[0] == "nif":
            return nif(operator[1], isInALoop)
        if operator[0] == "lpc":
            return lpc(operator[1], isInALoop)
        if operator[0] == "lpn":
            return lpn(operator[1], isInALoop)
        if operator[0] == "dlw":
            return dlw(operator[1], isInALoop)
        if operator[0] == "dlu":
            return dlu(operator[1], isInALoop)

    if operator[-1] == Instruction_Subsets.DAT.value:
        if operator[0] == "abs":
            return abs(operator[1],operator[2],isInALoop)
        if operator[0] == "neg":
            return neg(operator[1],operator[2],isInALoop)
        if operator[0] == "add":
            return add(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "sub":
            return sub_(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "mul":
            return mul(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "div":
            return div(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "mod":
            return mod(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "and":
            return and_(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "orb":
            return orb(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "xor":
            return xor(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "xad":
            return xad(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "nad":
            return nad(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "nor":
            return nor(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "not":
            return not_(operator[1],operator[2],isInALoop)
        if operator[0] == "mor":
            return mor(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "les":
            return les(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "equ":
            return equ(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "neq":
            return neq(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "gets":
            return get(operator[1],operator[2],operator[3],isInALoop)    
        if operator[0] == "let":
            return let(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "rdi":
            return rdi(operator[1],isInALoop)
        if operator[0] == "ric":
            return (operator[1],isInALoop)
        if operator[0] == "dsi":
            return dsi(operator[1],isInALoop)
        if operator[0] == "dic":
            return dic(operator[1],isInALoop)
        if operator[0] == "dic":
            return dic(operator[1],isInALoop)
        if operator[0] == "set":
            return set(operator[1],operator[2],isInALoop)
        if operator[0] == "max":
            return max(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "min":
            return min(operator[1],operator[2],operator[3],isInALoop)
    
    if operator[-1] == Instruction_Subsets.TXT.value:
        if operator[0] == "rdc":
            return rdc(operator[1],isInALoop)
        if operator[0] == "rds":
            return rds(operator[1],isInALoop) 
        if operator[0] == "eof":
            return eof(operator[1],isInALoop)
        if operator[0] == "dsc":
            return dsc(operator[1],operator[2],isInALoop)
        if operator[0] == "dss":
           return dss(operator[1],isInALoop)
        if operator[0] == "dsl":
           return dsl(operator[1],isInALoop)
        if operator[0] == "dec":
           return dec(operator[1],operator[2],isInALoop)
        if operator[0] == "des":
           return des(operator[1],isInALoop)
        if operator[0] == "del":
           return del_(operator[1],isInALoop)
        if operator[0] == "clr":
           return clr(operator[1],isInALoop)
        if operator[0] == "cat":
           return cat(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "idx":
           return idx(operator[1],operator[2],operator[3],isInALoop)
        if operator[0] == "ids":
           return ids(operator[1],operator[2],operator[3],operator[4],isInALoop)

    if operator[-1] == Instruction_Subsets.CSV.value:#
        if operator[0] == "csv":
            return csv(operator[1],isInALoop)       
        if operator[0] == "civ":
            return civ(operator[1],isInALoop)
        if operator[0] == "dsv":
            return dsv(operator[1],isInALoop)
        if operator[0] == "div":
            return div(operator[1],isInALoop)
        if operator[0] == "cfv":
            return cfv(operator[1],isInALoop)


def recursiveInstructionClassList(argumentlist):
    isInALoop = 0
    if argumentlist[0][0] == "":
        #print(argumentlist[0].count(""))
        isInALoop = argumentlist[0].count("")
        #print(argumentlist[0])
        argumentlist[0] = list(filter(lambda str: (str != "") ,argumentlist[0]))
        #print(argumentlist[0])
       
        #del argumentlist[0][0]#remove tab from list and put a boolian expression in the place. only support for one loop
    if len(argumentlist) == 1:
        return [giveCorrectClass(argumentlist[0], isInALoop)]
    else:
        return [giveCorrectClass(argumentlist[0], isInALoop)] + recursiveInstructionClassList(argumentlist[1:])


def lex(file):
    argument_list = map(split,file)
    #print(token_ouput_list)
    return recursiveInstructionClassList(list(argument_list))