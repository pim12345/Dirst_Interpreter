#add haskall notation todo
def readFile(filename : str) -> str:
    with open(filename, 'r') as f:
        return f.readlines()
