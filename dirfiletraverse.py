import os

rootDir = '.'
for dirName, SubdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith('.py'):
            print(fname)