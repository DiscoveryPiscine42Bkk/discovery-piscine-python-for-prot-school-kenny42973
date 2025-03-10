number = int(input('Enter a number less than 25 \n'))
x = 0
while True:
    if number <= 25:
        print(f'Inside the loop, my variable is {number}')
        number += 1
    elif number > 25:
        print('Error')
        break