# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:39:33 2023

@author: Student
"""
""" GOAL SEARCH SET """
tree={
      
      'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[]
      
      }

start=input("Enter start state ")
goal=input("Enter goal state ")
visited=set()
res=[]
def dfs(tree,start,goal):
    
    if start not in visited:
        #print(start)
        
        res.append(start)
        visited.add(start)
        neighbour=tree[start]
        for i in neighbour:
            if goal in visited:
                break
            else:
                dfs(tree,i,goal)
                

dfs(tree,start,goal)

print(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    