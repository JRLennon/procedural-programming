word1 = input("First word: ")
word2 = input("Second word: ")

anagram = True if sorted(word1) == sorted(word2) else False
if anagram:
    print(word1, "and", word2, "are anagrams.")
else:
    print(word1, "and", word2, "are not anagrams.")