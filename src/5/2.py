
def overlap(interval, sourceInterval):
    start, end = interval
    sourceStart, sourceEnd = sourceInterval

    if end <= sourceStart or sourceEnd <= start:
        return [], [interval]
    elif start < sourceStart:
        if end <= sourceEnd:
            return [(sourceStart, end)], [(start, sourceStart)]
        else:
            return [(sourceStart, sourceEnd)], [(start, sourceStart), (sourceEnd, end)]
    else:
        if end <= sourceEnd:
            return [interval], []
        else:
            return [(start, sourceEnd)], [(sourceEnd, end)]

with open('src/5/input.txt') as file:
    _, *seeds  = file.readline().split();
    seeds = list(map(int, seeds))
    before = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]    
    after = []
    while line := file.readline():
        if 'map' in line:
            before = before + after
            after = []
        elif line and not line.isspace():
            destinationStart, sourceStart, sourceLength = map(int, line.split())
            sourceInterval = (sourceStart, sourceStart + sourceLength)
            newBefore = []
            for interval in before:
                overlapping, remaining = overlap(interval, sourceInterval);
                newBefore += remaining
                for start, end in overlapping:
                    after.append((start - sourceStart + destinationStart, end - sourceStart + destinationStart))
            before = newBefore
    
    print(min(start for start, _ in after))
