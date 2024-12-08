# Encrypt and Decrypt Strings Using Caesar Cipher

def enc(str, num):
    letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    # got big letters sequence because of high number test cases
    dic = {}
    # empty dictionary
    res = ""
    # empty result string

    for i in range(len(letters)):
        dic[f"{letters[i]}"] = letters[letters.find(letters[i]) + num]
    # created dictionary for exact test case, like if num = 2 one of the pair will be "a": "c", (It got forward by 2) this will be used to replace letters

    for i in str:
        if i not in letters and i not in letters.upper(): # checked if char was in lower letters or upper letters for symbols like: "!", ",", etc.
            res += i
        else:
            if i.isupper(): # checked case because if char was in uppercase in starting string it has to be uppercase now too.
                res += dic[i.lower()].upper()
            else: # just replaced char with precreated dictionary
                res += dic[i]

    return dic

print(enc("abc", 2))
print(enc("xyz", 3))
print(enc("Hello, World!", 5))
print(enc("Python", 0))
print(enc("abc", -1))

# ✔