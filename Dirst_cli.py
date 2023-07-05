from Lexer.tokens import *
from Lexer.lexer import *
from Runner.runner import *
from Parser.parser import *
import sys

#main :: None -> None
def main() -> None:
    match sys.argv:
        case [_,'-f', scriptLocation]:
            console_printing_INFO = lambda *args: print(*args)
            runABlock(parseCodeBlock(lex(open(scriptLocation, "r")), CodeBlock())[1], 0, ProgramState(), console_printing_INFO)
            exit(0)
        case _:
            print("Unknown command selected. Exiting...")
            exit(1)




if __name__ == "__main__":
    main()