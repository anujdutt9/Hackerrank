# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

N = int(input())
A = [int(num) for num in input().strip().split(' ')]
a = max(A)

while max(A) == a:
    A.remove(max(A))
print(max(A))

