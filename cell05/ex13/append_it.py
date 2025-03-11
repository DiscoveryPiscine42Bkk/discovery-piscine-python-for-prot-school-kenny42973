word = input().split()
if len(word) == 0:
    print('none')
else:
    words = []
    for x in range(len(word)):
        if not 'ism' in word[x]:
            words.append(word[x] + 'ism')
print(*words, sep="\n") 
