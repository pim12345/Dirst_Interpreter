#from typing import Tuple, List, Callable, Union, TypeVar, Optional
#from functools import reduce
from tokens import *
from lexer import *
from runner import *
from Parser import *
#import logging
import sys


def main():
    cmdargs = sys.argv
    print(len(cmdargs))
    print(type(cmdargs))
    #print(cmdargs[1])
    match cmdargs:
        case [_,'-f', scriptLocation]:
            #print(scriptLocation)
            console_printing_INFO = lambda *args: print(*args)
            fileTree = open(scriptLocation, "r")
            lex_output = lex(fileTree)
            fileTree.close()
            parse = parseCodeBlock(lex_output, CodeBlock())[1]
            runABlock(parse, 0, ProgramState(), console_printing_INFO)
            exit(0)
        case filename,'test','test':
            print("test")
        case _:
            print("Unknown command selected. Exiting...")
            exit(1)




if __name__ == "__main__":
    main()