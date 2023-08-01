tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = input("Enter the start state ")


def bfs(tree):
    goal = input("Enter the goal node ")
    visited = []
    queue = [start]

    if (start == goal):
        print("Goal node is ", start)
        return
    visited.append(start)
    while queue:
        node = queue.pop(0)
        neighbour = tree[node]
        for i in neighbour:
            if i not in visited:
                visited.append(i)
                queue.append(i)
            if i == goal:
                print("goal found ", i)
                return visited


def bfs_traverse(tree):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbour = tree[node]
            for i in neighbour:
                queue.append(i)
    return visited


print("Travaersal nodes are ", bfs_traverse(tree))
bfs(tree)
