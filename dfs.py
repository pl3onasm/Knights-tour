from collections import defaultdict
import sys; sys.setrecursionlimit(10000000)

def getJumps(x,y,n,start):
  jumps = set()
  for i,j in (2,-1),(-2,-1),(-1,-2),(1,-2),(-1,2),(1,2),(2,1),(-2,1):
    if 0 <= x+i < n and 0 <= y+j < n and (x+i,y+j)!=start: 
      jumps.add((x+i,y+j))
  return jumps

def distance(x,y,n):  
  # used to sort on largest distance from the center
  return (x-n/2)**2 + (y-n/2)**2

def dfs (graph, vertices, path, n):
  if len(path) == n*n: return True
  vertices = sorted(vertices, key=lambda k: (len(graph[k]),-distance(*k,n)))
  for vertex in vertices:
    path += [vertex]
    for val in graph[vertex]: graph[val].remove(vertex)
    if dfs(graph, graph[vertex], path, n): return True
    path.pop()
    for val in graph[vertex]: graph[val].add(vertex)
  return False

def tour(n,start):
  if n<5 or n&1 and sum(start)&1: return None  # color criterion
  graph = defaultdict(set)
  for i in range (n):
    for j in range(n):
      graph[(i,j)] = getJumps(i,j,n,start)
  path = [start]
  if dfs(graph, graph[start], path, n): return path
  return None




