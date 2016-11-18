# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/beautiful-triplets

n,d = input().strip().split(' ')
n,d = [int(n),int(d)]
A = [int(num) for num in input().strip().split(' ')]

count = 0

for i in range(n):
    if A[i]+d in A and A[i]+2*d in A:
        count += 1

print(count)            
  
