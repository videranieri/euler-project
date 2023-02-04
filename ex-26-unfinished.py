import re

REPEATER = re.compile(r"(.+?)\1+$")

def returner(num):
    decimal = str(num)[2:]
    
    match = REPEATER.match(decimal)
    return match.group(1) if match else None

print(returner(1/6))