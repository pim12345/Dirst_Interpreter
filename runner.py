from typing import List, Tuple
from tokens import *
from lexer import *
from Parser import *


def runner(parse):
    pass

class ProgramState:
    def __init__(self):
        self.pointer = 1#need to clear register 0 for loops and arguments
        self.memory = [0]*10#om de 2 registers is eerste de identifyer de 2e is de variable value
        self.variablenamesDictionary = {}

    #__repr__ :: ProgramState -> String
    def __repr__(self) -> str:
        return "ptr: " + str(self.pointer) + " val: " + str(self.memory)


#runABlock :: CodeBlock -> Integer -> ProgramState -> String -> (ProgramState, String)
def runABlock(code : CodeBlock, codePtr : int, state : ProgramState, output : str) -> Tuple[CodeBlock,int, ProgramState, str]:
    print(state)
    #print(code.statements)
    print("len statments: " + str(len(code.statements)) + " len codePtr: " + str(codePtr))
    if(codePtr >= len(code.statements)):
        return code, codePtr, state, output
    statement = code.statements[codePtr]
    print(str(statement))
    if isinstance(statement, createVar):
        print("test")
        if statement.name in state.variablenamesDictionary:
            print("error systeem nog niet in plaats, maar var bestaat al ")
            return code, codePtr, state, "error"
        state.memory[state.pointer]=0
        state.variablenamesDictionary[statement.name] = state.pointer
        state.pointer+=1
        
        #print(test)
        #print(statement.name)
        return runABlock(code,codePtr+1,state,output)

    elif isinstance(statement, setValue):
        print("test2")
        print(statement.name + "= " + str(state.variablenamesDictionary[statement.name]))
        print(type(statement.newValue))
        if statement.newValue.isdigit() == True:
            state.memory[state.variablenamesDictionary[statement.name]] = int(statement.newValue)
        else:
            state.memory[state.variablenamesDictionary[statement.name]] = state.memory[state.variablenamesDictionary[statement.newValue]]
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, addValue):
        if statement.parameter2.isdigit() == True and statement.parameter3.isdigit() == False:
            state.memory[state.variablenamesDictionary[statement.parameter1]] = statement.parameter2 + state.memory[state.variablenamesDictionary[statement.parameter3]]
        elif statement.parameter2.isdigit() == False and statement.parameter3.isdigit() == True:
            state.memory[state.variablenamesDictionary[statement.parameter1]] = state.memory[state.variablenamesDictionary[statement.parameter2]] + statement.parameter3
        else:
            state.memory[state.variablenamesDictionary[statement.parameter1]] = state.memory[state.variablenamesDictionary[statement.parameter2]] + state.memory[state.variablenamesDictionary[statement.parameter3]]
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, displayValue):
        print(statement.value)
        #print(str(state.memory[state.variablenamesDictionary[statement.value]]))
        print("output in block: ", output)
        output = str(state.memory[state.variablenamesDictionary[statement.value]]) + '\n'
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, valueCompare):
        print(state.memory[state.variablenamesDictionary[statement.parameter2]])
        print(statement.parameter2)
        if (int(state.memory[state.variablenamesDictionary[statement.parameter2]]) < int(statement.parameter3) ):#need fix for fib later, maak functie als niet in dir zit kijkt of het naar een int gecast kan worden, anders error meegeven
            state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
        else:
            state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, subValue):
        state.memory[state.variablenamesDictionary[statement.parameter1]] = state.memory[state.variablenamesDictionary[statement.parameter2]] - int(statement.parameter3) #temp extend to all possible combinations
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, deleteVar):
        state.memory[state.variablenamesDictionary[statement.name]] = 0
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, Loop):
        print("loop")
        print("statement name: ", statement.varname)
        #state.memory[state.pointer]=1
        print()
        state.memory[0] = state.memory[state.variablenamesDictionary[statement.varname]] 
        #state.memory[state.pointer]=1
        #state.memory[0]=1
        #codePtr+=1
        statementLoop = code.statements[codePtr].code
        print(type(statementLoop))
        statementLoop, codePtr_, state_, output = runABlock(statementLoop, 0, state, output)#loop at least once
        state_, output = runloopDLW(statementLoop, state_, output)
        state_.memory[state.variablenamesDictionary[statement.varname]] = state_.memory[0]
        state_.memory[0] = state.memory[0]
        #return runABlock(code, codePtr + 1, state_, output_)
        return runABlock(code, codePtr+1, state_, output)
    elif isinstance(statement, RunFunction):
        state.memory[state.variablenamesDictionary[statement.result]],output_ = runAFunction(statement.function,state.memory[state.variablenamesDictionary[statement.argument]], output)
        print(state.variablenamesDictionary[statement.result])
        print(state.memory[state.variablenamesDictionary[statement.result]])
        return runABlock(code, codePtr+1, state, output_)
    elif isinstance(statement, ReturnFunction):
        return code, codePtr, state, output
    elif isinstance(statement, ReturnIFFunction):#returnIFEquealFunction
        print(statement.parameter1)
        if statement.parameter1.isdigit() == True and statement.parameter2.isdigit() == False:
            if int(statement.parameter1) == state.memory[state.variablenamesDictionary[statement.parameter2]]:
                state.memory[state.variablenamesDictionary["result"]] = int(statement.parameter3)
                #output += statement.parameter3 + '\n'
                return code, codePtr, state, output
            else:
                return runABlock(code, codePtr+1, state, output)
        elif statement.parameter1.isdigit() == False and statement.parameter2.isdigit() == True:
            if int(statement.parameter2) == state.memory[state.variablenamesDictionary[statement.parameter1]]:
                state.memory[state.variablenamesDictionary["result"]] = int(statement.parameter3)
                #output += statement.parameter3 + '\n'
                return code, codePtr, state, output
            else:
                return runABlock(code, codePtr+1, state, output)
        elif statement.parameter1.isdigit() == True and statement.parameter2.isdigit() == True:
            if statement.parameter1 == statement.parameter2:
                state.memory[state.variablenamesDictionary["result"]] = int(statement.parameter3)
                #output += statement.parameter3 + '\n'
                return code, codePtr, state, output
            else:
                return runABlock(code, codePtr+1, state, output)
        else:
            if state.memory[state.variablenamesDictionary[statement.parameter1]] == state.memory[state.variablenamesDictionary[statement.parameter2]]:
                state.memory[state.variablenamesDictionary["result"]] = int(statement.parameter3)
                #output += statement.parameter3 + '\n'
                return code, codePtr, state, output
            else:
                return runABlock(code, codePtr+1, state, output)
    print("end")
    state.memory[state.pointer]=0 #idk misch weg
    return code, codePtr, state, output
    
def runAFunction(filename : str, argument1 : int, output : str):
    #eerst andere code lexen uit andere file daarna parsen en daarna door de runAvblock halen. 
    fileTree = open((filename + ".txt"), "r")
    lexoutput = lex(fileTree)
    fileTree.close()
    state = ProgramState()
    state.variablenamesDictionary["argument1"] = 0
    state.variablenamesDictionary["result"] = 9
    state.memory[0] = argument1
    code, codePtr, state, output = runABlock(parseCodeBlock(lexoutput, CodeBlock())[1], 0, state, output)
    
    #return number of string in ieder geval 1 arg en output
    return state.memory[state.variablenamesDictionary["result"]],output

    #runloop :: Loop -> ProgramState -> String -> (ProgramState, String)
def runloopDLW(loop : CodeBlock, state: ProgramState, output : str) -> Tuple[ProgramState, str]:#loop : Loop
    #print("loop")
    print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if(state.memory[0]!=0):
        return state,output
    else:
        state_, output_ = runABlock(loop.code,0,state,output)
        return runloopDLW(loop, state_, output_)

def runloop(loop : CodeBlock, state: ProgramState, output : str) -> Tuple[ProgramState, str]:#loop : Loop
    #print("loop")
    print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if(state.memory[0]!=0):
        return state,output
    else:
        state_, output_ = runABlock(loop.code,0,state,output)
        return runloop(loop, state_, output_)