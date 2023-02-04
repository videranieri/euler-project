fibonacci = [1, 1, 2]

while len(str(fibonacci[-1])) < 1000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci.index(fibonacci[-1]) + 1)
