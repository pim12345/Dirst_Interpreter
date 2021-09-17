import re
from typing import List
from tokens import *

fileTree = open("Fib_seq.txt", "r")

#print(fileTree.read())
lambda x: x+x ,

# foobar_loop :: [String] → [String]
def fileToArgumentList(list: list[str]) -> list[list[str]]:
    if len(list) == 0:
        return []
    else:
        head, *tail = list
        return [fileToArgumentList(head)] + fileToArgumentList(tail)


def lex(file):
    #now no folder support
    argument_list = []
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
    token_ouput_list = []
    for x in argument_list:
        #print(x)
        if x[0] == Instruction_Subsets.DIRECTORY.value:
            #this is a folder
            #DIRECTORY
            if x[1] == "fnc":
                fncClass = fnc(x[2])
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
        


lex(fileTree)
fileTree.close()
