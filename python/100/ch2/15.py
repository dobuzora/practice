# 末尾のN行を出力

# tail -n 5 hightemp.txt

import sys

args = sys.argv

if len(args) != 3:
    print('failed')
    exit()

f = open(args[2],"r")

count = sum(1 for line in f) 
f.close()

with open(args[2],"r") as f:
    lines = 0
    for line in f:
        lines += 1
        if (lines > count - int(args[1])):
            print(line,end="")

f.close()
