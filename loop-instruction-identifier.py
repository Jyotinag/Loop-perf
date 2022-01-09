import os
import re
import pandas as pd
import errno

#reading the c/c++ file
#returns a string 
def read_c_file():
    try:
        fileName = input()
        with open(fileName) as file:
            file_contents = file.read()
            #print(file_contents)
        return file_contents
    except:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), fileName
        )

def convert_string(stringFile):
    li = stringFile.split("\n")
    return li

def id_loops(contentList):
    loopList = []
    for line in contentList:
        if "for" in line:
            loopList.append(line)
        elif "while" in line:
            loopList.append(line)
    
    for loop in loopList:
        loop = loop.replace(" ","")
        loop = loop.replace("(","")
        loop = loop.replace(")","")
        loop = loop.replace("{","")
        loop = loop.replace("i++","i+=2")
        print(loop)
        
    return loopList


#the main function
def main():
    file_contents = read_c_file()
    content_list = convert_string(file_contents)
    # print(content_list)
    loopList = id_loops(content_list)
    print(loopList)
    print(type(file_contents))

if __name__=='__main__':
    main()
