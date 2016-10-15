# 20.JSONデータの読み込み
# coding: utf-8

import sys
import re

args = sys.argv

match_str = u'イギリス'

with open(args[1],'r') as f:
    for line in f:
        matchOB =  re.search(match_str,line)
        if matchOB:
            print(line,end='')
f.close()
