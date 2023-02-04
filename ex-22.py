from requests import get

data = sorted(str(get("https://projecteuler.net/project/resources/p022_names.txt")
                  .content).replace('"', "").replace("'", "").replace("b", "").split(","))

def positions(word):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in word:
        yield alphabet.index(letter) + 1

total = 0

for name in data:
    w = sum([result for result in positions(name)])
    p = data.index(name) + 1

    total += w * p

print(total)