import os 

#add haskall notation todo
# def readFile(filename : str) -> str:
#     with open(filename, 'r') as f:
#         return f.readlines()


#add haskall notation todo
def readFile(filename : str) -> str:
    with open(os.path.join(os.getcwd() , filename), 'r') as f:
        return f.readlines()