# 18.各行の３コラム目の数値の降順にソート

data = [line.split("\t") for line in open("hightemp.txt")]
for line in sorted(data,key=lambda x: float(x[2])):
    print("\t".join(line),end="")
