#  ┌─────────────────────────────────────────────────────────┐
#  │  File name: tour.py                                     │
#  │  Author: David De Potter, pl3onasm@gmail.com            │
#  │  License: see the license file in this repository       │
#  │  Description: this module ensures input is read and     │
#  │  results are nicely formatted and stored, including a   │
#  |  graphical representation if applicable                 |
#  └─────────────────────────────────────────────────────────┘

import os,sys
from time import perf_counter
from dfs import tour

def output (path,s,t,n,time):
  info = (f'\n==< Knight\'s tour on a {n}x{n} '
        + f'chessboard starting at ({s},{t}) >==\n\n'
        + f"Execution time: {time:.3f} s\n\n")
  if path:
    out, newline, lim = 'Path:\n[', 0, 110 if n > 15 else 50
    for i,(h,k) in enumerate(path):
      out += (tup :=  f'({h},{k})')
      newline = 0 if newline >= lim else newline+len(tup)
      if i<n*n-1: out += ',' if not i or newline else ',\n'
    out += ']\n'
    if n < 32:
      board = [n*[0] for _ in range(n)]
      for i in range(n*n):
        x,y = path[i]
        board[x][y] = i
      out += "\nGraphical representation:\n\n"
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
    return info + out
  return info + 'There is no solution.\n'

def getFileNumber(dirpath):
  files = os.listdir(dirpath)
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
  if not os.path.exists(path): os.makedirs(path)
  outFile = path + f"/{getFileNumber(path)}.out"
  with open(outFile, 'w', encoding = "utf-8") as f:
    f.write(out)

if __name__ == "__main__":
  if len(sys.argv) == 3:
    fx,fy = sys.argv[2].strip('[]').split(',')
    main(int(sys.argv[1]),(int(fx),int(fy)))
  else:
    raise ValueError("Incorrect input") 