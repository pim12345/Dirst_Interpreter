from Lexer.tokens import *
from Lexer.lexer import *
from Parser.parser import *
from Tools.tools import *
from Runner.runner import *
import sys

#main :: None -> None
def main() -> None:
    print("Running Dirst CLI")
    match sys.argv:
        case [_,'-f', scriptLocation]:
            print("Running script: ", scriptLocation)
            consolePrinting = PrintingOutput()
            fileTree = readFile(os.path.join(os.getcwd() , scriptLocation))
            consoleInput = ""#no input provided
            lex_output = lex(fileTree, consoleInput)
            tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
            code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
            print(output)
            print("program end, exiting...")
            exit(0)
            
        case [_,'-f', scriptLocation, '-i', consoleInput]:
            print("Running script: ", scriptLocation, " with input: ", consoleInput)
            consolePrinting = PrintingOutput()
            fileTree = readFile(os.path.join(os.getcwd() , scriptLocation))
            lex_output = lex(fileTree, consoleInput)
            tokens, parsedCode, parsedFunctions = parseCodeBlock(lex_output, CodeBlock(), CodeBlock())
            code, codePtr, state, output, functions = runABlock(parsedCode, 0, ProgramState(), consolePrinting, parsedFunctions)
            print(output)
            print("program end, exiting...")
            exit(0)
        case _:
            print("Unknown or no command selected. Exiting...")
            exit(1)


if __name__ == "__main__":
    main()