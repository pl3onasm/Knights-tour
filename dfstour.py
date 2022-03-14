
import os,sys; from collections import defaultdict
from time import perf_counter
sys.setrecursionlimit(10000000)

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
  if n<5 or n&1 and sum(start)&1: return None  # coloring rule
  graph = defaultdict(set)
  for i in range (n):
    for j in range(n):
      graph[(i,j)] = getJumps(*(i,j),n,start)
  path = [start]
  if dfs(graph, graph[start], path, n): return path
  return None

def output (path,s,t,n,time):
  out = (f'\n==< Knight\'s tour on a {n}x{n} '
        + f'chessboard starting at ({s},{t}) >==\n\n'
        + f"Execution time: {time:.3f} s\n\n")
  if path:
    out += 'Path:\n'
    for i,(h,k) in enumerate(path):
      out += f'({h},{k})'
      if i<n*n-1: out += ',' if not i or i%15 else '\n'
    out += ']\n'
    if n < 30:
      board = [n*[0] for _ in range(n)]
      for i in range(n*n):
        x,y = path[i]
        board[x][y] = i
      out += "\n"
      w = n*5 if n < 10 else n*6
      for i in range(n):
        out += '\t'+'-'*(w+1)+'\n\t'
        for j in range(n):
          d = board[i][j]
          if n <10:
            if d: out += f"|{d:3d} "
            else: out += f"| ♞ "
          elif n >= 10:
            if d: out += f"|{d:4d} "
            else: out += f"|  ♞ "
        out += "|"+'\n'
      out += '\t'+'-'*(w+1)+'\n\n'
  else: out += 'There is no solution.\n'
  return out

def getFileNumber(path):
  files = os.listdir(path)
  if files:
    for idx,file in enumerate(files):
      files[idx] = int(file.split('.')[0])
    files.sort()
    return 1 + files.pop()
  return 1

def main(n,start):
  begin = perf_counter()
  res = tour(n,start)
  end = perf_counter()
  out = output(res,*start,n,end-begin) 
  
  path = os.getcwd() + "/output"
  if not os.path.exists(path): 
    os.makedirs(path)
  outFile = path + f"/{getFileNumber(path)}.out"
   
  with open(outFile, 'w', encoding = "utf-8") as f:
    f.write(out)

if __name__ == "__main__":
  if len(sys.argv) == 3:
    fx,fy = sys.argv[2].strip('[]').split(',')
    main(int(sys.argv[1]),(int(fx),int(fy)))
  else:
    raise ValueError("Incorrect input") 
