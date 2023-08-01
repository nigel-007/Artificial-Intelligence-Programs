#Deepening DFS
tree={'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[],
      }        
start=input("Enter start node ")

goal=input("Enter goal state ")
maxD=input("Enter Max depth ")
level=0
path=list()
def depth_limited(tree,start,goal,level,maxD,path):
    print("Current level",level)
    path.append(start)
    if start==goal:
        print("goal found ")
        return path
    print("Goal not found")
    if level==maxD:
        return False
    neighbour=tree[start]
    for i in neighbour:
        if depth_limited(tree, i, goal, level+1, maxD, path):
            return path
        print(path.pop())
    return False    

test=depth_limited(tree, start, goal, level, maxD, path)
if test:
    print("Goal not found")
    print("Path is ",path)
else  :
    print("Goal node found in the given max depth")    
            
