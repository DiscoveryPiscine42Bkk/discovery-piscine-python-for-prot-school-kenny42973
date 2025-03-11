og_array = [2, 8, 9, 48, 8, 22,-12, 2]
New_array = og_array.copy()
for x in range(len(og_array)):
    New_array[x] = New_array[x] + 2

print(f'Original array: {og_array}')
print(f'New array: {New_array}')