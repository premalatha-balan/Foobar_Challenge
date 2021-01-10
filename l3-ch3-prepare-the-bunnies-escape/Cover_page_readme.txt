This was a challenging one for me. I have got two solutions both of them work and passed the Foobar test cases. I do not think either of these is a BFS or DFS algorithm. Here is a link that explains BFS & DFS. I think this problem needs DFS algorithm. https://www.youtube.com/watch?v=TIbUeeksXcI&t=118s
Here is a link that explains BFS algorithm and python implementation of it. https://www.youtube.com/watch?v=hettiSrJjM4&t=3s

I need to learn queue library and use it. That will be my next solution for this. 

I came across a site which had the hidden test cases figured out and published for this challenge after I had solved the problem and submitted my solution. But found the information fascinating and so took time to add the test cases to this repo. I had used my own extra test cases that helped me solve the problem. 
The xls file has the matrices/test-cases representing the maze visually. 

Here is how the tests cases are designed I think: (and this is what helped me solve the problem)
test case 1, 2, & 3 all have output (h+w-1) as the shortest path
test case 1 - there is a solvable path from (0,0) to (h,w) without removing a wall and that is also the shortest path.
test case 2 - there is a solveable path but it is not the shortest. Removing first occuring wall gives h+w-1 as output. So it doesn't go for exhaustive search of all paths. 
test case 3 - there is no solveable path without removing a wall. Removing first occuring wall is removed, gives shortest solveable path is h+w-1
test case 4 - there is solveable path but it is not the shortest. Removing any wall does not give h+w-1 so, exhaustive search of all paths have to collected and shortest (min) of all the paths is returned. 
test ase 5 - there is no solveable path. Not all walls by removing result in solveable paths. Exhaustive search for all paths and removing all walls is needed. The shortest (min) of the solveable paths is returned.
