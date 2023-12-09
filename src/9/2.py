
def extrapolate(sequence):
    if not any(sequence):
        return 0
    else:
        diff = [b - a for a, b in zip(sequence, sequence[1:])]
        return sequence[0] - extrapolate(diff)

with open('src/9/input.txt') as file:
    print(sum(extrapolate(
        list(map(int, line.strip().split())))
        for line in file
        if not line.isspace()
    ))
