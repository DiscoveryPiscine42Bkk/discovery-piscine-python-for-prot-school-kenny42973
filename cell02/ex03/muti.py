a = int(input('Enter the first number: \n'))
b = int(input('Enter the second number: \n'))
c = a*b
print(f'{a} x {b} = {c}')

if c > 0:
    print('The result is positive.')
elif c < 0:
    print('The result is negative.')
else:
    print('The result is positive and negative.')