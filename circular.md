
  
## Circular Buffer Problem
Implement a circular buffer of size N. Allow the caller to append, remove and list the contents of the buffer. Implement the buffer to achieve maximum performance for each of the operations.
The new items are appended to the end and the order is retained i.e elements are placed in increasing order of their insertion time. When the number of elements in the list elements exceeds the defined size, the older elements are overwritten.
 
 
### There are four types of commands.
 

 - "A"  n -  Append the following n lines to the buffer. If the buffer
   is full they replace the older entries. 
  - "R"  n -  Remove first n elements of the buffer. These n elements are the ones that were added earliest among the current elements. 
  - "L"   - List the elements of
   buffer in order of their inserting time. 
   "Q"  - Quit.

 
### Your task is to execute commands on circular buffer.
 
## Input format :
 
First line of input contains N ,  the size of the buffer.
A n  - append the following n lines to the buffer.
R n - remove first n elements of the buffer.
L - list the buffer.
Q - Quit.
 
## Output format :
 
Whenever  L command appears in the input, print the elements of buffer in order of their inserting time. Element that was added first should appear first. 
 
### Sample Input :
 

    10
    A 3
    Fee
    Fi
    Fo
    A 1
    Fum
    R 2
    L
    Q

 
### Sample Output :
 

    Fo
    Fum

 
### Constraint :
 
0 <= N <= 10000
Number of removing elements will <= number of elements presents in circular buffer.
total number of commands <= 50000.
total number of characters in input <= 20000000.
