from typing import List, Tuple, Callable, Self, Any, Union
from Lexer.tokens import *
from Lexer.lexer import *
from Parser.parser import *
from Tools.tools import *
import math
from operator import xor

class ProgramState():
    def __init__(self, pointer: int=1, memory: List[int]=[math.nan]*10, variableNamesDictionary: dict={}, stack: List[int]=[], tape: List[int]=[math.nan], tapePointer: int=0):#overloading didnt work so this is the solution
        self.pointer = pointer#need to clear register 0 for loops and arguments
        self.memory = memory#om de 2 registers is eerste de identifyer de 2e is de variable value
        self.variableNamesDictionary = variableNamesDictionary
        self.stack = stack
        self.tape = tape
        self.tapePointer = tapePointer
    
    #changeStatePointer :: ProgramState -> Union[int, float, string] -> ProgramState
    def changeStateMemory(self, index: int, value: Union[int, float, str] ) -> Self:
        newMemoryState = self.memory[:index]+[value]+self.memory[index+1:]#https://www.geeksforgeeks.org/python-list-slicing/
        return ProgramState(self.pointer, newMemoryState, self.variableNamesDictionary, self.stack, self.tape, self.tapePointer)
    
    #changeStatePointer :: ProgramState -> int -> ProgramState
    def changeStatePointer(self, pointer: int) -> Self:
        return ProgramState(pointer, self.memory, self.variableNamesDictionary, self.stack, self.tape, self.tapePointer)
    
    #changeStateVariableNamesDictionary :: ProgramState -> String -> int -> ProgramState
    def changeStateVariableNamesDictionary(self, varName: string, pointer: int) -> Self:
        newVariableNamesDictionary = {**self.variableNamesDictionary, **{varName: pointer}}#https://favtutor.com/blogs/merge-dictionaries-python
        return ProgramState(self.pointer, self.memory, newVariableNamesDictionary, self.stack, self.tape, self.tapePointer)
    
    #removeVarFromVariableNamesDictionary :: ProgramState -> String -> ProgramState
    def removeVarFromVariableNamesDictionary(self, varName: string) -> Self:
        newVariableNamesDictionary = {key:val for key, val in self.variableNamesDictionary.items() if key != varName}
        return ProgramState(self.pointer, self.memory, newVariableNamesDictionary, self.stack, self.tape, self.tapePointer)
        
    #changeTapePointer :: ProgramState -> int -> ProgramState
    def changeTapePointer(self, tapePointer: int) -> Self:
        return ProgramState(self.pointer, self.memory, self.variableNamesDictionary, self.stack, self.tape, tapePointer)
        
    #changeTapeElement :: ProgramState -> int -> ProgramState
    def changeTapeElement(self, newElement: int) -> Self:
        return ProgramState(self.pointer, self.memory, self.variableNamesDictionary, self.stack, self.tape[:self.tapePointer]+[newElement]+self.tape[self.tapePointer+1:], self.tapePointer)
    
    #insertTapeElement :: ProgramState -> int -> ProgramState
    def insertTapeElement(self, newElement: int) -> Self:
        return ProgramState(self.pointer, self.memory, self.variableNamesDictionary, self.stack, self.tape[:self.tapePointer]+[newElement]+self.tape[self.tapePointer:], self.tapePointer)
    
    #__repr__ :: ProgramState -> String
    def __repr__(self) -> str:
        return "ptr: " + str(self.pointer) + " val: " + str(self.memory) + " varname dictionary: " + str(self.variableNamesDictionary)
    
    #__str__ :: ProgramState -> String    
    def __str__(self) -> str:
        return self.__repr__()  

#runABlock :: CodeBlock -> Integer -> ProgramState -> Callable -> CodeBlock -> (CodeBlock, Integer, ProgramState, Callable, CodeBlock)
@function_debug_printing
def runABlock(code: CodeBlock, codePtr: int, state: ProgramState, output: Callable, functions: CodeBlock) -> Tuple[CodeBlock, int, ProgramState, Callable, CodeBlock]:
    if(codePtr >= len(code.statements) or codePtr < 0):
        return code, codePtr, state, output, functions
    statement = code.statements[codePtr]
    
    if hasattr(statement, 'parameter1'):#check if object has parameter1
        try:
            if statement.parameter1 in state.variableNamesDictionary:
                parameter1_value = state.memory[state.variableNamesDictionary[statement.parameter1]]#gets the value from the memory
            else:
                parameter1_value = __builtins__[statement.instructionType.value](statement.parameter1)#casting the value to the correct type using the enum for the type(to cast to int, float, string and other ) #https://gist.github.com/mdogo/4947278
        except:
            raise Exception("Error: converting or getting parameter parameter1 from memory: " + statement.parameter1)
    if hasattr(statement, 'parameter2'):#check if object has parameter2
        try:
            if statement.parameter2 in state.variableNamesDictionary:
                parameter2_value = state.memory[state.variableNamesDictionary[statement.parameter2]]#gets the value from the memory
            else:
                parameter2_value = __builtins__[statement.instructionType.value](statement.parameter2)#casting the value to the correct type using the enum for the type(to cast to int, float, string and other ) #https://gist.github.com/mdogo/4947278 
        except:
            raise Exception("Error: converting or getting parameter parameter2 from memory: " + statement.parameter2)    
    if hasattr(statement, 'parameter3'):#check if object has parameter3
        try:
            if statement.parameter3 in state.variableNamesDictionary:
                parameter3_value = state.memory[state.variableNamesDictionary[statement.parameter3]]#gets the value from the memory
            else:
                parameter3_value = __builtins__[statement.instructionType.value](statement.parameter3)#casting the value to the correct type using the enum for the type(to cast to int, float, string and other ) #https://gist.github.com/mdogo/4947278
        except:
            raise Exception("Error: converting or getting parameter parameter3 from memory: " + statement.parameter3)
    
    match statement:        
        case CallFunction():
            result, output_ = runAFunction(state.memory[state.variableNamesDictionary[statement.functionInputVar]], statement.functionName, output, functions)
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.functionReturnVar], result)
            return runABlock(code, codePtr+1, newState, output_, functions)

        case CreateVar():
            if statement.name in state.variableNamesDictionary:
                raise Exception("error variable with the name: " + statement.name + " is already created")
            newState = state.changeStateMemory(state.pointer, 0)
            newState_ = newState.changeStateVariableNamesDictionary(statement.name, newState.pointer)
            newState__ = newState_.changeStatePointer(newState_.pointer+1)
            return runABlock(code, codePtr+1, newState__, output, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.GREATER):
            if parameter2_value > parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.LESS):
            if parameter2_value < parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.EQUAL):
            if parameter2_value == parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.NOTEQUAL):
            if parameter2_value != parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,codePtr+1,newState,output, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.GREATEREQUAL):
            if parameter2_value >= parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,codePtr+1,newState,output, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.LESSEQUAL):
            if parameter2_value <= parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,codePtr+1,newState,output, functions)
        
        case setValue():
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.plus):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value + parameter3_value)
            return runABlock(code,codePtr+1,newState,output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.minus):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value - parameter3_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.multiply):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value * parameter3_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.divide):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value / parameter3_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.modulo):  
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value % parameter3_value)          
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.andOp):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value & parameter3_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.orb):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value | parameter3_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.xor):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value ^ parameter3_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.xad):
            #https://deepai.org/machine-learning-glossary-and-terms/xand is it the same as xnor
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~(parameter2_value ^ parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.nad):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~(parameter2_value & parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.nor):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~(parameter2_value | parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,convertType=ConvertType.bitWiseNot):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~parameter2_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.maxVal):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], max(parameter2_value, parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.maxVal):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], min(parameter2_value, parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,convertType=ConvertType.roundNormal):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], round(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,convertType=ConvertType.roundCeiling):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.ceil(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,convertType=ConvertType.roundFloor):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.floor(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,mathFunctionType=MathFloatType.power):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.pow(parameter2_value, parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.sign):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.copysign(1, parameter2_value))# https://www.tutorialspoint.com/how-to-get-the-sign-of-an-integer-in-python
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.squareRoot):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.sqrt(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFloatFunctionType=MathFloatType.sin):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.sin(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.cos):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.cos(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.tan):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.tan(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicSin):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.sinh(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicCos):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.cosh(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicTan):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.tanh(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.logBase10):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.log10(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.logNatural):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.log(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,mathFunctionType=MathFloatType.log):  
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.log(parameter2_value, parameter3_value))
            return runABlock(code, codePtr+1, newState, output, functions)
            
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.eToPower):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.exp(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,convertType=ConvertType.absolute):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], abs(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,convertType=ConvertType.negative):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -parameter2_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseSin):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.asin(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseCos):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.acos(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseTan):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.atan(parameter2_value))
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case Tape(tapeAction=TapeAction.MoveLeft):#TODO fix tape implementation
            if state.tapePointer == 0:
                newState = state.insertTapeElement(math.nan)#insert blank
                pass
            else:
                newState = state.changeTapePointer(state.tapePointer-1)
            return runABlock(code, codePtr+1, newState, output, functions)
                
        case Tape(tapeAction=TapeAction.MoveRight):
            if (newState.tapePointer + 1) >= len(newState.tape)-1:
                newState = state.insertTapeElement(math.nan)#insert blank
            newState = state.changeTapePointer(state.tapePointer+1)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case Tape(tapeAction=TapeAction.ReadCurrentElementPosition):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], newState.tape[newState.tapePointer])
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case Tape(tapeAction=TapeAction.WriteElementToCurrentPosition):
            newState = state.changeTapeElement(parameter1_value)
            return runABlock(code, codePtr+1, newState, output, functions)
        
        case displayValue():
            if statement.nameVar in state.variableNamesDictionary:
                if statement.newLine:
                    newOutput = output(str(state.memory[state.variableNamesDictionary[statement.nameVar]]) + '\n')
                else:
                    newOutput = output(str(state.memory[state.variableNamesDictionary[statement.nameVar]]))
            else:
                if statement.newLine:
                    newOutput = output(str(statement.nameVar) + '\n')
                else:
                    newOutput = output(str(statement.nameVar))
            return runABlock(code, codePtr+1, state, newOutput, functions)
        
        case DeleteVar():
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.name], 0)
            newState_ = newState.removeVarFromVariableNamesDictionary(statement.name)
            return runABlock(code, codePtr+1, newState_, output, functions)
        
        case Loop(block=block,varConditionName=varConditionName,whileZero=False,loopAtLeastOnce=True,onlyOneTime=True):#fnc
            statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[codePtr].block, 0, state, output, functions)#loop only once
            if codePtr_ <= -1:
                    return code, codePtr, state_, output_, functions_
            return runABlock(code, codePtr+1, state_, output_, functions_)
        
        case Loop(block=block,varConditionName=varConditionName,whileZero=False,loopAtLeastOnce=False,onlyOneTime=True):#dif
            if state.memory[state.variableNamesDictionary[statement.varConditionName]] != 0:#only checks if statement is var name not if statement is int maybe implement in front code
                statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[codePtr].block, 0, state, output, functions)
                if codePtr_ <= -1:
                    return code, codePtr, state_, output_, functions_
                return runABlock(code, codePtr+1, state_, output_, functions_)
            return runABlock(code, codePtr+1, state, output, functions)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=True, loopAtLeastOnce=False, onlyOneTime=True):#nif
            if state.memory[state.variableNamesDictionary[statement.varConditionName]] == 0:#only checks if statement is var name not if statement is int maybe implement in front code
                statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[codePtr].block, 0, state, output, functions)
                if codePtr_ <= -1:
                    return code, codePtr, state_, output_, functions_
                return runABlock(code, codePtr+1, state_, output_, functions_)
            return runABlock(code, codePtr+1, state, output, functions)

        case Loop(block=block, varConditionName=varConditionName, whileZero=False, loopAtLeastOnce=False, onlyOneTime=False):#lpc # check if logic is good with if statement
            state_, output_ = runLoopWhileNotZero(code.statements[codePtr].block, state, output, statement.varConditionName, functions)
            return runABlock(code, codePtr+1, state_, output_, functions)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=True, loopAtLeastOnce=False, onlyOneTime=False):#lpn
            state_, output_ = runLoopWhileZero(code.statements[codePtr].block, state, output, statement.varConditionName, functions)# check if logic is good with if statement in function
            return runABlock(code, codePtr+1, state_, output_, functions)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=False, loopAtLeastOnce=True, onlyOneTime=False):#dlw
            statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[codePtr].block, 0, state, output, functions)#loop at least once
            state__, output__ = runLoopWhileNotZero(statementLoop, state_, output_, statement.varConditionName, functions_)
            return runABlock(code, codePtr+1, state__, output__, functions_)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=True, loopAtLeastOnce=True, onlyOneTime=False):#dlu
            statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[codePtr].block, 0, state, output, functions)#loop at least once
            state__, output__ = runLoopWhileZero(statementLoop, state_, output_, statement.varConditionName, functions_)
            return runABlock(code, codePtr+1, state__, output__, functions_)
        
        case ReturnFunction():
            newState = state.changeStateMemory(0, parameter1_value)
            newCodePtr = -1
            return code, newCodePtr, newState, output, functions
        
        case NotImplemented(ignore=True):
            #statement is not implemented and not really important so ignore it
            return runABlock(code, codePtr+1, state, output, functions)
        
        case NotImplemented() | _:
            raise Exception("method not implemented")
        

#runAFunction :: String -> String -> Callable -> CodeBlock -> (int, Callable)
@function_debug_printing
def runAFunction(functionInputVarValue: str, functionName: str, output: Callable, functions: CodeBlock) -> Tuple[int,Callable]:
    functionCodes = list(filter(lambda x: isinstance(x, DeclareFunction) and x.functionName == functionName, functions.statements))
    if len(functionCodes) == 0:
        #There is no function declared with that name
        raise Exception("error, no function declared with the name: " + functionName + '\n')
    else:
        functionCode = functionCodes[0]
    # create a new state for the function and copy the variables from the current state to the function state(input var)
    functionState = ProgramState().changeStateMemory(1, functionInputVarValue)
    functionState_ = functionState.changeStateVariableNamesDictionary(functionCode.functionInputVar, functionState.pointer)
    functionState__ = functionState_.changeStatePointer(functionState_.pointer+1)
    code_, codePtr_, functionState___, newOutput, functions_ = runABlock(functionCode.block, 0, functionState__, output, functions)
    return functionState___.memory[0], newOutput#in place 0 in the memory is always the return var(only one return var supported)

#runLoopWhileZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
@function_debug_printing
def runLoopWhileZero(loop : CodeBlock, state: ProgramState, output : Callable, loopName : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    if state.memory[state.variableNamesDictionary[loopName]] == 0:
        loop_, codePtr_, state_, output_, functions_ = runABlock(loop.code, 0, state, output, functions)
        return runLoopWhileZero(loop_, state_, output_, loopName, functions_)
    else:
        return state, output

#runLoopWhileNotZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
@function_debug_printing
def runLoopWhileNotZero(loop : CodeBlock, state: ProgramState, output : Callable, loopName : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    if state.memory[state.variableNamesDictionary[loopName]] != 0:
        loop_, codePtr_, state_, output_, functions_ = runABlock(loop, 0, state, output, functions)
        return runLoopWhileNotZero(loop_, state_, output_, loopName, functions_)
    else:
        return state, output