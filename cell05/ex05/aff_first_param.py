word = input().split('" "')
word = [text.replace('"', '').replace("'", '') for text in word]
if len(word) == 0:
    print('none')
else:
    print(word[0])
