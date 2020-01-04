import sys


def dijkstra(graph,start,dest):
    short_dist = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []


    for item, node in unseenNodes.items():
        for cnode, value in node.items():
            short_dist[cnode] = infinity

    short_dist[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif short_dist[node] < short_dist[minNode]:
                minNode = node
                

        for childNode, weight in graph[minNode].items():
    
            if weight + short_dist[minNode] < short_dist[childNode]:
                # print(childNode, weight)
                short_dist[childNode] = weight + short_dist[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = dest
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            break
    path.insert(0,start)
    if short_dist[dest] != infinity:
        print(' -> '.join(path) + ' : ' + str(short_dist[dest]))


def init_graph():
    inputs = list(open(sys.argv[1],"r"))

    graph = {}

    for i in range(len(inputs)):
        graph.update({str(inputs[i].split('\n')[0].split(' ')[0]):{}})


    for i in range(len(inputs)):
        # print(inputs[i].split('\n')[0].split(' '))
        graph[str(inputs[i].split('\n')[0].split(' ')[0])][str(inputs[i].split('\n')[0].split(' ')[1])] = int(inputs[i].split('\n')[0].split(' ')[2])

    return graph


try:
    graph = init_graph()
    print("Graph: \n-------")
    print(graph)

    print("\nShortest Paths: \n---------------")
    dijkstra(init_graph(), sys.argv[2], sys.argv[3])


except:
    print("Invalid input, please try again")
    print("[USAGE] python dijkstra.py inputs.txt")
