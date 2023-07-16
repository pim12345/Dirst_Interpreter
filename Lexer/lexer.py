import re
from typing import List, Tuple
from Lexer.tokens import *

#split :: String -> String
def split(line : str) -> str:
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
    +-------------+---------------+
    |     -h      |       /       | this is added by this interpreter, not in original
    +-------------+---------------+

    Args:
        line (str): Line of the Dirst scripting programming language

    Returns:
        str:  String line of the Dirst programming language with interpreted Escape Codes 
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
    line = line.replace('-h','\\')
    return re.split(r'_|\.|\t', line)
    
#giveCorrectClass :: list[String] -> Token
def giveCorrectClass(operator : list[str], isInALoop : int, consoleInput : str) -> Token:
    """Checks with class is correct by operator and returns the correct class
       Not all classes are implemented yet.
    Args:
        operator (list): List of strings with the operators needed to return the correct class used for lexing the language
        isInALoop (int): Number of how nested the function is 

    Returns:
        class: Returns the class associated with the operators given by given by call
    """    
    if len(operator[0]) > 3:
        # Instructions are three letters long, if longer the instruction is not valid
        return ERR("an instruction is longer then 3 characters, so it is not an valid instruction")
    elif operator[0] == "fnc" and isInALoop > 0:
        return fnc(operator[1],operator[2], isInALoop)
    elif operator[0] == "dif" and isInALoop > 0:
        return dif_(operator[1], isInALoop)
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
        return ERR("instruction provided is not an valid instruction")
    if operator[-1] == Instruction_Subsets.DAT.value: #complete
        if operator[0] == "abs":
            return abs(operator[1],operator[2],isInALoop)
        elif operator[0] == "neg":
            return neg(operator[1],operator[2],isInALoop)
        elif operator[0] == "add":
            return add(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "sub":
            return sub_dat(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "mul":
            return mul(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "div":
            return div_dat(operator[1],operator[2],operator[3],isInALoop)
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
        elif operator[0] == "get":
            return get(operator[1],operator[2],operator[3],isInALoop)    
        elif operator[0] == "let":
            return let(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "rdi":
            return rdi(operator[1],consoleInput, isInALoop)
        elif operator[0] == "ric":
            return ric(operator[1],consoleInput, isInALoop)
        elif operator[0] == "dsi":
            return dsi(operator[1],isInALoop)
        elif operator[0] == "dic":
            return dic(operator[1],isInALoop)
        elif operator[0] == "dic":
            return dic(operator[1],isInALoop)
        elif operator[0] == "set":
            return set(operator[1],operator[2],isInALoop)
        elif operator[0] == "max":
            return max_(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "min":
            return min_(operator[1],operator[2],operator[3],isInALoop)
    
    elif operator[-1] == Instruction_Subsets.TXT.value: #complete not checked
        if operator[0] == "rdc":
            return rdc(operator[1],consoleInput,isInALoop)
        elif operator[0] == "rds":
            return rds(operator[1],consoleInput,isInALoop) 
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
           return ids(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "lid":
           return lid(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "rep":
           return rep(operator[1],operator[2],operator[3],operator[4],isInALoop)
        elif operator[0] == "sub":
           return sub_txt(operator[1],operator[2],operator[3],operator[4],isInALoop)
        elif operator[0] == "rmv":
           return rmv(operator[1],operator[2],operator[3],operator[4],isInALoop)
        elif operator[0] == "ins":
           return ins(operator[1],operator[2],operator[3],operator[4],isInALoop)
        elif operator[0] == "tou":
           return tou(operator[1],operator[2],isInALoop)
        elif operator[0] == "tol":
           return tol(operator[1],operator[2],isInALoop)
        elif operator[0] == "pdl":
           return pdl(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "cpl":
           return cpl(operator[1],operator[2],operator[3],operator[4],isInALoop)
        elif operator[0] == "pdr":
           return pdr(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "cpr":
           return cpr(operator[1],operator[2],operator[3],operator[4],isInALoop)
        elif operator[0] == "sam":
           return sam(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "dif":
           return dif(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "hiv":
           return hiv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "lov":
           return lov(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "hev":
           return hev(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "lev":
           return lev(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "ssw":
           return ssw(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "sew":
           return sew(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "trm":
           return trm(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "tms":
           return tms(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "tme":
           return tme(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "ses":
           return ses(operator[1],operator[2],isInALoop)

    elif operator[-1] == Instruction_Subsets.BIN.value:
        if operator[0] == "pls":
            return pls(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "mns":
            return mns(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "tms":
            return tms(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "dvb":
            return dvb(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "pwr":
            return pwr(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "sgn":
            return sgn(operator[1],operator[2],isInALoop)
        elif operator[0] == "sqr":
            return sqr(operator[1],operator[2],isInALoop)
        elif operator[0] == "sin":
            return sin(operator[1],operator[2],isInALoop)
        elif operator[0] == "cos":
            return cos(operator[1],operator[2],isInALoop)
        elif operator[0] == "tan":
            return tan(operator[1],operator[2],isInALoop)
        elif operator[0] == "snh":
            return snh(operator[1],operator[2],isInALoop)
        elif operator[0] == "csh":
            return csh(operator[1],operator[2],isInALoop)
        elif operator[0] == "tnh":
            return tnh(operator[1],operator[2],isInALoop)
        elif operator[0] == "cil":
            return cil(operator[1],operator[2],isInALoop)
        elif operator[0] == "flr":
            return flr(operator[1],operator[2],isInALoop)
        elif operator[0] == "log":
            return log(operator[1],operator[2],isInALoop)
        elif operator[0] == "lge":
            return lge(operator[1],operator[2],isInALoop)
        elif operator[0] == "lbq":
            return lbq(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "epw":
            return epw(operator[1],operator[2],isInALoop)
        elif operator[0] == "avl":
            return avl(operator[1],operator[2],isInALoop)
        elif operator[0] == "rnd":
            return rnd(operator[1],isInALoop)
        elif operator[0] == "rou":
            return rou(operator[1],operator[2],isInALoop)
        elif operator[0] == "asn":
            return asn(operator[1],operator[2],isInALoop)
        elif operator[0] == "acs":
            return acs(operator[1],operator[2],isInALoop)
        elif operator[0] == "atn":
            return atn(operator[1],operator[2],isInALoop)
        elif operator[0] == "mks":
            return mks(operator[1],operator[2],isInALoop)
        elif operator[0] == "fmx":
            return fmx(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "fmn":
            return fmn(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "grt":
            return grt(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "lst":
            return lst(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "eqt":
            return eqt(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "net":
            return net(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "gte":
            return gte(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "lte":
            return lte(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "rfv":
            return rfv(operator[1],consoleInput ,isInALoop)
        elif operator[0] == "dfv":
            return dfv_bin(operator[1],isInALoop)
    
    elif operator[-1] == Instruction_Subsets.ZIP.value:
        if operator[0] == "giv":
            return giv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "siv":
            return siv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "gsv":
            return gsv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "siv":
            return siv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "gfv":
            return gfv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "sfv":
            return sfv(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "fia":
            return fia(operator[1],operator[2],isInALoop)
        elif operator[0] == "zia":
            return zia(operator[1],operator[2],isInALoop)
        elif operator[0] == "fsa":
            return fsa(operator[1],operator[2],isInALoop)
        elif operator[0] == "zsa":
            return zsa(operator[1],operator[2],isInALoop)
        elif operator[0] == "ffa":
            return ffa(operator[1],operator[2],isInALoop)
        elif operator[0] == "zfa":
            return zfa(operator[1],operator[2],isInALoop)
        
    elif operator[-1] == Instruction_Subsets.EXE.value:
        if operator[0] == "sia":
            return sia(operator[1],operator[2],isInALoop)
        elif operator[0] == "ssa":
            return ssa(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "sti":
            return sti(operator[1],operator[2],isInALoop)
        elif operator[0] == "stf":
            return stf(operator[1],operator[2],isInALoop)
        elif operator[0] == "stc":
            return stc(operator[1],operator[2],operator[3],isInALoop)
        elif operator[0] == "its":
            return its(operator[1],operator[2],isInALoop)
        elif operator[0] == "itf":
            return itf(operator[1], operator[2], isInALoop)
        elif operator[0] == "ias":
            return ias(operator[1],operator[2],isInALoop)
        elif operator[0] == "aif":
            return aif(operator[1],operator[2],isInALoop)
        elif operator[0] == "fts":
            return fts(operator[1],operator[2],isInALoop)
        elif operator[0] == "fti":
            return fti(operator[1], operator[2], isInALoop)
        elif operator[0] == "afi":
            return afi(operator[1],operator[2],isInALoop)
        
    elif operator[-1] == Instruction_Subsets.DLL.value:
        if operator[0] == "psh":
            return psh(operator[1],isInALoop)
        elif operator[0] == "pop":
            return pop(operator[1],isInALoop)
        elif operator[0] == "spk":
            return spk(operator[1],isInALoop)
        elif operator[0] == "ssz":
            return ssz(operator[1],isInALoop)
        elif operator[0] == "enq":
            return enq(operator[1],isInALoop)
        elif operator[0] == "deq":
            return deq(operator[1],isInALoop)
        elif operator[0] == "qpk":
            return qpk(operator[1],isInALoop)
        elif operator[0] == "qsz":
            return qsz(operator[1],isInALoop)
        elif operator[0] == "tpl":
            return tpl(isInALoop)
        elif operator[0] == "tpr":
            return tpr(isInALoop)
        elif operator[0] == "tsv":
            return tsv(operator[1],isInALoop)
        elif operator[0] == "tgv":
            return tgv(operator[1],isInALoop)
        elif operator[0] == "gbe":
            return gbe(isInALoop)
        elif operator[0] == "gen":
            return gen(isInALoop)
        elif operator[0] == "gef":
            return gef(isInALoop)
        elif operator[0] == "lce":
            return lce(isInALoop)
        elif operator[0] == "lcn":
            return lcn(isInALoop)
        elif operator[0] == "lcf":
            return lcf(isInALoop)
        elif operator[0] == "ges":
            return ges(operator[1],isInALoop)
        elif operator[0] == "ces":
            return ces(isInALoop)
    
    elif operator[-1] == Instruction_Subsets.CSV.value: #complete not checked (array also extra check if good implementation)
        if operator[0] == "cia":
            return cia(operator[1],isInALoop)
        elif operator[0] == "civ":
            return civ(operator[1],isInALoop)
        elif operator[0] == "csa":
            return csa(operator[1],isInALoop)
        elif operator[0] == "csv":
            return csv(operator[1],isInALoop)       
        elif operator[0] == "cfa":
            return cfa(operator[1],isInALoop)
        elif operator[0] == "cfv":
            return cfv(operator[1],isInALoop)
        elif operator[0] == "dia":
            return dia(operator[1],isInALoop)
        elif operator[0] == "div":
            return div_csv(operator[1],isInALoop)
        elif operator[0] == "dsa":
            return dsa(operator[1],isInALoop)
        elif operator[0] == "dsv":
            return dsv(operator[1],isInALoop)
        elif operator[0] == "dfa":
            return dfa(operator[1],isInALoop)
        elif operator[0] == "dfv":
            return dfv_csv(operator[1],isInALoop)
    
    elif operator[-1] == Instruction_Subsets.LNK.value:
        if operator[0] == "run":
            return run(operator[1], operator[2],operator[3], isInALoop)
        elif operator[0] == "rtn":#todo check if good this and make 1 line in logic
            return rtn(operator[1],isInALoop)
        
        
    return NotImplemented()

#recursiveInstructionClassList :: list[String] -> String
def recursiveInstructionClassList(argumentList: list[str], consoleInput : str) -> str:
    """Recursive function used as a map function to build up a list of all the lexed code in the Dirst programming language

    Args:
        argumentList (list): A list of lines of the scripting language of Dist

    Returns:
        list: A list of lexed classes of Dirst
    """    
    isInALoop = argumentList[0].count("")
    if argumentList[0][0] == "":
        argumentList[0] = list(filter(lambda str: (str != "") ,argumentList[0]))
    if len(argumentList) == 1:
        return [giveCorrectClass(argumentList[0], isInALoop, consoleInput)]
    else:
        return [giveCorrectClass(argumentList[0], isInALoop, consoleInput)] + recursiveInstructionClassList(argumentList[1:], consoleInput)

#lex :: list[String] -> list[Token]
def lex(file : list[str], consoleInput : str) -> list[Token]:
    """Function that lex the given file

    Args:
        file (list): A text file according to the Dist scripting language

    Returns:
        list: A list with all the correct classes and parameters(lexed of the Dirst scripting language)
    """    
    return recursiveInstructionClassList(list(map(split,file)), consoleInput)