import re
from typing import List
from tokens import *

fileTree = open("Greeter.txt", "r")

#print(fileTree.read())
#lambda x: x+x ,

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
    
# foobar_loop :: [String] → [String]
#def fileToArgumentList(list: list[str]) -> list[list[str]]:
 #   if len(list) == 0:
#        return []
#    else:
#        head, *tail = list
#        return [fileToArgumentList(head)]#split + fileToArgumentList(tail)

def giveCorrectClass(operator):
    if operator[0] == Instruction_Subsets.DIRECTORY.value:
        if operator[1] == "fnc":
            return fnc(operator[2])
        if operator[1] == "dif":
            return dif(operator[2])
        if operator[1] == "nif":
            return nif(operator[2])
        if operator[1] == "lpc":
            return lpc(operator[2])
        if operator[1] == "lpn":
            return lpn(operator[2])
        if operator[1] == "dlw":
            return dlw(operator[2])
        if operator[1] == "dlu":
            return dlu(operator[2])

    if operator[-1] == Instruction_Subsets.DAT.value:
        if operator[0] == "abs":
            return abs(operator[1],operator[2])
        if operator[0] == "neg":
            return neg(operator[1],operator[2])
        if operator[0] == "add":
            return add(operator[1],operator[2],operator[3])
        if operator[0] == "sub":
            return sub(operator[1],operator[2],operator[3])
        if operator[0] == "mul":
            return mul(operator[1],operator[2],operator[3])
        if operator[0] == "div":
            return div(operator[1],operator[2],operator[3])
        if operator[0] == "mod":
            return mod(operator[1],operator[2],operator[3])
        if operator[0] == "and":
            return and_(operator[1],operator[2],operator[3])
        if operator[0] == "orb":
            return orb(operator[1],operator[2],operator[3])
        if operator[0] == "xor":
            return xor(operator[1],operator[2],operator[3])
        if operator[0] == "xad":
            return xad(operator[1],operator[2],operator[3])
        if operator[0] == "nad":
            return nad(operator[1],operator[2],operator[3])
        if operator[0] == "nor":
            return nor(operator[1],operator[2],operator[3])
        if operator[0] == "not":
            return not_(operator[1],operator[2])
        if operator[0] == "mor":
            return mor(operator[1],operator[2],operator[3])
        if operator[0] == "less":
            return less(operator[1],operator[2],operator[3])
        if operator[0] == "equ":
            return equ(operator[1],operator[2],operator[3])
        if operator[0] == "neq":
            return neq(operator[1],operator[2],operator[3])
        if operator[0] == "gets":
            return gets(operator[1],operator[2],operator[3])    
        if operator[0] == "let":
            return let(operator[1],operator[2],operator[3])
        if operator[0] == "rdi":
            return rdi(operator[1])
        if operator[0] == "ric":
            return (operator[1])
        if operator[0] == "dsi":
            return dsi(operator[1])
        if operator[0] == "dic":
            return dic(operator[1])
        if operator[0] == "dic":
            return dic(operator[1])
        if operator[0] == "set":
            return set(operator[1],operator[2])
        if operator[0] == "max":
            return max_(operator[1],operator[2],operator[3])
        if operator[0] == "min":
            return min_(operator[1],operator[2],operator[3])
    
    if operator[-1] == Instruction_Subsets.TXT.value:
        if operator[0] == "rdc":
            return rdc(operator[1])
        if operator[0] == "rds":
            return rds(operator[1]) 
        if operator[0] == "eof":
            return eof(operator[1])
        if operator[0] == "dsc":
            return dsc(operator[1],operator[2])
        if operator[0] == "dss":
           return dss(operator[1])
        if operator[0] == "dsl":
           return dsl(operator[1])
        if operator[0] == "dec":
            return dec(operator[1],operator[2])
        if operator[0] == "des":
           return des(operator[1])
        if operator[0] == "del":
           return del_(operator[1])
        if operator[0] == "clr":
           return clr(operator[1])
        if operator[0] == "cat":
           return cat(operator[1],operator[2],operator[3])
        if operator[0] == "idx":
           return idx(operator[1],operator[2],operator[3])
        if operator[0] == "ids":
           return ids(operator[1],operator[2],operator[3],operator[4])
        
       
        
    
    if operator[-1] == Instruction_Subsets.CSV.value:#
        if operator[0] == "csv":
            return csv(operator[1])       
        if operator[0] == "civ":
            return civ(operator[1])
        if operator[0] == "dsv":
            return dsv(operator[1])
        if operator[0] == "div":
            return div(operator[1])

def recursiveInstructionClassList(argumentlist):
    if len(argumentlist) == 1:
        return [giveCorrectClass(argumentlist[0])]
    else:
        return [giveCorrectClass(argumentlist[0])] + recursiveInstructionClassList(argumentlist[1:])


def lexv2(file):
    argument_list = map(split,file)
    #token_ouput_list = []
    list1 = recursiveInstructionClassList(list(argument_list))
    print(list1)

    #maak nog functie die meerdere functies maakt mail ff diederik hoe en wat met classes en hoe moet je dan data opslaan?



def lex(file):
    #now no folder support
    """argument_list = []
    for line in file:
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
        argument_list.append(re.split(r'_|\.|\t', line))
    #print(argument_list)
    """
    argument_list = map(split,file)
    token_ouput_list = []
    for x in argument_list:
        #print(x)
        if x[0] == Instruction_Subsets.DIRECTORY.value:
            #this is a folder
            #DIRECTORY
            if x[1] == "fnc":
                fncClass = fnc(x[2])
                token_ouput_list.append(fncClass)
            if x[1] == "dlw":
                dlwClass = dlw(x[2])
                token_ouput_list.append(dlwClass)
            #print("test123: " + x[1])
        #print(Instruction_Subsets.CSV.value)
        #print(x[:1][0])
        if x[-1] == Instruction_Subsets.CSV.value:#
            if x[0] == "csv":
                csvClass = csv(x[1])
                #print(csvClass.name)
                token_ouput_list.append(csvClass)
            if x[0] == "civ":
                civClass = civ(x[1])
                token_ouput_list.append(civClass)
            if x[0] == "dsv":
                dsvClass = dsv(x[1])
                token_ouput_list.append(dsvClass)
            if x[0] == "div":
                divClass = div(x[1])
                token_ouput_list.append(divClass)
        if x[-1] == Instruction_Subsets.DAT.value:
            if x[0] == "set":
                setClass = set(x[1],x[2])
                token_ouput_list.append(setClass)
            if x[0] == "add":
                addClass = add(x[1],x[2],x[3])
                token_ouput_list.append(addClass)
            if x[0] == "dsi":
                dsiClass = dsi(x[1],x[2],x[3])
                token_ouput_list.append(dsiClass)
        if x[-1] == Instruction_Subsets.TXT.value:
            if x[0] == "dss":
                dssClass = dss(x[1])
                #print(dssClass.name)
                token_ouput_list.append(dssClass)
                #print(dssClass.name)
            if x[0] == "rds":
                rdsClass = rds(x[1])
                #print(dssClass.name)
                token_ouput_list.append(rdsClass)
                #print(rdsClass.name)

            #print("test")

    print(len(token_ouput_list))
        


#lex(fileTree)
lexv2(fileTree)
fileTree.close()
