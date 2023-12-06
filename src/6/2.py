
with open('src/6/input.txt') as file:
    _, *times = file.readline().split()
    _, *distances = file.readline().split()

    time = int(''.join(times))
    distance = int(''.join(distances))
    count = 0
    for t in range(time + 1):
        if (time - t) * t > distance:
            count += 1
    print(count)
