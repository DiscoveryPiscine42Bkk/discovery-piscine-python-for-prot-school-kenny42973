def greetings(a="noble stranger"):
    if isinstance(a, str):
        print(f'Hello, {a}.')
    elif isinstance(a, int):
        print(f'Hello, {a}.')

greetings('Alexandra') 
greetings('Wil') 
greetings() 
greetings(42)