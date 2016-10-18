# 05.n-gramm

def ngram(string):
    for i in range(1,len(string)):
        print(string[i-1:i+1])


string = "I am an NLPer"
ngram(string)
ngram(string.split())
