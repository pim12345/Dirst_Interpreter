import os 

#add haskall notation todo
def readFile(filename : str) -> str:
    with open(filename, 'r') as f:
        return f.readlines()

class PrintingOutput:
    def __init__(self) -> None:
        self.output = ""
    
    def __call__(self, text):
        self.output += text
        return self.output

#add haskall notation todo
# def readFile(filename : str) -> str:
#     print("test")
#     print("Path at terminal when executing this file")
#     print(os.getcwd() + "\n")

#     print("This file path, relative to os.getcwd()")
#     print(__file__ + "\n")

#     print("This file full path (following symlinks)")
#     full_path = os.path.realpath(__file__)
#     print(full_path + "\n")

#     print("This file directory and name")
#     path, filename = os.path.split(full_path)
#     print(path + ' --> ' + filename + "\n")

#     print("This file directory only")
#     print(os.path.dirname(full_path))
#     print(2)
#     with open(os.path.join(os.getcwd() , filename), 'r') as f:
#         return f.readlines()