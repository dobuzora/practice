# 13.col1.txtとcol2.txtをマージ

# paste col1.txt col2.txt 

import sys

args = sys.argv

if len(args) != 4:
    print("failed")
    exit()

f = open(args[1],"r")

with open(args[2],"r") as f1:
    with open(args[3],"r") as f2:
        for _ in f:
            print(f1.readline().rstrip("\n") + " " + f2.readline().rstrip("\n"))


