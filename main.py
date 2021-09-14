import re
fileTree = open("Fib_seq.txt", "r")

#print(fileTree.read())

def lex(file):
    #now no folder support
    lex_output_list = []
    for line in file:
        line = line.replace('\n',"") #remove newline from string.
        #print(re.split(r'([\t\._])', line))#met de punten en _ in de lijst 
        #print(re.split(r'_|\.|\t', line))#zonder punten en _ in de lijst
        lex_output_list.append(re.split(r'_|\.|\t', line))
    print(lex_output_list)
        


lex(fileTree)
fileTree.close()
