#Function To Sort A List
def solve(l):
  l = sorted(l, reverse=True)
	i = 0
	while i < 4:
		print l[i]
		i = i + 1

# Getting Inputs
n = input()
l = []
for line in range(n):
	l.append(input())

solve(l)

