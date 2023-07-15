from typing import List, Tuple, Callable, Any
from Lexer.tokens import *
from Lexer.lexer import *
from Parser.parser import *
from Tools.tools import *
import math
from operator import xor

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
    
    #todo check wat te doen met parameter 1 wel of niet casten
    if hasattr(statement, 'parameter2'):#check if object has parameter2
        if statement.parameter2 in state.variablenamesDictionary:
            parameter2_value = state.memory[state.variablenamesDictionary[statement.parameter2]]
        else:
            parameter2_value = __builtins__[statement.instructionType.value[0]](statement.parameter2)#https://gist.github.com/mdogo/4947278 #todo check safety of this, and of allowed to use this
            #parameter2_value = statement.instructionType(statement.parameter2)#todo check if casting works, and if it works add documentation
            
    if hasattr(statement, 'parameter3'):#check if object has parameter3
        if statement.parameter3 in state.variablenamesDictionary:
            parameter3_value = state.memory[state.variablenamesDictionary[statement.parameter3]]
        else:
            parameter3_value = __builtins__[statement.instructionType.value[0]](statement.parameter3)#todo check if casting works, and if it works add documentation #https://gist.github.com/mdogo/4947278
    
    
    
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
            result, output_ = runAFunction(state.memory[state.variablenamesDictionary[statement.functionInputVar]], statement.functionReturnVar, statement.functionName, output, functions)
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
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.GREATER):
            if parameter2_value > parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code, codePtr+1, state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.LESS):
            if parameter2_value < parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code, codePtr+1, state, output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.EQUAL):
            if parameter2_value == parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.NOTEQUAL):
            if parameter2_value != parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.GREATEREQUAL):
            if parameter2_value >= parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.LESSEQUAL):
            if parameter2_value <= parameter3_value:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = -1
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = 0
            return runABlock(code,codePtr+1,state,output, functions)
        case setValue():
            #todo convert to new casting system
            if statement.parameter2.lstrip("-").isdigit():
                state.memory[state.variablenamesDictionary[statement.parameter1]] = int(statement.parameter2)
            else:
                if statement.parameter2 in state.variablenamesDictionary:
                    state.memory[state.variablenamesDictionary[statement.parameter1]] = state.memory[state.variablenamesDictionary[statement.parameter2]]
                else:
                    state.memory[state.variablenamesDictionary[statement.parameter1]] = statement.parameter2#because language dont differenstate between if an string is an variable or an string, is there no error if an user forget to create an var.
            return runABlock(code,codePtr+1,state,output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.plus):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value + parameter3_value
            return runABlock(code,codePtr+1,state,output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.minus):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value - parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.multiply):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value * parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.divide):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value / parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.modulo):            
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value % parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.andOp):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value & parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.orb):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value | parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.xor):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = parameter2_value ^ parameter3_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.xad):
            #https://deepai.org/machine-learning-glossary-and-terms/xand is it the same as xnor
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value ^ parameter3_value)#todo test if good
            return code, codePtr, state, output
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.nad):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value & parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.nor):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~(parameter2_value | parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.bitWiseNot):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = ~parameter2_value
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.maxVal):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = max(parameter2_value, parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.maxVal):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = min(parameter2_value, parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case roundValue():
            if statement.roundToCeiling == True:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = math.ceil(parameter2_value)
            else:
                state.memory[state.variablenamesDictionary[statement.parameter1]] = math.floor(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,mathFunctionType=MathFloatType.power):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.pow(parameter2_value, parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.sign):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.copysign(1, parameter2_value)#todo check if good use of sign https://www.tutorialspoint.com/how-to-get-the-sign-of-an-integer-in-python
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.squareRoot):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.sqrt(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFloatFunctionType=MathFloatType.sin):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.sin(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.cos):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.cos(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.tan):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.tan(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicSin):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.sinh(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicCos):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.cosh(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicTan):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.tanh(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.logBase10):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.log10(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.logNatural):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.log(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,mathFunctionType=MathFloatType.log):  
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.log(parameter2_value, parameter3_value)
            return runABlock(code, codePtr+1, state, output, functions)
            
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.eToPower):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.exp(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.absolute):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = abs(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.negative):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = -parameter2_value#todo need to test if good negative value, otherwise use ~abs
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseSin):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.asin(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseCos):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.acos(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseTan):
            state.memory[state.variablenamesDictionary[statement.parameter1]] = math.atan(parameter2_value)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case displayValue():
            #print(statement.value)
            #print(str(state.memory[state.variablenamesDictionary[statement.value]]))
            #todo convert to new type system
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
        
        case ReturnFunction():
            if statement.parameter1.isdigit():
                state.memory[0] = int(statement.parameter1)#always return on 0 place in memory is always the return var, only 1 return var supported
            else:#state.variablenamesDictionary["result"]
                state.memory[0] = state.memory[state.variablenamesDictionary[statement.parameter1]]#todo add maybe check if in var in dictionary and otherwise error
            codePtr = -1
            return code, codePtr, state, output, functions
        case NotImplemented(ignore=True):
            #statement is not implemented and not really important so ignore it
            return runABlock(code, codePtr+1, state, output, functions)
        
        case NotImplemented() | _:
            
            output("method not implemented" + '\n')
            return code, codePtr, state, output, functions

#runAFunction :: str -> int -> Callable -> (int, Callable)
def runAFunction(functionInputVarValue: str, functionReturnVar : str, functionName: str, output: Callable, functions: CodeBlock) -> Tuple[int,Callable]:
    
    functionCodes = list(filter(lambda x: isinstance(x, DeclareFunction) and x.functionName == functionName, functions.statements))#.block
    if len(functionCodes) == 0:
        #no function declared with that name
        output("error, no function declared with the name: " + functionName + '\n')
        return -1, output#todo add return code if error encountered
    else:
        functionCode = functionCodes[0]
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
    if state.memory[state.variablenamesDictionary[loopname]] == 0:
        code_, codePtr_, state_, output_, functions_ = runABlock(loop.code,0,state,output, functions)
        return runLoopWhileZero(loop, state_, output_, loopname, functions_)
    else:
        return state, output#todo is this correct functional programming?

#runLoopWhileNotZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileNotZero(loop : CodeBlock, state: ProgramState, output : Callable, loopname : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    if state.memory[state.variablenamesDictionary[loopname]] != 0:
        code_, codePtr_, state_, output_, functions_ = runABlock(loop, 0, state, output, functions)
        return runLoopWhileNotZero(loop, state_, output_, loopname, functions_)
    else:
        return state, output