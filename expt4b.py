graph = [['A', 'H', 7, 0], ['A', 'B', 1, 3], ['A', 'C', 2, 4], ['B', 'D', 4, 2], ['B', 'E', 6, 6], [
    'C', 'F', 3, 3], ['C', 'G', 2, 1], ['D', 'H', 5, 0], ['D', 'E', 7, 6], ['F', 'H', 1, 0], ['G', 'H', 2, 0]]

nodes = set()

for i in graph:
    nodes.add(i[0])
    nodes.add(i[1])

# print(nodes)
cost = dict()
cost1 = dict()
path = dict()
open = set()
close = set()

start = input("ENTER START NODE: ")
goal = input("ENTER THE GOAL NODE: ")

for i in nodes:
    cost[i] = 9999
    cost1[i] = 9999
    path[i] = ' '

open.add(start)
cost[start] = 0
path[start] = start


def Astar(start, goal, graph, open, close, cost):
    if start in open:
        open.remove(start)
        close.add(start)

    for i in graph:
        if (i[0] == start and (cost[i[0]] + i[2] + i[3]) <= cost[i[1]]):
            open.add(i[1])
            cost[i[1]] = cost[i[0]] + i[2]
            path[i[1]] = path[i[0]] + '->' + i[1]
            cost1[i[1]] = cost[i[0]] + i[2] + i[3]

    cost[start] = 9999
    smallest = min(cost, key=cost.get)
    if smallest not in close:
        Astar(smallest, goal, graph, open, close, cost)

Astar(start, goal, graph, open, close, cost)
print("THE SHORTEST PATH IS : ", path[goal])
print("THE TOTAL COST IS : ", cost1[goal])
