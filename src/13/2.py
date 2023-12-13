
def getMirrors(lines):
    for linesBefore in range(1, len(lines)):
        if all(
            lines[linesBefore - 1 - index] == lines[linesBefore + index]
            for index in range(linesBefore)
            if linesBefore + index< len(lines)
        ):
            yield linesBefore

with open('src/13/input.txt') as file:
    total = 0
    for i, smudgedPattern in enumerate(file.read().split('\n\n')):
        
        smudgedVertical = tuple(zip(*(line for line in smudgedPattern.split())))
        smudgedHorizontal = tuple(tuple(line) for line in smudgedPattern.split())
        smudgedVerticalMirrors = set(getMirrors(smudgedVertical))
        smudgedHorizontalMirrors = set(getMirrors(smudgedHorizontal))

        for index, char in enumerate(smudgedPattern):
            pattern = smudgedPattern

            if char == '.':
                pattern = smudgedPattern[:index] + '#' + smudgedPattern[1+index:]
            elif char == '#':
                pattern = smudgedPattern[:index] + '.' + smudgedPattern[1+index:]
            else:
                continue

            vertical = tuple(zip(*(line for line in pattern.split())))
            horizontal = tuple(tuple(line) for line in pattern.split())
            verticalMirrors = set(getMirrors(vertical))
            horizontalMirrors = set(getMirrors(horizontal))

            verticalMirrors.difference_update(smudgedVerticalMirrors)
            horizontalMirrors.difference_update(smudgedHorizontalMirrors)

            if len(verticalMirrors) + len(horizontalMirrors) == 1:
                total += sum(verticalMirrors) + 100 * sum(horizontalMirrors)
                break
    
    print(total)
