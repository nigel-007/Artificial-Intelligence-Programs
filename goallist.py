# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:06:12 2023

@author: Student
"""

""" GOAL SEARCH LIST """

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

def dfs_path(tree):
    visited=[]
    stack=[[start]]
    if start==goal:
        print(start," is the goal node ")
    while stack:
        path=stack.pop()
        node=path[-1]
        if node not in visited:
            visited.append(node)
        neighbour=tree[node]
        for i in neighbour:
            new_path=list(path)
            new_path.append(i)
            stack.append(new_path)
            if i==goal:
                return new_path
            
            
print("shortest path of dfs goal search is ",dfs_path(tree))
        






