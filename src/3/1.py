import re

def isNextToSymbol(match, lines):
    for line in lines:
        begin = max(0, match.start() - 1)
        end = min(len(line), match.end() + 1)
        for char in line[begin:end]:
            if char != '.' and not char.isdigit() and not char.isspace():
                return True
    return False

with open('src/3/input.txt') as file:
    with open('src/3/output1.txt', 'w') as output:
        total = 0

        line1 = ""
        line2 = ""

        for line3 in file.readlines() + [""]:
            for match in re.finditer(r"\d+", line2):
                if isNextToSymbol(match, (line1, line2, line3)):
                    total += int(match.group())
                    output.write(match.group() + ' ')
            
            output.write('\n')
            
            line1 = line2
            line2 = line3

        print(total)
