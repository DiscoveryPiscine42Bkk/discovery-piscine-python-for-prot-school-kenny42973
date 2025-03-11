og_array = [2, 8, 9, 48, 8, 22,-12, 2]
New_array = []
for x in range(len(og_array)):
    if og_array[x] + 2 >= 5:
        New_array.append(og_array[x] + 2)
print(og_array)
print(set(New_array))                                                                                                                                                                        