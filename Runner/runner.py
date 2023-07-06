from typing import List, Tuple, Callable, Any
from Lexer.tokens import *
from Lexer.lexer import *
from Parser.parser import *
from Tools.tools import *

class ProgramState:
    def __init__(self):
        self.pointer = 1#need to clear register 0 for loops and arguments
        self.memory = [0]*10#om de 2 registers is eerste de identifyer de 2e is de variable value
        self.variablenamesDictionary = {}

    #__repr__ :: ProgramState -> String
    def __repr__(self) -> str:
        return "ptr: " + str(self.pointer) + " val: " + str(self.memory) + " varname dictionary: " + str(self.variablenamesDictionary)


#runABlock :: CodeBlock -> Integer -> ProgramState -> Callable -> (CodeBlock, int, ProgramState, Callable)
def runABlock(code: CodeBlock, codePtr: int, state: ProgramState, output: Callable) -> Tuple[CodeBlock, int, ProgramState, Callable]:
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
        try:
            parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
        except KeyError:#key has not be found so the var has not been created
            parameter2_value = statement.parameter2#language is not very clear when to specifi if it is a variable or a value, so if it not created it assumes it is a value, this can be a problem if expect it to be a variable, but forget to create it. But I won't fix this because otherwise it is out of spec with the language
        #if isinstance(statement.parameter2, str):
        #parameter2_value = statement.parameter2
        #else:
        #    parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
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
                output("error: ", statement.name , " already created")
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
            
            if statement.nameVar in state.variablenamesDictionary:#todo check if good
                if statement.newLine:
                    output(state.memory[state.variablenamesDictionary[statement.nameVar]] + '\n')
                else:
                    output(state.memory[state.variablenamesDictionary[statement.nameVar]])
            else:
                if statement.newLine:
                    output(statement.nameVar + '\n')
                else:
                    output(statement.nameVar)
            #output(state.memory[state.variablenamesDictionary[statement.nameVar]])
            #output = str(state.memory[state.variablenamesDictionary[statement.value]]) + '\n'
            return runABlock(code,codePtr+1,state,output)
        case deleteVar():
            state.memory[state.variablenamesDictionary[statement.name]] = 0
            del state.variablenamesDictionary[statement.name]
            return runABlock(code,codePtr+1,state,output)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=True,onlyOneTime=True):#fnc
            statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)#loop only once needs work!!!!!!!!!!!!!!!
            return runABlock(code, codePtr+1, state, output)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=False,onlyOneTime=True):#dif
            if state.memory[state.variablenamesDictionary[statement.varname]] != 0:#only checks if statemt is var name not if statement is int maybe implent in front code
                statementLoop, codePtr_, state_, output = runABlock(code.statements[codePtr].block, 0, state, output)
            return runABlock(code, codePtr+1, state_, output)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=False,onlyOneTime=True):#nif
            if state.memory[state.variablenamesDictionary[statement.varname]] == 0:#only checks if statemt is var name not if statement is int maybe implent in front code
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
        case ReturnIFFunction():#returnIFEqualFunction
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

#runAFunction :: str -> int -> Callable -> (int, Callable)
def runAFunction(filename : str, argument1 : int, output: Callable) -> Tuple[int,Callable]:
    fileTree = readFile(filename + ".txt")
    lexOutput = lex(fileTree)
    state = ProgramState()
    state.variablenamesDictionary["argument1"] = 0
    state.variablenamesDictionary["result"] = 9
    state.memory[0] = argument1
    code, codePtr, state, output = runABlock(parseCodeBlock(lexOutput, CodeBlock())[1], 0, state, output)
    return state.memory[state.variablenamesDictionary["result"]],output

#runLoopWhileZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileZero(loop : CodeBlock, state: ProgramState, output : Callable, loopname : str) -> Tuple[ProgramState, Callable]:
    #print("loop")
    #print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if state.memory[state.variablenamesDictionary[loopname]] != 0:
        return state, output
    else:
        code_, codePtr_, state_, output_ = runABlock(loop.code,0,state,output)
        return runLoopWhileZero(loop, state_, output_, loopname)

#runLoopWhileNotZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileNotZero(loop : CodeBlock, state: ProgramState, output : Callable, loopname : str) -> Tuple[ProgramState, Callable]:
    #print("loop")
    #print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if state.memory[state.variablenamesDictionary[loopname]] == 0:
        return state, output
    else:
        code_, codePtr_, state_, output_ = runABlock(loop,0,state,output)
        return runLoopWhileNotZero(loop, state_, output_, loopname)