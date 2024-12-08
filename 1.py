# Check If Two Strings Are Anagrams

def anagram_check(str1, str2):
    return sorted(str1) == sorted(str2)
    # anagram words means that they contain exact same characters with different sequence, so if sorted they should be same

print(anagram_check("listen","silent")) # True
print(anagram_check("triangle","integral")) # True
print(anagram_check("apple","pale")) # False
print(anagram_check("a","a")) # True
print(anagram_check("rat","car")) # False

# ✔