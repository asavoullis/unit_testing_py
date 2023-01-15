""" 
Write a Python program that takes a word and a file as input
checks if they are anagrams in that file. 

An anagram is a word or phrase formed by rearranging the letters 
of another word or phrase, using all the original letters exactly once. 
Your program should output whether the given words are anagrams or not.
"""

with open('word_file.txt', 'r') as f:
    words = f.readlines()

# for word in words:
#     print(word)

def find_anagrams(word):
    hashmap = {}

    for letter in word:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    return hashmap



steak_hash = find_anagrams("steak")
for word in words:
    if find_anagrams(word.lower().rstrip()) == steak_hash:
        print(word)


