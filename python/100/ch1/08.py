# 08.暗号文

string = "I study python."

def cipher(string):
    lists = []
    for i in string:
        if (not i.isupper()):
            lists.append(chr(219 - ord(i))) 
        else:
            lists.append(i)
    return lists

encryption = cipher(string)
print("".join(encryption))
composite = cipher(encryption)
print("".join(composite))

