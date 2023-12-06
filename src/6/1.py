
with open('src/6/input.txt') as file:
    _, *times = file.readline().split()
    _, *distances = file.readline().split()

    total = 1
    for time, distance in zip(map(int, times), map(int, distances)):
        count = 0
        for t in range(time + 1):
            if (time - t) * t > distance:
                count += 1
        total *= count
    print(total)
