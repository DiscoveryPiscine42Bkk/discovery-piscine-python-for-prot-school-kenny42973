word = input()
if word == '':
    print('none')
elif not 'z' in word:
    print('none')
else:
    print('z' * word.count('z'))