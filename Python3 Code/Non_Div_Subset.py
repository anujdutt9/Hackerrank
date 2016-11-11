# Solution to Hackerrank Problem:
# https://www.hackerrank.com/challenges/non-divisible-subset


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

arr = []
arr = [int(num) for num in input().strip().split(' ')]

total = 0

d = {x:[] for x in range(k)}
for i in range(n):
    d[arr[i]%k].append(arr[i])


if len(d[0]) > 0:
    total = 1

S = set([(x,k-x) for x in range(1,k//2+1)])

for i,j in S:
    if i != j:
        if len(d[i]) > len(d[j]):
            total += len(d[i])
        else:
            total += len(d[j])
    else:
        if len(d[i]) > 0:
            total += 1

print (total)
