#DFS
tree={'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[],
      }

start=input("Enter start state ")
def dfs_traversal(tree):
    visited=[]
    stack=[start]
    while stack:
        node=stack.pop()#A
        if node not in visited:
            visited.append(node)
        neighbours=tree[node]
        for i in neighbours:
            stack.append(i)
    return visited
print("DFS traversal is ",dfs_traversal(tree))  
