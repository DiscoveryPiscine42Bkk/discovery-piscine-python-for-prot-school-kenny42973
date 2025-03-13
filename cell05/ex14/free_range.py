range_ = list(map(int, input().split()))
number = []
x = range_[0]
y = 0
while x <= range_[1]:
    number.append(range_[0]+y)
    x += 1
    y += 1
print(number)
