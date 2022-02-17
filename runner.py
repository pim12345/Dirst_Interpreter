from typing import List, Tuple
from tokens import *
from lexer import *
from Parser import *


def runner(parse):
    pass

class ProgramState:
    def __init__(self):
        self.pointer = 0
        self.memory = [0]*10#om de 2 registers is eerste de identifyer de 2e is de variable value
        self.variablenamesDictionary = {}

    #__repr__ :: ProgramState -> String
    def __repr__(self) -> str:
        return "ptr: " + str(self.pointer) + " val: " + str(self.memory)


#runABlock :: CodeBlock -> Integer -> ProgramState -> String -> (ProgramState, String)
def runABlock(code : CodeBlock, codePtr : int, state : ProgramState, output : str) -> Tuple[ProgramState, str]:
    print(state)
    #print(code.statements)
    print("len statments: " + str(len(code.statements)) + " len codePtr: " + str(codePtr))
    if(codePtr >= len(code.statements)):
        return state, output
    statement = code.statements[codePtr]
    print(str(statement))
    if isinstance(statement, createVar):
        print("test")
        if statement.name in state.variablenamesDictionary:
            print("error systeem nog niet in plaats, maar var bestaat al ")
            return state, "error"
        state.memory[state.pointer]=0
        state.variablenamesDictionary[statement.name] = state.pointer
        state.pointer+=1
        
        #print(test)
        #print(statement.name)
        return runABlock(code,codePtr+1,state,output)

    elif isinstance(statement, setValue):
        print("test2")
        print(statement.name + "= " + str(state.variablenamesDictionary[statement.name]))
        state.memory[state.variablenamesDictionary[statement.name]] = statement.newValue
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, displayValue):
        print(statement.value)
        return runABlock(code,codePtr+1,state,output)
    elif isinstance(statement, valueCompare):
        print(state.memory[state.variablenamesDictionary[statement.parameter2]])
        if (int(state.memory[state.variablenamesDictionary[statement.parameter2]]) < int(statement.parameter3) ):#need fix for fib later, maak functie als niet in dir zit kijkt of het naar een int gecast kan worden, anders error meegeven
            state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
        else:
            state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
        return runABlock(code,codePtr+1,state,output)

    elif isinstance(statement, LoopOpen):#LoopOpen
        print("loop")
        #state.memory[state.pointer]=1
        state.memory[state.pointer]=1
        state.memory[0]=1
        #codePtr+=1
        statement2 = code.statements[codePtr+1]
        state_, output_ = runloop(statement2, state, output)
        #return runABlock(code, codePtr + 1, state_, output_)
        return runABlock(code, codePtr+1, state_, output_)
    
    print("end")
    #state.memory[state.pointer]=0
    #return state, output
    

    #runloop :: Loop -> ProgramState -> String -> (ProgramState, String)
def runloop(loop : CodeBlock, state: ProgramState, output : str) -> Tuple[ProgramState, str]:#loop : Loop
    #print("loop")
    print(state.pointer)
    if(state.memory[state.pointer]!=0):
        return state,output
    else:
        state_, output_ = runABlock(loop.code,0,state,output)
        return runloop(loop, state_, output_)