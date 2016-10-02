import random

def importCSV(fileName):
    inStream = open(fileName, 'r')
    lines = inStream.readlines()
    inStream.close()
    return lines

def cleanUp(L):
    for w in range(len(L)):
        L[w] = L[w].strip()
        L[w] = L[w].strip( "\n" )
        L[w] = L[w].strip( "\r" )
        if ('"' in L[w][0]):
            L[w] = L[w].split( '"' )[1:]
            L[w][1] = L[w][1][1:]
        else:
            L[w] = L[w].split( ',' )
    return L

def convertToDict(fileName):
    L = cleanUp(importCSV(fileName))
    D = dict()
    for subL in L:
        D[subL[0]] = subL[1]
    return D

def editFile(string, filename):
    outstream = open(filename,'a')
    outstream.write(string)
    outstream.close()
