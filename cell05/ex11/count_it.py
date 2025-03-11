word = input().split()
if len(word) == 0:
    print('none')
else:
    for x in range(len(word)):
        print(len(word[x]))