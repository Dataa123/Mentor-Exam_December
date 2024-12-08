# Reverse the Order of Words in a Sentence

def reverse_sent(sent):
    return " ".join(sent.split()[::-1])
    # splitted words because if we reverse it without split it will reverse whole sentence's characters, now we have words and if we reverse it we get reversed list of words and we just have to join it

print(reverse_sent("Hello World")) # "World Hello"
print(reverse_sent("Python is great")) # "great is Python"
print(reverse_sent("a b c")) # "c b a"
print(reverse_sent("")) # ""
print(reverse_sent(" Spaces")) # "Spaces"

# ✔