
with open('src/1/input.txt') as file:
    total = 0
    for line in file:
        if line:
            digits = [char for char in line if char.isdigit()]
            total += int(digits[0] + digits[-1])
    print(total)
