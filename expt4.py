# A* Search Program
GRAPH = [['A', 'H', 7, 0], ['A', 'B', 1, 3], ['A', 'C', 2, 4], ['B', 'D', 4, 2], ['B', 'E', 6, 6], [
    'C', 'F', 3, 3], ['C', 'G', 2, 1], ['D', 'H', 5, 0], ['D', 'E', 7, 6], ['F', 'H', 1, 0], ['G', 'H', 2, 0]]
value = {'A': 0, 'B': 3, 'C': 4, 'D': 2, 'E': 6, 'F': 3, 'G': 1, 'H': 0}

node = set()

for i in GRAPH:
    node.add(i[0])
    node.add(i[1])

cost = dict()
path = dict()
open = set()
close = set()

start = input("ENTER ROOT NODE: ")
goal = input("ENTER GOAL NODE: ")

for i in node:
    cost[i] = 999
    path[i] = " "

open.add(start)
cost[start] = 0
path[start] = start


def Astar(start, goal, open, close, cost, GRAPH):
    if start in open:
        open.remove(start)
        close.add(start)
    for i in GRAPH:
        if i[0] == start and cost[i[0]]+i[2]+i[3] < cost[i[1]]:
            open.add(i[1])
            cost[i[1]] = cost[i[0]]+i[2]+i[3]-value[i[0]]
            path[i[1]] = path[i[0]]+'->'+i[1]
    cost[start] = 999
    mincost = min(cost, key=cost.get)
    if mincost not in close:
        Astar(mincost, goal, open, close, cost, GRAPH)


Astar(start, goal, open, close, cost, GRAPH)

print("THE SHORTEST PATH IS : ", path[goal])
print("THE TOTAL COST IS : ", cost[goal])
