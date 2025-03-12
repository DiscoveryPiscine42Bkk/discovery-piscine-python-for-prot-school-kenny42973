word = input().split('"')
if len(word) < 2:
    print('none')
while "" in word or " " in word:
    word.remove('')
    word.remove(' ')

print(*word[::-1], sep='\n')
