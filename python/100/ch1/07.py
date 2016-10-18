# 07.テンプレートによる文作成

x = 12
y = "気温"
z = 22.4

def tmpl(x,y,z):
    print("{0}時の{1}は{2}".format(x,y,z))

tmpl(x,y,z)


