tree={'A':[('B',12),('C',4)],
      'B':[('D',7),('E',3)],
      'C':[('F',8),('G',2)],
      'E':[('H',0)],
      'F':[('H',0)],
      'G':[('H',0)],
      'D':[],
      'H':[]
      }
'''
node=tree['A']
print(node)
print(node[0])
print(node[1])
print(node[0][1])
'''	

start=input("Enter the start state ")
goal=input("Enter goal state ")
def bestfs(start,goal,tree,open=[],close=[]):
    if start==goal:
        print("Goal found ",start)
        return
    
    if start not in close:
        print(start,end=" ")
        close.append(start)
        neighbour=tree[start]
        for i in neighbour:
            if i[0][0] not in open:
                open.append(i)
    open.sort(key=lambda x:x[1])
    if len(open)==0:
        print("Goal not found")
        return
    if open[0][0]==goal:
        print(open[0][0],end=" ")
    else:
        node=open[0]
        open.remove(node)
        bestfs(node[0], goal, tree,open,close)
bestfs(start, goal, tree,open=[],close=[])        

            
