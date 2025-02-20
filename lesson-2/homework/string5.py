from collections import Counter

text = str(input())
vowels = ["a", "e", "i", "o", "u"]

string = list(text.lower())
string_count = Counter(string)


finalvowels = sum(string_count[v] for v in vowels)
finalconsonants = len(text)-finalvowels

print("Number of vowels:", finalvowels)
print("Number of consonants:", finalconsonants)