# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:19:46 2023

@author: Student
"""

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

def dfs_traversal(tree):
    visited=[]
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
        neighbour=tree[node]
        for i in neighbour:
            stack.append(i)
    return visited

print("Dfs travaersal is ",dfs_traversal(tree))
    
    











