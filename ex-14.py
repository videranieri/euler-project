data = {'number': 2, 'chain': 2}

for num in reversed(range(2, 10**6)):
    base, chain = num, 1

    while base != 1:
        if base % 2 == 0:
            base //= 2
        else:
            base = base * 3 + 1
        
        chain += 1
    
    if chain > data['chain']:
        data = {'number': num, 'chain': chain}

print(data['number'])