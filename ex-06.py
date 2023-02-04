nums = [i for i in range(1, 101)]
print(abs(sum(list(map((lambda x: x**2), nums))) - sum(nums)**2))
