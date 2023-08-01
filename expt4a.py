GRAPH = [['A','H',7,0],['A','B',1,3],['A','C',2,4],['B','D',4,2],['B','E',6,6],['C','F',3,3],['C','G',2,1],['D','H',5,0],['D','E',7,6],['F','H',1,0],['G','H',2,0]]
value = {'A': 0, 'B': 3, 'C': 4, 'D': 2, 'E': 6, 'F': 3, 'G': 1, 'H': 0}

def make_graph(graph_data):
    graph = {}
    for edge in graph_data:
        node1 = edge[0]
        node2 = edge[1]
        cost = edge[2]
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = cost
        graph[node2][node1] = cost
    return graph

def a_star(graph_data, start, goal):
    graph = make_graph(graph_data)
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while len(frontier) > 0:
        current = min(frontier)[1]
        frontier = [x for x in frontier if x[1] != current]

        if current == goal:
            break

        for next in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + value[next]
                frontier.append((priority, next))
                came_from[next] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

start_node=input("Enter the start node: ")
goal_node=input("Enter the goal node: ")

came_from, cost_so_far = a_star(GRAPH,start_node.upper(),goal_node.upper())
path = reconstruct_path(came_from,start_node.upper(),goal_node.upper())
print("Path:", path)
print("Traversal Cost:", cost_so_far[goal_node.upper()])