word = input().split('" "')
word = [text.replace('"', '').replace("'", '') for text in word]
if len(word) < 2:
    print('none')
else:
    print(*word[::-1], sep='\n')
