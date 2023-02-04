def abundant(num):
    divisors = set()

    for i in range(1, num):
        if num % i == 0:
            divisors.add(i)
    
    if sum(divisors) > num:
        return True

abundant = [i for i in range(1, 28123) if abundant(i)]
sums = set()

for num1 in abundant:
    for num2 in abundant:
        if (total := num1 + num2) >= 28123:
            break

        sums.add(total)

print(sum([i for i in range(1, 28123) if i not in sums]))