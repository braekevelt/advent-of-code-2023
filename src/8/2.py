
from math import lcm

with open('src/8/input.txt') as file:
    directions = file.readline().strip()
    graph = dict()
    for line in file:
        if not line or line.isspace(): continue
        node, connections = line.split(' = ')
        graph[node] = connections.strip('() \n').split(', ')

    steps = []
    for startNode in graph:
        if startNode.endswith('A'):
            step = 0
            currentNode = startNode
            while not currentNode.endswith('Z'):
                direction = directions[step % len(directions)]
                currentNode = graph[currentNode][0 if direction == 'L' else 1]
                step += 1
            steps.append(step)
    
    print(lcm(*steps))
