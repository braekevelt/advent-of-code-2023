
with open('src/8/input.txt') as file:
    directions = file.readline().strip()
    graph = dict()
    for line in file:
        if not line or line.isspace(): continue
        node, connections = line.split(' = ')
        graph[node] = connections.strip('() \n').split(', ')
    currentNode = 'AAA'
    steps = 0
    while currentNode != 'ZZZ':
        direction = directions[steps % len(directions)]
        currentNode = graph[currentNode][0 if direction == 'L' else 1]
        steps += 1
    print(steps)
