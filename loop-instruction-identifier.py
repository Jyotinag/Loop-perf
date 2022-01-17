import os
import errno
import subprocess

#reading the c/c++ file
#returns a string 
def read_c_file():
    try:
        fileName = input()
        with open(fileName) as file:
            file_contents = file.read()
            #print(file_contents)
        return file_contents, fileName
    except:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), fileName
        )

def convert_string(stringFile):
    li = stringFile.split("\n")
    return li

def id_loops(contentList):
    loopList = []
    indexList = []
    for line in contentList:
        if "for" in line:
            loopList.append(line)
            indexList.append(contentList.index(line))
        elif "while" in line:
            loopList.append(line)
            indexList.append(contentList.index(line))
    return indexList, loopList

def perforarte_loop(loopList):
    perforated = []
    for loop in loopList:
        index = loopList.index(loop)
        loop = loop.replace("++","+=10")
        loopList[index] = loop

def make_perforated_file(indexList, contentList, loopList):
    for i in range(0,len(indexList)):
        contentList[indexList[i]] = loopList[i]
    perforatedFile = open("perf.c","w")
    for element in contentList:
        perforatedFile.write(element +"\n")
    # print(contentList)
    return contentList

def analysis_perf(perfFileName, fileName):
    subprocess.check_call(
    ('gcc', perfFileName),
    stdin=subprocess.DEVNULL)

    with open('input.txt') as infile, open('outputperf.txt', 'w') as outfile:
        subprocess.check_call(
            ('./a.out',),
            stdin=infile,
            stdout=outfile,
            universal_newlines=True)
    
    subprocess.check_call(
    ('gcc', fileName),
    stdin=subprocess.DEVNULL)

    with open('input.txt') as infile, open('output.txt', 'w') as outfile:
        subprocess.check_call(
            ('./a.out',),
            stdin=infile,
            stdout=outfile,
            universal_newlines=True)

def error_metrice(resExact, resPerf):
    ratio = abs(float(resExact)-float(resPerf))/float(resExact)
    return ratio

def error_management():
    try:
        with open("outputperf.txt","r") as perfFile:
            resPerf = perfFile.read()
            resPerf.replace('\n','')
        with open("output.txt","r") as exactFile:
            resExact = exactFile.read()
            resExact.replace('\n','')
        return resExact,resPerf
    except:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), "outputperf.txt", "output.txt"
        )
        


#the main function
def main():
    file_contents, fileName = read_c_file()
    content_list = convert_string(file_contents)
    # print(content_list)
    indexList, loopList = id_loops(content_list)
    perforarte_loop(loopList)
    perf = make_perforated_file(indexList,content_list,loopList)
    analysis_perf("perf.c", fileName)
    resExact,resPerf = error_management()
    print(resExact)
    print(resPerf)
    print(error_metrice(resExact,resPerf))
    # print(loopList)
    # print(indexList)
    # print(type(file_contents))

if __name__=='__main__':
    main()
