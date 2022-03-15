# ♞ Knight's tour

This program returns a path for a knight's tour on a nxn chessboard, where n <= 400. The output consists of a list of coordinates indicating the successive knight's jumps on the chessboard. For n < 30 a graphical representation is included.


## ♘ Usage

To run the program, pass the input size n and the starting point as arguments.  
For example:

```
python3 dfstour.py 16 [1,2]
```

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
