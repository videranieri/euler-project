for a in range(1, 500):
    for b in range(1, 500):
        if a**2 + b**2 == (c := ((1000 - a) - b))**2:
            print(a*b*c)
            quit()