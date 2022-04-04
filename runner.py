from typing import List, Tuple
from tokens import *
from lexer import *
from Parser import *

class ProgramState:
    def __init__(self):
        self.pointer = 1#need to clear register 0 for loops and arguments
        self.memory = [0]*10#om de 2 registers is eerste de identifyer de 2e is de variable value
        self.variablenamesDictionary = {}

    #__repr__ :: ProgramState -> String
    def __repr__(self) -> str:
        return "ptr: " + str(self.pointer) + " val: " + str(self.memory) + " varname dictionary: " + str(self.variablenamesDictionary)


#runABlock :: CodeBlock -> Integer -> ProgramState -> String -> (ProgramState, String) <-old check if still correct
def runABlock(code: CodeBlock, codePtr: int, state: ProgramState, output: string) -> Tuple[CodeBlock, int, ProgramState, str]:
    #print(state)
    #print(code.statements)
    #print("len statments: " + str(len(code.statements)) + " len codePtr: " + str(codePtr))
    if(codePtr >= len(code.statements)):
        return code, codePtr, state, output
    statement = code.statements[codePtr]
    #print(str(statement))
    #print(type(statement))
    try:
        parameter2_value = int(statement.parameter2)#better name and explaining wat to do and explaining that if 
    except ValueError:
        parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
    except AttributeError:
        pass #there is no parameter 2, so it can't convert it
    try:
        parameter3_value = int(statement.parameter3)
    except ValueError:
        parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
    except AttributeError:
        pass #there is no parameter 3, so it can't convert it. So it will ignore it
    
    match statement:
        case createVar():
            if statement.name in state.variablenamesDictionary:
                output("error: ", statement.name , " allready created")
                return code, codePtr, state, output
            state.memory[state.pointer]=0
            state.variablenamesDictionary[statement.name] = state.pointer
            state.pointer+=1
            #print(test)
            #print(statement.name)
            return runABlock(code,codePtr+1,state,output)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.GREATER):
            if parameter2_value > parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.LESS):
            if parameter2_value < parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.EQUAL):
            if parameter2_value == parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.NOTEQUAL):
            if parameter2_value != parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.GREATEREQUAL):
            if parameter2_value >= parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.LESSEQUAL):
            if parameter2_value <= parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output)
        case setValue():
            #print(statement.name + "= " + str(state.variablenamesDictionary[statement.name]))
            #print(type(statement.parameter1))
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.plus):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value + parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.minus):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value - parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.multiply):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value * parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.divide):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value / parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.modulo):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value % parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.andOp):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value & parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.orb):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value | parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.xor):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value ^ parameter3_value
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.xad):
            #state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value  parameter3_value
            output("not yet implented")
            return code, codePtr, state, output
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.nad):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value & parameter3_value)
            return runABlock(code,codePtr+1,state,output)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.nor):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value | parameter3_value)
            return runABlock(code,codePtr+1,state,output)
        case displayValue():
            #print(statement.value)
            #print(str(state.memory[state.variablenamesDictionary[statement.value]]))
            output("output: ", state.memory[state.variablenamesDictionary[statement.value]])
            #output = str(state.memory[state.variablenamesDictionary[statement.value]]) + '\n'
            return runABlock(code,codePtr+1,state,output)
        case deleteVar():
            state.memory[state.variablenamesDictionary[statement.name]] = 0
            del state.variablenamesDictionary[statement.name]
            return runABlock(code,codePtr+1,state,output)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=True,onlyOneTime=True):#fnc
            statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)#loop only once needs work!!!!!!!!!!!!!!!
            return runABlock(code, codePtr+1, state, output)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=False,onlyOneTime=True):#dif #maybe implent if statement in switch case
            if state.memory[state.variablenamesDictionary[statement.parameter1]] != 0:#only checks if statemt is var name not if statement is int maybe implent in front code
                statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)
            return runABlock(code, codePtr+1, state_, output)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=False,onlyOneTime=True):#nif
            if state.memory[state.variablenamesDictionary[statement.parameter1]] == 0:#only checks if statemt is var name not if statement is int maybe implent in front code
                statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)
            return runABlock(code, codePtr+1, state_, output)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=False,onlyOneTime=False):#lpc # check if logic is good with if statement
            state_, output = runLoopWhileNotZero(code.statements[codePtr].block, state, output, statement.varname)
            return runABlock(code, codePtr+1, state_, output)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=False,onlyOneTime=False):#lpn
            state_, output = runLoopWhileZero(code.statements[codePtr].block, state, output, statement.varname)# check if logic is good with if statement in function
            return runABlock(code, codePtr+1, state_, output)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=True,onlyOneTime=False):#dlw
            statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)#loop at least once
            state_, output = runLoopWhileNotZero(statementLoop, state_, output, statement.varname)
            return runABlock(code, codePtr+1, state_, output)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=True,onlyOneTime=False):#dlu
            statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)#loop at least once
            state_, output = runLoopWhileZero(statementLoop, state_, output, statement.varname)
            return runABlock(code, codePtr+1, state_, output)
        case RunFunction():
            state.memory[state.variablenamesDictionary[statement.result]],output_ = runAFunction(statement.function,state.memory[state.variablenamesDictionary[statement.argument]], output)
            #print(state.variablenamesDictionary[statement.result])
            #print(state.memory[state.variablenamesDictionary[statement.result]])
            return runABlock(code, codePtr+1, state, output_)
        case ReturnFunction():
            return code, codePtr, state, output
        case ReturnIFFunction():#returnIFEquealFunction
            #print(statement.parameter1)
            if state.memory[state.variablenamesDictionary[statement.parameter1]] == parameter2_value:
                state.memory[state.variablenamesDictionary["result"]] = int(statement.parameter3)
                #output += statement.parameter3 + '\n'
                return code, codePtr, state, output
            else:
                return runABlock(code, codePtr+1, state, output)
        case NotImplemented() | _:
            #print(statement)
            #print(type(statement))
            raise Exception('method not implemented')
    
def runAFunction(filename : str, argument1 : int, output : str):
    fileTree = open(( "./" + filename + ".txt"), "r")
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
def runLoopWhileZero(loop : CodeBlock, state: ProgramState, output : str, loopname : str) -> Tuple[ProgramState, str, str]:#loop : Loop
    #print("loop")
    #print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if state.memory[state.variablenamesDictionary[loopname]] != 0:
        return state, output
    else:
        code_, codePtr_, state_, output_ = runABlock(loop.code,0,state,output)
        return runLoopWhileZero(loop, state_, output_, loopname)

def runLoopWhileNotZero(loop : CodeBlock, state: ProgramState, output : str, loopname : str) -> Tuple[ProgramState, str]:#loop : Loop
    #print("loop")
    #print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if state.memory[state.variablenamesDictionary[loopname]] == 0:
        return state, output
    else:
        code_, codePtr_, state_, output_ = runABlock(loop,0,state,output)
        return runLoopWhileNotZero(loop, state_, output_, loopname)