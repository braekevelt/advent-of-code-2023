
def hashmap(label):
    current = 0
    for char in label:
        current += ord(char)
        current *= 17
        current %= 256
    return current

with open('src/15/input.txt') as file:
    boxes = [dict() for _ in range(256)]
    for step in file.read().strip().split(','):
        if step[-1] == '-':
            label = step[:-1]
            boxNr = hashmap(label)
            box = boxes[boxNr]
            box.pop(label, None)
        else:
            label, focalLength = step.split('=', 1)
            boxNr = hashmap(label)
            box = boxes[boxNr]
            box[label] = int(focalLength)

    print(
        sum(
            (1 + boxNr) * (1 + slotNr) * focalLength
            for boxNr, box in enumerate(boxes)
            for slotNr, focalLength in enumerate(box.values())
        )
    )
