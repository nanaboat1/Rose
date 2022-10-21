## nana boateng amoah 
## CS-473-1 
## 09/20/22 
## breadth-first-search
from collections import deque
import sys
 
#data = [[6,6],[4,6],[6,5],[4,3],[3,5],[2,1],[1,4]]

# read-input.
f = open('rosalind_bfs.txt')

data = [] # store input

for line in f.readlines(): 
    #print(line)
    #data.append(line[:-1].split(" "))
    a,b = line.split(" ")
    data.append([int(a),int(b)])
    

graph = { } 

# traverse l->r for directed graph
# create the graph.
for val in data: 
    if int(val[0]) not in graph: 

        if val[0] != val[1]:
            graph[int(val[0])] = [int(val[1])]
    else:
        graph[int(val[0])].append(int(val[1])) 


# calculate the shortest distance for graph.
# my recursive algorithm.
def myTraverse(graph, start, end, path=[]) -> int: 

    # path of traversal 
    path = path + [start] 

    if start == end: 
        return len(path[:-1]) 

    if start not in graph: 
        return None
    
    for node in graph[start]: 

        # prevent revisit of seen nodes.
        if node not in path: 
            newpath = myTraverse(graph,node,end,path)
        
            if newpath: return newpath 

    return None    

## iterative conversion of my recursive graph traverse algo.
#  used recursive, because my computer cannot make 10^10 recursive calls
#  
def itr_bfs(graph, start, end, path=[]) -> int: 

    queue = deque() # updates nodes being visited.
    seen_node = set() # prevent's revisit of traversed nodes. 

    # start node is a path
    queue.append([start])
    seen_node.add(start)

    # itr to traverse the queue.
    while queue: 

        path = queue.pop()
        vtx = path[-1] 

        if vtx == end: # when destination is reached

            return len(path[:-1])
               
        for node in graph.get(vtx,[]): 

            if node not in seen_node: 
                seen_node.add(node)
                newpath = list(path)
                newpath.append(node)
                queue.append(newpath) 

##

## testing fxn edge case. 
# print(itr_bfs(graph, 1,2))
N = len(graph)+1

for idx in range(1,N+1): 
    out: int or None = itr_bfs(graph,1,idx)

    if out == None: 
        print(-1,end=" ")
    else: 
        print(out, end=" ")
