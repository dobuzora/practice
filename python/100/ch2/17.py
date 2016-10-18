# 17.一行目の文字列の異なり

# cut -f1 hightmap.txt | sort | uniq

import sys

args = sys.argv

str_set = []


with open(args[1],'r') as f:
    for line in f:
        str_set.append(line.split()[0])
        
print("\n".join(sorted(set(str_set))))


