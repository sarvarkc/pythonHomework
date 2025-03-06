file = open('sample.txt')
txt = file.read()

txt = txt.lower().replace(',','')
txt = txt.lower().replace('.','')
txt = txt.lower().replace('-','')
txt = txt.lower().replace('_','')

words = {
    
}

for x in txt.split():
    if x not in words:
        words.update({x:1})
    else:
        words.update({x:words[x]+1})

print("Total words:", sum(words.values()))

words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))

for x in range(len(words)-5):
    words.popitem()

print('Top 5 Words:')

for x in words:
    print(x, '-', words[x], 'times')

