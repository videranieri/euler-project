def sunday_counter(pos, leap) -> list[int]:
    week = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    order = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    status, total = week[(pos)], 0

    if leap == 4:
        leap = 0
        order[1] = 29

    for idx in range(0, 12):
        if status == 'sun':
            total += 1

        while order[idx] != 0:
            order[idx] -= 1

            if pos >= 6:
                pos = 0
            else:
                pos += 1

            status = week[pos]

    return [pos, leap + 1, total]

year, data = 1901, [1, 1]
total = 0

while year <= 2000:
    data = sunday_counter(data[0], data[1])
    total += data[2]
    year += 1

print(total)
