a = ["abc", "ab", "a", "abcd", "abcde", "abcdef"]
b = sorted(a, key=lambda x: len(x))

print(b)