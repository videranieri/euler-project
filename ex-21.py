def amic(n) -> int:
    divisors = set()

    for i in range(1, n):
        if n % i == 0:
            divisors.add(i)
    
    return sum(divisors)

print(sum([num for num in range(1, 10**4) if amic(amic(num)) == num and amic(num) != num]))