
with open('src/5/input.txt') as file:
    _, *seeds  = file.readline().split();
    before = list(map(int, seeds))
    after = []
    while line := file.readline():
        if 'map' in line:
            before = before + after
            after = []
        elif line and not line.isspace():
            destinationRangeStart, sourceRangeStart, rangeLength = map(int, line.split())
            remaining = []
            for number in before:
                if sourceRangeStart <= number < sourceRangeStart + rangeLength:
                    after.append(number - sourceRangeStart + destinationRangeStart)
                else:
                    remaining.append(number)
            before = remaining
    print(min(after))
