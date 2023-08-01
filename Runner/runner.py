from typing import List, Tuple, Callable, Self, Any
from Lexer.tokens import *
from Lexer.lexer import *
from Parser.parser import *
from Tools.tools import *
import math
from operator import xor
import random
import copy#todo check of niet standaard package is anders ff toevoegen aan requirements.txt

class ProgramState():
    def __init__(self, pointer: int=1, memory: List[int]=[math.nan]*10, variableNamesDictionary: dict={}, stack: List[int]=[], tape: List[int]=[math.nan], tapePointer: int=0):#overloading didnt work so this is the solution
        self.pointer = pointer#need to clear register 0 for loops and arguments
        self.memory = memory#om de 2 registers is eerste de identifyer de 2e is de variable value
        self.variableNamesDictionary = variableNamesDictionary
        self.stack = stack#todo idk if good if add so, os maybe remove
        self.tape = tape#todo idk if good if add so, os maybe remove
        self.tapePointer = tapePointer#todo idk if good if add so, os maybe remove
    
    #changeStatePointer :: ProgramState -> int -> ProgramState
    def changeStateMemory(self, index: int, value: int ) -> Self:#todo add string type to value
        #self.memory[index] = value
        #this is because of functional programming
        newMemoryState = self.memory[:index]+[value]+self.memory[index+1:]#https://www.geeksforgeeks.org/python-list-slicing/
        
        return ProgramState(self.pointer, newMemoryState, self.variableNamesDictionary, self.stack, self.tape, self.tapePointer)
    
    #changeStatePointer :: ProgramState -> int -> ProgramState
    def changeStatePointer(self, pointer: int) -> Self:
        #self.pointer = pointer
        return ProgramState(pointer, self.memory, self.variableNamesDictionary, self.stack, self.tape, self.tapePointer)
    
    #changeStateVariableNamesDictionary :: ProgramState -> String -> int -> ProgramState
    def changeStateVariableNamesDictionary(self, varName: string, pointer: int) -> Self:
        #self.variableNamesDictionary[varName] = pointer
        newVariableNamesDictionary = {**self.variableNamesDictionary, **{varName: pointer}}#https://favtutor.com/blogs/merge-dictionaries-python
        return ProgramState(self.pointer, self.memory, newVariableNamesDictionary, self.stack, self.tape, self.tapePointer)
        #return ProgramState(self.pointer, self.memory, {**self.variableNamesDictionary, **{varName: pointer}}, self.stack, self.tape, self.tapePointer)
    
    def removeVarFromVariableNamesDictionary(self, varName: string) -> Self:
        newVariableNamesDictionary = {key:val for key, val in self.variableNamesDictionary.items() if key != varName}
        return ProgramState(self.pointer, self.memory, newVariableNamesDictionary, self.stack, self.tape, self.tapePointer)
        
    #__repr__ :: ProgramState -> String
    def __repr__(self) -> str:
        return "ptr: " + str(self.pointer) + " val: " + str(self.memory) + " varname dictionary: " + str(self.variableNamesDictionary)


#runABlock :: CodeBlock -> Integer -> ProgramState -> Callable -> CodeBlock -> (CodeBlock, Integer, ProgramState, Callable)
def runABlock(code: CodeBlock, codePtr: int, state: ProgramState, output: Callable, functions: CodeBlock) -> Tuple[CodeBlock, int, ProgramState, Callable, CodeBlock]:
    if(codePtr >= len(code.statements) or codePtr < 0):
        return code, codePtr, state, output, functions
    statement = code.statements[codePtr]
    #newState = copy.deepcopy(state)#cant change original variable, and python is bad with constant and normal copy, this is slower but works
    newOutput = copy.deepcopy(output)#cant change original variable, and python is bad with constant and normal copy(is by classes a pointer), this is slower but works
    newCodePtr = codePtr#cant change original variable, and python is bad with constant and normal copy, this is slower but works
    #todo add check if value is the same as the type(like int is int and not string)
    #todo check wat te doen met parameter 1 wel of niet casten
    
    
    #todo check if conversion from parameter 1 is good
    if hasattr(statement, 'parameter1'):#check if object has parameter1
        if statement.parameter1 in state.variableNamesDictionary:
            parameter1_value = state.memory[state.variableNamesDictionary[statement.parameter1]]
        else:
            print("test")
            parameter1_value = __builtins__[statement.instructionType.value](statement.parameter1)
    
    if hasattr(statement, 'parameter2'):#check if object has parameter2
        if statement.parameter2 in state.variableNamesDictionary:
            parameter2_value = state.memory[state.variableNamesDictionary[statement.parameter2]]
        else:
            parameter2_value = __builtins__[statement.instructionType.value](statement.parameter2)#https://gist.github.com/mdogo/4947278 #todo check safety of this, and of allowed to use this
            #parameter2_value = statement.instructionType(statement.parameter2)#todo check if casting works, and if it works add documentation
            
    if hasattr(statement, 'parameter3'):#check if object has parameter3
        if statement.parameter3 in state.variableNamesDictionary:
            parameter3_value = state.memory[state.variableNamesDictionary[statement.parameter3]]
        else:
            parameter3_value = __builtins__[statement.instructionType.value](statement.parameter3)#todo check if casting works, and if it works add documentation #https://gist.github.com/mdogo/4947278
    
    
    
    match statement:
        #case DeclareFunction():
            #todo check if there is already a function with that name(with count or something)
            # if statement.functionName in newState.variableNamesDictionary:
            #     newOutput("error function with the name: ", statement.name , " is already created")
            #     return code, newCodePtr, newState, newOutput, functions
            # newState.memory[newState.pointer]=0#todo check of wel goed doe en of wel nodig is, misch apparte dictionary of gewoon ignoren en alleen checken bij call
            # newState.variableNamesDictionary[statement.functionName] = newState.pointer
            # newState.pointer+=1
            #return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        case CallFunction():
            result, output_ = runAFunction(state.memory[state.variableNamesDictionary[statement.functionInputVar]], statement.functionReturnVar, statement.functionName, newOutput, functions)
            #newState.memory[newState.variableNamesDictionary[statement.functionReturnVar]] = result
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.functionReturnVar], result)#todo check if good functional programming
            # newCodePtr = len(code.statements)+1#todo change after running a function to set the pointer to end of all the underlining functions
            # return code, newCodePtr, newState, newOutput, functions
            return runABlock(code, newCodePtr+1, newState, output_, functions)#todo change after running a function to set the pointer to end of all the underlining functions

        case createVar():
            if statement.name in state.variableNamesDictionary:
                newOutput("error variable with the name: " + statement.name + " is already created")
                return code, newCodePtr, state, newOutput, functions
            newState = state.changeStateMemory(state.pointer, 0)
            #newState.memory[newState.pointer]=0
            newState_ = newState.changeStateVariableNamesDictionary(statement.name, newState.pointer)
            #newState.variableNamesDictionary[statement.name] = newState.pointer
            newState__ = newState_.changeStatePointer(newState_.pointer+1)
            #newState.pointer+=1
            return runABlock(code, newCodePtr+1, newState__, newOutput, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.GREATER):
            if parameter2_value > parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -1
            else:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = 0
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.LESS):
            if parameter2_value < parameter3_value:
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -1
            else:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = 0
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.EQUAL):
            if parameter2_value == parameter3_value:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -1
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = 0
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,newCodePtr+1,newState,newOutput, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.NOTEQUAL):
            if parameter2_value != parameter3_value:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -1
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = 0
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,newCodePtr+1,newState,newOutput, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.GREATEREQUAL):
            if parameter2_value >= parameter3_value:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -1
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = 0
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,newCodePtr+1,newState,newOutput, functions)
        
        case IfStatement(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,condition=IfStatementType.LESSEQUAL):
            if parameter2_value <= parameter3_value:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -1
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -1)
            else:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = 0
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], 0)
            return runABlock(code,newCodePtr+1,newState,newOutput, functions)
        
        case setValue():
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.plus):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value + parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value + parameter3_value
            return runABlock(code,newCodePtr+1,newState,newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.minus):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value - parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value - parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.multiply):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value * parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value * parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.divide):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value / parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value / parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.modulo):  
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value % parameter3_value)          
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value % parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.andOp):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value & parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value & parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.orb):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value | parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value | parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.xor):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], parameter2_value ^ parameter3_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = parameter2_value ^ parameter3_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.xad):
            #https://deepai.org/machine-learning-glossary-and-terms/xand is it the same as xnor
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~(parameter2_value ^ parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = ~(parameter2_value ^ parameter3_value)#todo test if good
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.nad):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~(parameter2_value & parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = ~(parameter2_value & parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.nor):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~(parameter2_value | parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = ~(parameter2_value | parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.bitWiseNot):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], ~parameter2_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = ~parameter2_value
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.maxVal):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], max(parameter2_value, parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = max(parameter2_value, parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case operators(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,operatorType=operatorsType.maxVal):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], min(parameter2_value, parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = min(parameter2_value, parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case roundValue():
            if statement.roundToCeiling == True:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.ceil(parameter2_value)
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.ceil(parameter2_value))
            else:
                #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.floor(parameter2_value)
                newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.floor(parameter2_value))
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,mathFunctionType=MathFloatType.power):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.pow(parameter2_value, parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.pow(parameter2_value, parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.sign):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.copysign(1, parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.copysign(1, parameter2_value)#todo check if good use of sign https://www.tutorialspoint.com/how-to-get-the-sign-of-an-integer-in-python
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.squareRoot):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.sqrt(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.sqrt(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFloatFunctionType=MathFloatType.sin):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.sin(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.sin(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.cos):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.cos(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.cos(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.tan):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.tan(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.tan(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicSin):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.sinh(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.sinh(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicCos):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.cosh(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.cosh(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.hyperbolicTan):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.tanh(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.tanh(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.logBase10):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.log10(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.log10(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.logNatural):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.log(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.log(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,mathFunctionType=MathFloatType.log):  
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.log(parameter2_value, parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.log(parameter2_value, parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
            
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.eToPower):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.exp(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.exp(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.absolute):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], abs(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = abs(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.negative):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], -parameter2_value)
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = -parameter2_value#todo need to test if good negative value, otherwise use ~abs
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
            
        case valueConv(parameter1=parameter1,parameter2=parameter2,parameter3=parameter3,convertType=ConvertType.RANDOM):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], random.randint(parameter2_value, parameter3_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = random.randint(parameter2_value, parameter3_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseSin):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.asin(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.asin(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseCos):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.acos(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.acos(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case mathFloatFunctions(parameter1=parameter1,parameter2=parameter2,mathFunctionType=MathFloatType.inverseTan):
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], math.atan(parameter2_value))
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = math.atan(parameter2_value)
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case Tape(tapeAction=TapeAction.MoveLeft):#todo fix tape implementation
            if newState.tapePointer == 0:#todo make more functional with functions in state
                newState.tape.insert(0,math.nan)#insert blank
            else:
                newState.tapePointer-=1
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
                
        case Tape(tapeAction=TapeAction.MoveRight):#todo make more functional with functions in state
            if (newState.tapePointer + 1) >= len(newState.tape)-1:#todo fix tape implementation
                newState.tape.append(math.nan)
            newState.tapePointer+=1
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case Tape(tapeAction=TapeAction.ReadCurrentElementPosition):#todo fix tape implementation
            #newState.memory[newState.variableNamesDictionary[statement.parameter1]] = newState.tape[newState.tapePointer]
            #newState = state.changeStateMemory(state.variableNamesDictionary[statement.parameter1], newState.tape[newState.tapePointer])
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case Tape(tapeAction=TapeAction.WriteElementToCurrentPosition):#todo fix tape implementation
            #newState.tape[newState.tapePointer] = newState.memory[newState.variableNamesDictionary[statement.parameter1]]
            #newState = state.changeStateTape(newState.tapePointer, newState.memory[newState.variableNamesDictionary[statement.parameter1]])
            return runABlock(code, newCodePtr+1, newState, newOutput, functions)
        
        case displayValue():
            #print(statement.value)
            #print(str(newState.memory[newState.variableNamesDictionary[statement.value]]))
            #todo convert to new type system
            if statement.nameVar in state.variableNamesDictionary:#todo check if good
                if statement.newLine:
                    newOutput(str(state.memory[state.variableNamesDictionary[statement.nameVar]]) + '\n')
                else:
                    newOutput(str(state.memory[state.variableNamesDictionary[statement.nameVar]]))
            else:
                if statement.newLine:
                    newOutput(str(statement.nameVar) + '\n')
                else:
                    newOutput(str(statement.nameVar))
            #newOutput(newState.memory[newState.variableNamesDictionary[statement.nameVar]])
            #newOutput = str(newState.memory[newState.variableNamesDictionary[statement.value]]) + '\n'
            return runABlock(code, newCodePtr+1, state, newOutput, functions)
        
        case deleteVar():
            newState = state.changeStateMemory(state.variableNamesDictionary[statement.name], 0)
            #del newState.variableNamesDictionary[statement.name]
            #newState_ = newState.changeStatePointer(newState.pointer-1)
            newState_ = newState.removeVarFromVariableNamesDictionary(statement.name)
            return runABlock(code, newCodePtr+1, newState_, newOutput, functions)
        
        case Loop(block=block,varConditionName=varConditionName,whileZero=False,loopAtLeastOnce=True,onlyOneTime=True):#fnc
            statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[newCodePtr].block, 0, state, newOutput, functions)#loop only once needs work!!!!!!!!!!!!!!!
            if codePtr_ <= -1:#todo add logic in begin if that works and other in other loop functions
                    return code, newCodePtr, state_, output_, functions_
            return runABlock(code, newCodePtr+1, state_, output_, functions_)
        
        case Loop(block=block,varConditionName=varConditionName,whileZero=False,loopAtLeastOnce=False,onlyOneTime=True):#dif
            if state.memory[state.variableNamesDictionary[statement.varConditionName]] != 0:#only checks if statement is var name not if statement is int maybe implement in front code
                statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[newCodePtr].block, 0, state, newOutput, functions)
                if codePtr_ <= -1:#todo add logic in begin if that works and other in other loop functions
                    return code, newCodePtr, state_, output_, functions_
                return runABlock(code, newCodePtr+1, state_, output_, functions_)
            return runABlock(code, newCodePtr+1, state, newOutput, functions)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=True, loopAtLeastOnce=False, onlyOneTime=True):#nif
            if state.memory[state.variableNamesDictionary[statement.varConditionName]] == 0:#only checks if statement is var name not if statement is int maybe implement in front code
                statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[newCodePtr].block, 0, state, newOutput, functions)
                if codePtr_ <= -1:#todo add logic in begin if that works and other in other loop functions
                    return code, newCodePtr, state_, output_, functions_
                return runABlock(code, newCodePtr+1, state_, output_, functions_)
            return runABlock(code, newCodePtr+1, state, newOutput, functions)

        case Loop(block=block, varConditionName=varConditionName, whileZero=False, loopAtLeastOnce=False, onlyOneTime=False):#lpc # check if logic is good with if statement
            state_, output_ = runLoopWhileNotZero(code.statements[newCodePtr].block, state, newOutput, statement.varConditionName, functions)
            return runABlock(code, newCodePtr+1, state_, output_, functions)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=True, loopAtLeastOnce=False, onlyOneTime=False):#lpn
            state_, output_ = runLoopWhileZero(code.statements[newCodePtr].block, state, newOutput, statement.varConditionName, functions)# check if logic is good with if statement in function
            return runABlock(code, newCodePtr+1, state_, output_, functions)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=False, loopAtLeastOnce=True, onlyOneTime=False):#dlw
            statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[newCodePtr].block, 0, state, newOutput, functions)#loop at least once
            state__, output__ = runLoopWhileNotZero(statementLoop, state_, output_, statement.varConditionName, functions_)
            return runABlock(code, newCodePtr+1, state__, output__, functions_)
        
        case Loop(block=block, varConditionName=varConditionName, whileZero=True, loopAtLeastOnce=True, onlyOneTime=False):#dlu
            statementLoop, codePtr_, state_, output_, functions_ = runABlock(code.statements[newCodePtr].block, 0, state, newOutput, functions)#loop at least once
            state__, output__ = runLoopWhileZero(statementLoop, state_, output_, statement.varConditionName, functions_)
            return runABlock(code, newCodePtr+1, state__, output__, functions_)
        
        case ReturnFunction():
            #if statement.parameter1.isdigit():
                #newState = state.changeStateMemory(0, int(statement.parameter1))
                #newState.memory[0] = int(statement.parameter1)#always return on 0 place in memory is always the return var, only 1 return var supported
            #else:#newState.variableNamesDictionary["result"]
                #newState.memory[0] = newState.memory[newState.variableNamesDictionary[statement.parameter1]]#todo add maybe check if in var in dictionary and otherwise error
            newState = state.changeStateMemory(0, parameter1_value)    
            newCodePtr = -1
            return code, newCodePtr, newState, newOutput, functions
        
        case NotImplemented(ignore=True):
            #statement is not implemented and not really important so ignore it
            return runABlock(code, newCodePtr+1, state, output, functions)
        
        case NotImplemented() | _:
            
            newOutput("method not implemented" + '\n')
            return code, newCodePtr, state, newOutput, functions

#runAFunction :: str -> int -> Callable -> (int, Callable)
def runAFunction(functionInputVarValue: str, functionReturnVar : str, functionName: str, output: Callable, functions: CodeBlock) -> Tuple[int,Callable]:
    functionCodes = list(filter(lambda x: isinstance(x, DeclareFunction) and x.functionName == functionName, functions.statements))
    if len(functionCodes) == 0:
        #There is no function declared with that name
        newOutput = copy.deepcopy(output)
        newOutput("error, no function declared with the name: " + functionName + '\n')
        return -1, newOutput#todo add return code if error encountered
    else:
        functionCode = functionCodes[0]
    # create a new state for the function
    functionState = ProgramState()
    # copy the variables from the current state to the function state(input var)
    functionState.memory[functionState.pointer]=functionInputVarValue
    functionState.variableNamesDictionary[functionCode.functionInputVar] = functionState.pointer
    functionState.pointer+=1
    
    #functionState.memory[functionState.pointer]=0
    #functionState.variableNamesDictionary[functionReturnVar] = functionState.pointer
    #functionState.pointer+=1
    #todo check if return var exists, if is an digit also add check if it is a digit and return that directly
    code_, codePtr_, functionState_, newOutput, functions_ = runABlock(functionCode.block, 0, functionState, output, functions)#todo make it smarter like runloop functions so it requires less hackery
    return functionState_.memory[0], newOutput#in place 0 in the memory is always the return var(only one return var supported)

#runLoopWhileZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileZero(loop : CodeBlock, state: ProgramState, output : Callable, loopName : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    if state.memory[state.variableNamesDictionary[loopName]] == 0:
        loop_, codePtr_, state_, output_, functions_ = runABlock(loop.code, 0, state, output, functions)
        return runLoopWhileZero(loop_, state_, output_, loopName, functions_)
    else:
        return state, output#todo is this correct functional programming?

#runLoopWhileNotZero :: CodeBlock -> ProgramState -> Callable -> String -> (ProgramState, Callable)
def runLoopWhileNotZero(loop : CodeBlock, state: ProgramState, output : Callable, loopName : str, functions: CodeBlock) -> Tuple[ProgramState, Callable]:
    if state.memory[state.variableNamesDictionary[loopName]] != 0:
        loop_, codePtr_, state_, output_, functions_ = runABlock(loop, 0, state, output, functions)
        return runLoopWhileNotZero(loop_, state_, output_, loopName, functions_)
    else:
        return state, output