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
def runABlock(code: CodeBlock, codePtr: int, state: ProgramState, output: Callable, functions: CodeBlock) -> Tuple[CodeBlock, int, ProgramState, Callable, CodeBlock]:
    if(codePtr >= len(code.statements) or codePtr < 0):
        return code, codePtr, state, output, functions
    statement = code.statements[codePtr]
    
    match statement:
        #case DeclareFunction():
            #todo check if there is already a function with that name(with count or something)
            # if statement.functionName in state.variablenamesDictionary:
            #     output("error function with the name: ", statement.name , " is already created")
            #     return code, codePtr, state, output, functions
            # state.memory[state.pointer]=0#todo check of wel goed doe en of wel nodig is, misch apparte dictionary of gewoon ignoren en alleen checken bij call
            # state.variablenamesDictionary[statement.functionName] = state.pointer
            # state.pointer+=1
            #return runABlock(code, codePtr+1, state,output, functions)
        case CallFunction():
            result, output_ = runAFunction(state.memory[state.variablenamesDictionary[statement.functionInputVar]], statement.functionReturnVar,statement.functionName,  output, functions )
            state.memory[state.variablenamesDictionary[statement.functionReturnVar]] = result
            # codePtr = len(code.statements)+1#todo change after running a function to set the pointer to end of all the underlinging functions
            # return code, codePtr, state, output, functions
            return runABlock(code, codePtr+1, state, output_, functions)#todo change after running a function to set the pointer to end of all the underlinging functions

        case createVar():
            if statement.name in state.variablenamesDictionary:
                output("error variable with the name: " + statement.name + " is already created")
                return code, codePtr, state, output, functions
            state.memory[state.pointer]=0
            state.variablenamesDictionary[statement.name] = state.pointer
            state.pointer+=1
            #print(test)
            #print(statement.name)
            return runABlock(code, codePtr+1, state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.GREATER):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            if parameter2_value > parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code, codePtr+1, state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.LESS):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            if parameter2_value < parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code, codePtr+1, state, output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.EQUAL):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            if parameter2_value == parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.NOTEQUAL):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            if parameter2_value != parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.GREATEREQUAL):
            
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
                
            if parameter2_value >= parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementsList.LESSEQUAL):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
                
            if parameter2_value <= parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case setValue():
            #print(statement.name + "= " + str(state.variablenamesDictionary[statement.name]))
            #print(type(statement.parameter1))
            if statement.parameter2.lstrip("-").isdigit():
                state.memory[state.variablenamesDictionary[statement.parameter1]] = int(statement.parameter2)
            else:
                if statement.parameter2 in state.variablenamesDictionary:
                    state.memory[state.variablenamesDictionary[statement.parameter1]] = state.memory[state.variablenamesDictionary[statement.parameter2]]
                else:
                    state.memory[state.variablenamesDictionary[statement.parameter1]] = statement.parameter2#because language dont differenstate between if an string is an variable or an string, is there no error if an user forget to create an var.
            return runABlock(code,codePtr+1,state,output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.plus):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
                
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value + parameter3_value
            return runABlock(code,codePtr+1,state,output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.minus):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value - parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.multiply):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value * parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.divide):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value / parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.modulo):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value % parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.andOp):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value & parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.orb):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value | parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.xor):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value ^ parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.xad):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            #state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value  parameter3_value
            output("error: not yet implented")
            return code, codePtr, state, output
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.nad):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value & parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.nor):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value | parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.maxVal):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            state.memory[state.variablenamesDictionary[statement.parameter1]] = max(parameter2_value, parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsList.maxVal):
            if statement.parameter2.isdigit():#todo fix code duplication for this if statement
                parameter2_value = int(statement.parameter2)
            else:
                parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
            if statement.parameter3.isdigit():
                parameter3_value = int(statement.parameter3)
            else:
                parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
            state.memory[state.variablenamesDictionary[statement.parameter1]] = min(parameter2_value, parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
            
        case displayValue():
            #print(statement.value)
            #print(str(state.memory[state.variablenamesDictionary[statement.value]]))
            #todo check, not triggerd using dsi 
            if statement.nameVar in state.variablenamesDictionary:#todo check if good
                if statement.newLine:
                    output(str(state.memory[state.variablenamesDictionary[statement.nameVar]]) + '\n')
                else:
                    output(str(state.memory[state.variablenamesDictionary[statement.nameVar]]))
            else:
                if statement.newLine:
                    output(str(statement.nameVar) + '\n')
                else:
                    output(str(statement.nameVar))
            #output(state.memory[state.variablenamesDictionary[statement.nameVar]])
            #output = str(state.memory[state.variablenamesDictionary[statement.value]]) + '\n'
            return runABlock(code, codePtr+1, state, output, functions)
        case deleteVar():
            state.memory[state.variablenamesDictionary[statement.name]] = 0
            del state.variablenamesDictionary[statement.name]
            return runABlock(code, codePtr+1, state, output, functions)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=True,onlyOneTime=True):#fnc
            statementLoop, codePtr_, state_, output, functions = runABlock(code.statements[codePtr].block, 0, state, output, functions)#loop only once needs work!!!!!!!!!!!!!!!
            if codePtr_ <= -1:#todo add logic in begin if that works and other in other loop functions
                    return code, codePtr, state, output, functions
            return runABlock(code, codePtr+1, state, output, functions)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=False,onlyOneTime=True):#dif
            if state.memory[state.variablenamesDictionary[statement.varname]] != 0:#only checks if statemt is var name not if statement is int maybe implent in front code
                statementLoop, codePtr_, state_, output, functions = runABlock(code.statements[codePtr].block, 0, state, output, functions)
                if codePtr_ <= -1:#todo add logic in begin if that works and other in other loop functions
                    return code, codePtr, state, output, functions
                return runABlock(code, codePtr+1, state_, output, functions)
            return runABlock(code, codePtr+1, state, output, functions)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=False,onlyOneTime=True):#nif
            if state.memory[state.variablenamesDictionary[statement.varname]] == 0:#only checks if statemt is var name not if statement is int maybe implent in front code
                statementLoop, codePtr_, state_, output, functions = runABlock(code.statements[codePtr].block, 0, state, output, functions)
                if codePtr_ <= -1:#todo add logic in begin if that works and other in other loop functions
                    return code, codePtr, state, output, functions
                return runABlock(code, codePtr+1, state_, output, functions)
            return runABlock(code, codePtr+1, state, output, functions)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=False,onlyOneTime=False):#lpc # check if logic is good with if statement
            state_, output = runLoopWhileNotZero(code.statements[codePtr].block, state, output, statement.varname, functions)
            return runABlock(code, codePtr+1, state_, output, functions)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=False,onlyOneTime=False):#lpn
            state_, output = runLoopWhileZero(code.statements[codePtr].block, state, output, statement.varname, functions)# check if logic is good with if statement in function
            return runABlock(code, codePtr+1, state_, output, functions)
        case Loop(block=block,varname=varname,whileZero=False,loopAtLeastOnce=True,onlyOneTime=False):#dlw
            statementLoop, codePtr_, state_, output, functions = runABlock(code.statements[codePtr].block, 0, state, output, functions)#loop at least once
            state_, output = runLoopWhileNotZero(statementLoop, state_, output, statement.varname, functions)
            return runABlock(code, codePtr+1, state_, output, functions)
        case Loop(block=block,varname=varname,whileZero=True,loopAtLeastOnce=True,onlyOneTime=False):#dlu
            statementLoop, codePtr_, state_, output, functions = runABlock(code.statements[codePtr].block, 0, state, output, functions)#loop at least once
            state_, output = runLoopWhileZero(statementLoop, state_, output, statement.varname, functions)
            return runABlock(code, codePtr+1, state_, output, functions)
        #case RunFunction():
        #    state.memory[state.variablenamesDictionary[statement.result]],output_ = runAFunction(statement.function,state.memory[state.variablenamesDictionary[statement.argument]], output)
        #    #print(state.variablenamesDictionary[statement.result])
        #    #print(state.memory[state.variablenamesDictionary[statement.result]])
        #    return runABlock(code, codePtr+1, state, output_, functions)
        case ReturnFunction():
            if statement.parameter1.isdigit():
                state.memory[0] = int(statement.parameter1)#always return on 0 place in memory is always the return var, only 1 return var supported
            else:#state.variablenamesDictionary["result"]
                state.memory[0] = state.memory[state.variablenamesDictionary[statement.parameter1]]#todo add maybe check if in var in dictionary and otherwise error
            codePtr = -1
            return code, codePtr, state, output, functions
        # case ReturnIFFunction():#returnIFEqualFunction
        #     #print(statement.parameter1)
        #     if state.memory[state.variablenamesDictionary[statement.parameter1]] == parameter2_value:
        #         state.memory[state.variablenamesDictionary["result"]] = int(statement.parameter3)
        #         #output += statement.parameter3 + '\n'
        #         return code, codePtr, state, output, functions
        #     else:
        #         return runABlock(code, codePtr+1, state, output, functions)
        case NotImplemented() | _:
            #print(statement)
            #print(type(statement))
            output("method not implemented" + '\n')
            return code, codePtr, state, output, functions
            #raise Exception('method not implemented')

#runAFunction :: str -> int -> Callable -> (int, Callable)
def runAFunction(functionInputVarValue: str, functionReturnVar : str, functionName: str, output: Callable, functions: CodeBlock) -> Tuple[int,Callable]:
    
    functionCode = list(filter(lambda x: isinstance(x, DeclareFunction) and x.functionName == functionName, functions.statements))[0]#.block
    # create a new state for the function
    functionState = ProgramState()
    # copy the variables from the current state to the function state(input and return var)
    functionState.memory[functionState.pointer]=functionInputVarValue
    functionState.variablenamesDictionary[functionCode.functionInputVar] = functionState.pointer
    functionState.pointer+=1
    
    #functionState.memory[functionState.pointer]=0
    #functionState.variablenamesDictionary[functionReturnVar] = functionState.pointer
    #functionState.pointer+=1
    #todo check if return var exists, if is an digit also add check if it is a digit and return that directly
    code_, codePtr_, functionState_, output_, functions = runABlock(functionCode.block, 0, functionState, output, functions)#todo make it smarter like runloop functions so it requires less hackery
    return functionState_.memory[0], output_#in place 0 in the memory is always the return var(only one return var supported)

#runLoopWhileZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileZero(loop : CodeBlock, state: ProgramState, output : Callable, loopname : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    #print("loop")
    #print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if state.memory[state.variablenamesDictionary[loopname]] == 0:
        code_, codePtr_, state_, output_, functions_ = runABlock(loop.code,0,state,output, functions)
        return runLoopWhileZero(loop, state_, output_, loopname, functions_)
    else:
        return state, output#todo is this correct functional programming?

#runLoopWhileNotZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileNotZero(loop : CodeBlock, state: ProgramState, output : Callable, loopname : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    #print("loop")
    #print(state.pointer)
    #if(state.memory[state.pointer]!=0):
    if state.memory[state.variablenamesDictionary[loopname]] != 0:
        code_, codePtr_, state_, output_, functions_ = runABlock(loop, 0, state, output, functions)
        return runLoopWhileNotZero(loop, state_, output_, loopname, functions_)
    else:
        return state, output