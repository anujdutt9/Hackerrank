# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/list-comprehensions

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

print([[i,j,k] for i in range(0,X+1) for j in range(0,Y+1) for k in range(0,Z+1) if (i+j+k != N)])

