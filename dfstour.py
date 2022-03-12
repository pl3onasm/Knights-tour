
import sys; from collections import defaultdict
sys.setrecursionlimit(100000)

def getJumps(x,y,n,start):
  jumps = []
  for i,j in (2,-1),(-2,-1),(-1,-2),(1,-2),(-1,2),(1,2),(2,1),(-2,1):
    if 0 <= x+i < n and 0 <= y+j < n and (x+i,y+j)!=start: 
      jumps += [(x+i,y+j)]
  return jumps

def dfs (graph, vertices, path, n):
  if len(path) == n*n: yield path
  vertices.sort(key=lambda k: len(graph[k]))
  for vertex in vertices:
    path += [vertex]
    for val in graph[vertex]: graph[val].remove(vertex)
    yield from dfs(graph, graph[vertex], path, n)
    path.pop()
    for val in graph[vertex]: graph[val] += [vertex]

def knights_tour(start,n):
  graph,vertices = defaultdict(list),[(i,j) for i in range(n) for j in range(n)]
  for vertex in vertices:
    graph[vertex] = getJumps(*vertex,n,start)

  return next(dfs(graph, graph[start], [start], n), None)



#print(knights_tour((0,0),100))
print(knights_tour((3,3),5))
print(knights_tour((0,0),4))
