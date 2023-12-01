
words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def firstDigit(line):
    if line[0].isdigit():
        return line[0]

    for word, digit in words.items():
        if line.startswith(word):
            return digit

    return firstDigit(line[1:])


def lastDigit(line):
    if line[-1].isdigit():
        return line[-1]
    
    for word, digit in words.items():
        if line.endswith(word):
            return digit

    return lastDigit(line[:-1])

with open('src/1/input.txt') as file:
    print(sum(int(firstDigit(line) + lastDigit(line)) for line in file if line))
