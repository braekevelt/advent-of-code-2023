import re

def gearIndex(match, line):
    begin = max(0, match.start() - 1)
    end = min(len(line), match.end() + 1)
    for index in range(begin, end):
        if line[index] == '*':
            return index
    return None

with open('src/3/input.txt') as file:
    with open('src/3/output2.txt', 'w') as output:
        total = 0

        line1 = ""
        line2 = ""

        for line3 in file.readlines():
            gearIndexMatch = dict()
            for line in (line1, line2, line3):
                for match1 in re.finditer(r"\d+", line):
                    index = gearIndex(match1, line2)
                    if index is not None:
                        if index in gearIndexMatch:
                            match2 = gearIndexMatch[index]
                            total += int(match1.group()) * int(match2.group())
                            output.write(f"({match1.group()},{match2.group()}) ")
                        else:
                            gearIndexMatch[index] = match1
            output.write('\n')
            line1 = line2
            line2 = line3

    print(total)
