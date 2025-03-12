og_array = [2, 8, 9, 48, 8, 22,-12, 2]
New_array = []
x = 0
while x < 8:
    result = og_array[x] + 2
    New_array.append(result)
    x += 1
more_than_5 = []
y = 0
while y < 8:
    if New_array[y] >= 5:
        more_than_5.append(New_array[y])
    y += 1
print(set(more_than_5))
