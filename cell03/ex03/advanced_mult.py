x = 0
while x <= 10:
    y = 0
    result = f"Table de {x}:"
    while y <= 10: 
        result += f" {x * y}"
        y += 1
    print(result)
    x += 1
