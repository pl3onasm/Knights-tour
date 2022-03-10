# ♞ Knight's tour
Comparison between a local search and a divide-and-conquer algorithm


## ♘ Usage

To run the program, make sure to provide the input size n as an argument. For example:

```
python3 nqueens.py 250
```

The above command will write a solution for the 250-queens problem to a .out file in the output folder (which will be created if it does not exist) located in the current working directory. For sizes n < 200, a graphical representation of the chessboard is included. For larger problem sizes, the output only consists of a list of all the queen positions.  
The same program also allows for specifying one fixed board location, indicated by its coordinates. For example:  

```
python3 nqueens.py 10 [2,8]
```

This command will generate a solution for a problem with 10 queens, of which one is set to take the spot with row index 2 and column index 8.    
If no solution exists, the program will output an appropriate message.    


## ♘ References  

- Besa, J. J., Johnson, T., Mamano, N., Osegueda, M. C., & Williams, P. (2022). Taming the knight's tour: Minimizing turns and crossings. Theoretical Computer Science, 902, 1-20.
- Bi, B., Butler, S., DeGraaf, S., & Doebel, E. (2015). Knight’s tours on boards with odd dimensions. Involve, a Journal of Mathematics, 8(4), 615-627.
- Lin, S. S., & Wei, C. L. (2005). Optimal algorithms for constructing knight's tours on arbitrary n× m chessboards. Discrete applied mathematics, 146(3), 219-232.
- McGown, K., & Leininger, A. (2002). Knight’s tours. Cull, Paul (advisor). Oregon State Univesity.
- Parberry, I. (1997). An efficient algorithm for the Knight's tour problem. Discrete Applied Mathematics, 73(3), 251-260.
- Pranav, M., Nithin, S., & Guruprasad, N. (2019). A Comparison of Warnsdorff’s Rule and Backtracking for Knight’s Tour on Square Boards. In Emerging Research in Electronics, Computer Science and Technology (pp. 171-185). Springer, Singapore.
- Squirrel, D., & Çull, P. (1996). A Warnsdorff-Rule Algorithm for Knight's Tours on square chessboards.
