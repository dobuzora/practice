# 16.ファイルをN分割する

# split -l 5 hightemp.txt

import sys

args = sys.argv

if len(args) != 3:
    print(erorr)
    exit()

with open(args[2],'r') as f:
    count = 0
    for line in f:
        print(line,end="")
        count += 1
        if count == int(args[1]):
            print("+++++++++++++++++++++++++++++++")
            count = 0

f.close()


