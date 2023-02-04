nums = (lambda num: [i for i in range(1, num + 1)])(100)
total = 1

for num in nums:
    total *= num
    
print(sum([int(char) for char in str(total)]))