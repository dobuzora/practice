# 10.行数のカウント

import sys

args = sys.argv

# 引数チェック
if len(args) != 2:
    print("failed")

f = open(args[1],'r')

count = 0
for line in f:
    count += 1

print(count)

f.close()
