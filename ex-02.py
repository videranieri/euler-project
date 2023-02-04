fibonacci = [1, 1, 2]

while fibonacci[-1] <= 4*10**6:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(sum([n for n in fibonacci if n % 2 == 0]))
