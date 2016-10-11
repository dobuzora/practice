# 14.先頭からN行を出力

# head -n 4 hightemp.txt

import sys

args = sys.argv

if len(args) != 3:
    print("failed")
    exit()

f = open(args[2],"r")

for _ in range(int(args[1])):
    print(f.readline(),end="")
