word = input().split('"')
while '' in word:
    word.remove('')
while ' ' in word:
    word.remove(' ')

def downcase_all():
    if len(word) < 1:
        print('none')
    else:
        x = 0
        while x < len(word):
            print(word[x].lower())
            x += 1
    return

downcase_all()
# "HELLO WORLD" "I understood Arrays well!"
