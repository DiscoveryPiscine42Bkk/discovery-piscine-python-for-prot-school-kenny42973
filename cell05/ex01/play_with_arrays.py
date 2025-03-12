og_array = [2, 8, 9, 48, 8, 22,-12, 2]
New_array = []
x = 0
while x < 8:
    result = og_array[x] + 2
    New_array.append(result)
    x += 1
print(f'Original array: {og_array}')
print(f'New array: {New_array}')
