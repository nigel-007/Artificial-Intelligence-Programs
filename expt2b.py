#DFS using goal set
tree={'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[],
      }        
goal=input("Enter goal state ")
visited=set()
res=[]
def dfs(tree,start,goal):
   
    if start not in visited:
        #print(start)
        res.append(start)   
        visited.add(start)
    neighbours=tree[start]
    for i in neighbours:
        if goal in visited:
            break
        else:
            dfs(tree, i,goal)
dfs(tree, 'A',goal)
print(res)         
