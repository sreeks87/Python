graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited =set()
visited2={}
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for nodes in graph[node]:
            dfs(visited,graph,nodes)

def addEdges(u,v):
    graph[u].append(v)

def bfs(node):
    queue=[]
    queue.append(node)
    visited2[node]=True

    while queue:
        node=queue.pop(0)
        print(node)
        for i in graph[node]:
            if i not in visited2:
                queue.append(i)
                visited2[i]=True

dfs(visited,graph,'A')
bfs('A')
addEdges('D','E')
print(graph)
# Time Complexity
# Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E)O(V+E), where VV is the number of vertices and EE is the number of edges. In case of DFS on a tree, the time complexity is O(V)O(V), where VV is the number of nodes.

# Note: We say average time complexity because a set’s in operation has an average time complexity of O(1)O(1). If we used a list, the complexity would be higher.

