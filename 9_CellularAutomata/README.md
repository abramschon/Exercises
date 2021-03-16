# Cellular Automata

In the [course](https://www.complexityexplorer.org/courses/67-introduction-to-renormalization) I am doing on renormalization, it mentions cellular automata. A simple type of cellular automata involves rows of pixels, each of which can be on or off (1 or 0). The value of a pixel is determined by the values of the 3 pixels above it:

    [w,x,y,z]
    [a,b,c,d]
For instance, the value of pixel `b` would be determined by the values of `w,x,y`.
 
 There are different *rules* that specify how each row maps to the next row, for instance, [rule 110](https://en.wikipedia.org/wiki/Rule_110).

 Now, in the course, they mention that by coarse graining a system that evolves via rule 105 using a certain projection, and then evolving the coarse grained variables according to rule 150, we observe the same behaviour as we would see if we evolved the system in the fine grained system and then coarse-grained. 

 I thought it would be fun to implement this. 

 Tips can be found [here](http://tuvalu.santafe.edu/~simon/MOOC_problems.pdf) 

