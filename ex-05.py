def condition(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    
    return True

num = 20
while not condition(num):
    num += 20

print(num)