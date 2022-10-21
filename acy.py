## nana boateng amoah

# read input from file.



#apr 1: t ->O(N^2) s ->O(N)



graphs = []
nodes = []
# create graph.
graph = {}
with open('rosalind_dag.txt') as f: 
    c = int(f.readline().strip()) # number of individual graphs.

    for line in f: 
        if line.strip():  # when there is no white space
            node = list(map(int, line.strip().split(" ")))
            graph[node[0]].append(node[1])

        else: # when a new graph is intercepted.
            v,u = map(int, f.readline().strip().split(" "))
            graph = {i+1:[] for i in range(v)}
            graphs.append(graph)
            nodes.append(v)

    

def dfs(graph, node, seen): 

    # when node has already been seen.
    if seen[node]== True: 
        return True
    seen[node] = True # node has been seen. 
    

    for _nod in graph[node]:
        return dfs(graph, _nod, seen)
    return False

def acy(graph, v): 

    # loop is used to check acyclicity of each individual graph.
    for node in range(1, v+1):
        seen = [False for i in range(int(v)+1)]
        

        # when acylic
        if dfs( graph, node, seen): 
            return -1 
        
    # when not acyclic.
    return 1

N = len(graphs)
res = [] # result.

for n in range(N): 
    graph = graphs[n]
    v = nodes[n]

    res.append(str(acy(graph,v)))


# result print-out.
print(" ".join(res))
