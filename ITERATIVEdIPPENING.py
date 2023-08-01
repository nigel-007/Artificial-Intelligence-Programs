# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:46:34 2023

@author: Student
"""

""" ITERATIVE DEEPENING DFS """
tree={
      'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[]
      }
start=input('Enter start node ')
goal=input('Enter goal node ')
maxD=int(input('Enter max depth '))
level=0
path=list()

def iterative_dfs(tree,start,goal,level,maxD,path):
    print('Current level ',level)
    path.append(start)
    if start==goal:
        print('Goal found ',goal)
        return path
    else:
        print('Goal not found ')
    
    if level==maxD:
        return False
    neighbour=tree[start]
    for i in neighbour:
        if iterative_dfs(tree, i, goal, level+1, maxD, path):
            return path
        print(path.pop())
    return False

    
for i in range(maxD+1):
    path=list()
    print("i value ",i)
    test=iterative_dfs(tree, start, goal, level, maxD, path)
    
    if test:
        print("Goal not found")
        print("Path is ",path)
    else  :
     print("Goal node found in the given max depth")    












