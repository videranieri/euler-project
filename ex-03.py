def prime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False

    return True


num = 600851475143
print(max(set([n for n in range(1, int(num**.5)) if num % n == 0 and prime(n)])))