word = input().split("'")
while '' in word:
    word.remove('')
while ' ' in word:
    word.remove(' ')
if len(word) == 0:
    print('none')
else:
    only_8 = []
    x = 0
    while x < len(word):
        if len(word[x]) < 8:
            lower_8 = 8 - len(word[x])
            only_8.append(word[x] + ('Z'*lower_8))
        elif len(word[x]) > 8:
            only_8.append(word[x][0:8])        
        else:
            only_8.append(word[x])
        x += 1
    print(*only_8, sep='\n')

#'lol' 'physically' 'backpack' 
