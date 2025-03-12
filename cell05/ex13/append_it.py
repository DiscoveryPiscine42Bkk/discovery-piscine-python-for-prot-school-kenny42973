word = input().split('"')
if len(word) == 0:
    print('none')
while "" in word or " " in word:
    word.remove('')
    word.remove(' ')
x = 0
while x < len(word):
    if not 'ism' in word[x]:
        print(word[x] + 'ism')
    x += 1
