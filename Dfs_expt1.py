tree={
      'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[]
      }

start=input("Enter Start node here : ")
goal=input("Please enter the goal State : ")

def dfs_goal(tree):    
        visited=[]    #All the elements that have been visited
        stack=[[start]] #All the elements that are not explored
       
        if start==goal:
           print("Start is the goal State : ")
           return start
           
        while stack:          #While queue is not empty
            path=stack.pop()
            node=path[-1]
            if node not in visited:
                visited.append(node)
                neighbour=tree[node]
                for i in neighbour:
                    new_path=list(path)
                    new_path.append(i)
                    #print("PATH ",new_path)
                    stack.append(new_path)
                    #print("STACK ",stack)
                    if i==goal:
                        return new_path
   
print("Goal Search is ",dfs_goal(tree))
