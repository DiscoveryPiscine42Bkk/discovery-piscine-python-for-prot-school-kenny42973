word = input().split(' ')
word = [text.replace('"', '').replace("'", '') for text in word]
if len(word) == 0:
    print('none')
else:
    only_8 = []
    for x in range(len(word)):
        if len(word[x]) < 8:
            lower_8 = 8 - len(word[x])
            only_8.append(word[x] + ('Z'*lower_8))
        elif len(word[x]) > 8:
            only_8.append(word[x][0:8])        
        else:
            only_8.append(word[x])
    print(*only_8, sep='\n')