def prime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False

    return True

seen, num = 2, 3

while seen <= 10000:
    num += 2
    if prime(num):
        seen += 1

print(num)