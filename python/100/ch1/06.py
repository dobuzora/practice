# 06.集合

string1 = "paraparaparadise"
string2 = "paragraph"

def ngram(string):
    lists=[]
    for i in range(1,len(string)):
        lists.append(string[i-1:i+1])
    return set(lists)

X = ngram(string1)
Y = ngram(string2)

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

print("se" in X)
print("se" in Y)

