word = input().split('"')
if len(word) == 0:
    print('none')
while "" in word or " " in word:
    word.remove('')
    word.remove(' ')
print(f'parameters: {len(word)}')
x = 0
while x < len(word):
    print(f'{word[x]}: {len(word[x])}') 
    x += 1
