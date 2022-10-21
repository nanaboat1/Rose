## Nana Boateng Amoah
## CS-473-1 9/14/22
## Rosalind Degree Array
from sys import stdin
from collections import OrderedDict

# read input from file.
f = open('rosalind_ddeg.txt')

data = [] # store input

for line in f.readlines(): 
    data.append(line[:-1].split(" "))

#data = [[5,4],[1,2],[2,3],[4,3],[2,4]]
# graph is built using a dict with lists as elements. 

graph = {}

# traverse l->r
for val in data: 
    if int(val[0]) not in graph: 
        graph[int(val[0])] = [int(val[1])]
    else:
        graph[int(val[0])].append(int(val[1])) 

# traverse r->l 
for val in data: 
    if int(val[1]) in graph: 
       graph[int(val[1])].append(int(val[0])) 
    else : 
        graph[int(val[1])] = [int(val[0])] 

# flag any 1-degree (orphan) node from the graph. 
# modified for Degree-array 2
for node in graph: 
    if len(graph[node]) <=1 and sum(graph[node])<node: 
        graph[node] = [-1]

# remove orphan edges from each node.
for node, edges in graph.items(): 

    if graph[node] == [-1]:

        # find node in element list and remove as well.
        for node2 in graph: 

            # cont'd 
            if node in iter(graph[node2]):
                graph[node2].remove(node)

out = []

# sort then, output the data.
graph = OrderedDict(sorted(graph.items()))
# print to output.
# for node in graph: 
# 
#     if graph[node] != [-1]: 
#         print(len(graph[node]),end=" ")

# filter the graph.
d = dict(filter(lambda elem: elem[1] != [-1], graph.items()))

# Add orphan-ed nodes 
for node in graph: 

    if node not in d: 
        d[node] = [0]

#print(d)

# calculate the degree of each node. 
len_node = {} 
for node in d: 

    if d[node] != [0]: 
        len_node[node] = len(d[node]) 
    else: 
        len_node[node] = 0 # orphan nodes

# Bug key-value issue with printing
len_node[0] = 0

# output the degree of neighbour nodes. 
out = []
for node in d: 
    compt =0  

    # calculates the degree.
    for vetx in d[node]: 
        compt += len_node[vetx] 
         
    
    print(compt, end=" ")

    
