# 12.1行目をcol1.txtに,2行目をcol2.txtに保存

# cut -f1 hightemp.txt > col1.txt && cut -f2 hightemp.txt > col2.txt

import sys

args = sys.argv

if len(args) != 2:
    print('failed')
    exit()

# ファイル読み込み
f = open(args[1],'r')

# ファイルハンドル
with open('col1.txt','w') as f1:
    with open('col2.txt','w') as f2:
        for line in f:
            line_list = line.split()
            f1.write(line_list[0] + "\n")
            f2.write(line_list[1] + "\n")



