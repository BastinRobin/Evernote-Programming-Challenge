#!/bin/python
#Multiplication of list elements
def mul(args):
    x= 1
    for arg in args:
       x*= arg
    return x
    
#Get the number of testcase as input
n = input()
l = []
#Get element for each test case
for i in range(n):
    l.append(input())
#Perform the final operation
for ind, j in enumerate(l):
	tmp = l.pop(ind)
	print mul(l)
	l.insert(ind, tmp)
