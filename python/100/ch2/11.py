# 11.タブをスペースに置換

# cat hightemp.txt | sed  s/$'\t'/" "/g

import re
import sys

args = sys.argv

if len(args) != 2:
    print("failed")

f = open(args[1],'r')
for line in f:
    print(line.replace('\t',' '),end="")


