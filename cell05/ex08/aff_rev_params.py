word = input().split()
if len(word) < 2:
    print('none')
else:
    print(*word[::-1], sep='\n')