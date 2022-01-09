import os
import re
import pandas as pd

fileName = input()
with open(fileName) as file:
    file_contents = file.readline()
    #print(file_contents)

loops = []    
for line in file_contents:
    print(line)
    if "for" in line:
        loops.append(line)
print(loops)

