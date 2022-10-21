## nana boateng amoah
## cs-473-1
## october 10 2022
## topological sorting 

## input and graph creation. 
from typing import Tuple

f = open('rosalind_ts.txt')


#data = [[4,5],[1,2],[3,1],[3,2],[4,3],[4,2]] 
vtx, edge = map(int, f.readline().strip().split(" "))

# read input from graph.
graph = { i+1:[] for i in range(vtx+1)} 

for line in f: 
    v,u = map(int, line.strip().split(" "))
    graph[v].append(u)

## calculate the degree of each vertex. 
#gDeg = {v:len(u) for v,u in graph.items() }

# helper state. 
#graph[-1] = [-1]

# check the graph for nodes connected to vtx 
def checkVtx( vt, seen, out) : 
    seen[vt] = True 

    for node in graph[vt]: 
        if seen[node] == False: 
            checkVtx(node,seen,out )
    out.insert(0,vt)




# topological sort algo. 
def topoSort(graph, vtx): 

    # itr through graph & neighbors
    # if graph deg == 0 you know what to do. 
    # use dfs
    seen = [False]*(vtx+1) 
    out = [] 


    for vt in range(1, vtx+1): 
        if seen[vt] == False: 
            checkVtx(vt, seen, out)
    
    return out


result = topoSort(graph, vtx)
for node in result: 
    print(node, end=" ")