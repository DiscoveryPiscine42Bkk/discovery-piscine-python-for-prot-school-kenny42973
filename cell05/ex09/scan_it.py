import re
word = input().split(' ', 1)
if len(word) < 2 or len(word) > 2:
    print('none')
else:
    text = re.findall('the', word[1])
    print(len(text))