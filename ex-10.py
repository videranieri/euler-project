def prime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False

    return True

print(sum([num for num in range(3, 2*10**6, 2) if prime(num)]))