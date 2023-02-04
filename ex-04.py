num = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        temp = str(x * y)

        if temp == temp[::-1] and int(temp) > num:
            num = int(temp)

print(num)