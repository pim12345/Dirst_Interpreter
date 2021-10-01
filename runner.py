from typing import List, Tuple
from tokens import *
from lexer import *
from Parser import *


def runner(parse):
    pass


class ProgramState():
    pass


#runloop :: Loop -> ProgramState -> String -> (ProgramState, String)
def runloop(loop : Loop, state: ProgramState, output : str) -> Tuple[ProgramState, str]:
    #print("loop")
    if(state.memory[state.pointer]==0):
        return state,output
    else:
        state_, output_ = runBlock(loop.code,0,state,output)
        return runloop(loop, state_, output_)


def runABlock():
    pass


