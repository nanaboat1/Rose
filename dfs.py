## Nana Boateng Amoah
## CS-473-1 
## 10/3/2022
## note: we have different ways of reading directed graphs and undirected graphs. 

from sys import stdin
from collections import OrderedDict

# data : list = [[12,13],[1,2],[1,5],[5,9],[5,10],[9,10],[3,4],[3,7],[3,8],[4,8],[7,11],[8,11],[11,12],[8,12],[6]] 


# read input from file.
f = open('rosalind_cc.txt')


## apr 1 : t :o(n) s: o(n) 

# new way to read input.
v,u = map(int, f.readline().strip().split(" "))


graph = {i+1:[] for i in range(v)} 

# create graph.
for line in f: 
   put = list(map(int, line.strip().split(" ")))
   graph[put[0]].append(put[1])
   graph[put[1]].append(put[0]) 


seen = set() 
# seen = { i:False for i in graph.keys()}

def sln(graph, check :set =seen) -> int: 

    conn_comp : int = 0

    ## itr over N and check connected components. 
    for node in graph: 

        # if node not evaluated, then check it out. 
        if node not in check: 
            dfs(node)
            conn_comp += 1

    return conn_comp


def dfs(node, chk: set =seen) -> None: 

    chk.add(node) # cur node has been seen. 

    for ad_node in graph[node]: 

        if ad_node not in seen: 

            dfs(ad_node)


print(sln(graph)) 