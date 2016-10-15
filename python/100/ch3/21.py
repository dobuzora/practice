# 21.カテゴリ名含む行を抽出

import sys
import re

args = sys.argv

#[[:Category:

match_str = "\[\[:?Category:"

with open(args[1],'r') as f:
    for line in f:
        matchOB = re.search(match_str,line)
        if matchOB:
            print(line)
f.close()
