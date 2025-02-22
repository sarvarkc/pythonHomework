a = ['abc', 'a', 'abcde']
b = ['ab', 'abcd', 'abcdef']
c = a + b
print(sorted(c, key=lambda x: len(x)))