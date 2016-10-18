# 09.Typoglycemia

import random

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

for i in string.split():
    if len(i) <= 4:
        print(i,end=" ");
    else:
        rand_list = list(i[1:-1])
        random.shuffle(rand_list)
        print(i[0] + "".join(rand_list) + i[-1],end=" ")
print()
