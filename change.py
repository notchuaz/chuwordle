with open('words.txt') as f:
    lines = f.readlines()
file = open('wordsChanged.txt', 'w+')
for word in lines:
    word = '"'+word[:5]+'",'+'\n'
    file.write(word)
