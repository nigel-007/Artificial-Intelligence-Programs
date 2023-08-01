#DFS using goal list
tree={'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[],
      }        
goal=input("Enter goal state ")
start=input("Enter start node ")

def dfs_path(tree):
    visited=[]
    stack=[[start]]
    if start==goal:
        print(start," is a goal node")
    while stack:
        path=stack.pop()
        node=path[-1]
        if node not in visited:
            visited.append(node)
        neighbours=tree[node]
        for i in neighbours:
            new_path=list(path)
            new_path.append(i)
            stack.append(new_path)
            if i==goal:
                return new_path
print("shortest path of DFS is ",dfs_path(tree))            
