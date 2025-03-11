word = input().split()
if len(word) == 0:
    print('none')
else:
    print(f'parameters: {len(word)}')
    for x in range(len(word)):
        print(f'{word[x]}: {len(word[x])}')
