
def recordToCounts(record: str) -> str:
    counts = []
    count = 0
    for char in record:
        if char == '#':
            count += 1
        elif count > 0:
            counts.append(count)
            count = 0
    if count > 0:
        counts.append(count)
    return ','.join(map(str, counts))


def countArrangements(record: str, counts: str) -> int:
    if '?' in record:
        a = countArrangements(record.replace('?', '.', 1), counts)
        b = countArrangements(record.replace('?', '#', 1), counts)
        return a + b
    else:
        c = recordToCounts(record)
        return 1 if c == counts else 0

with open('src/12/input.txt') as file:
    total = 0
    for line in file:
        if not line.isspace():
            record, counts = line.strip().split()
            total += countArrangements(record, counts)
    print(total)
