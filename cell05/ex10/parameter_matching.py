word = input()
if word == "":
    print('none')
else:
    second_word = input('What was the parameter? ')
    if word == second_word:
        print('Good job!')
    else:
        print('Nope, sorry...')