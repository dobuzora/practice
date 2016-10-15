# 22.カテゴリ名の抽出

import sys
import re

args = sys.argv

category = re.compile('\[\[:?Category:(.*?)\]\]')

with open(args[1],'r') as f:
    for line in f:
        match = category.search(line)
        if match:
            print(match.group(1))
f.close()
