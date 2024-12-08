# Count the Number of Unique Words in a Text

def count_unique(s):
    return len(set(s.lower().split()))
    # used .lower() to "turn off" case sensitivity, uset .split() to make list of words for their count and also used set to don't include same words twice or more, len did the final job and counted how many different words were in string

print(count_unique("The quick brown fox jumps over the lazy dog")) # 8
print(count_unique("Hello hello world!")) # 2
print(count_unique("")) # 0
print(count_unique("Python is fun. Python is cool.")) # 4
print(count_unique("One word")) # 2

# ✔