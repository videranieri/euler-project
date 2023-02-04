def divisors(num):
    return sum(2 for i in range(1, int(num**.5) + 1) if num % i == 0)

num = 1

while True:
    triangle = num * (num + 1) // 2
    total = divisors(triangle)

    if total >= 500:
        print(triangle)
        break
    
    num += 1
