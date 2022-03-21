# ♞ Knight's tour

This program returns a path for a knight's tour on a nxn chessboard, where n <= 1000. The output consists of a list containing the coordinates indicating the successive knight's jumps on the chessboard. For n < 32 a graphical representation is included in the output file (in which the numbers indicate the order in which the moves are made). If no tour is possible, the program outputs an appropriate message.  

To compute a knight's tour, the program makes use of a depth-first-search algorithm that is guided by Warnsdorff’s rule, which simply states that the search should always move to the adjacent, unvisited square with minimal degree, i.e. with the least number of remaining adjacent, unexplored squares to move to. This rule, however, does not tell anything about what to do in case of ties, which are, in fact, so frequent in this problem that its heuristic value is far too weak to make for an efficient program. This is why an additional heuristic has been applied, which prioritizes adjacent squares that are farthest away from the board's center, since those have the least number of options to continue the knight's path from. The combination of these two heuristics efficiently directs the path towards a solution, as it minimizes reliance on expensive backtracking by preventing it from running into dead ends.  

## ♘ Usage

To run the program, pass the input size n and the starting point as arguments. For example:

```
python3 tour.py 16 [1,2]
```
This command will compute a knight's tour that starts at the square with row index 1 and column index 2 on a 16x16 chessboard. The output will be written to the /output folder (which will be created if it does not exist).   

Note that for large boards (n > 100), the stack size will have to be increased. This can be done in the terminal:  

```
ulimit -s unlimited
```

## ♘ References  

- Conrad, A., Hindrichs, T., Morsy, H., & Wegener, I. (1994). Solution of the knight's Hamiltonian path problem on chessboards. Discrete Applied Mathematics, 50(2), 125-134.
- McGown, K., & Leininger, A. (2002). Knight’s tours. Cull, Paul (advisor). Oregon State Univesity.
- Parberry, I. (1997). An efficient algorithm for the Knight's tour problem. Discrete Applied Mathematics, 73(3), 251-260.
- Pranav, M., Nithin, S., & Guruprasad, N. (2019). A Comparison of Warnsdorff’s Rule and Backtracking for Knight’s Tour on Square Boards. In Emerging Research in Electronics, Computer Science and Technology (pp. 171-185). Springer, Singapore.
- Squirrel, D., & Çull, P. (1996). A Warnsdorff-Rule Algorithm for Knight's Tours on square chessboards.
