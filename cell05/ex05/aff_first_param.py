word = input().split('"')
if len(word) == 0:
    print('none')
while "" in word or " " in word:
    word.remove('')
    word.remove(' ')

print(word[0])

