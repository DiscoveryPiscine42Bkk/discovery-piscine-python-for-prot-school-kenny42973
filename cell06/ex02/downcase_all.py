a = input().split('" "')
a = [text.replace('"', '').replace("'", '') for text in a]
def downcase_all():
    if len(a) < 1:
        print('none')
    else:
        
        for x in range(len(a)):
            print(a[x].lower())
    return

downcase_all()
# "HELLO WORLD" "I understood Arrays well!"