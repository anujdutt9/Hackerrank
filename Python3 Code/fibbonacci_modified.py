# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/fibonacci-modified

t1,t2,n = list(input().strip().split(' '))

n = int(n)
t1 = int(t1)
t2 = int(t2)

t = []*n
t.append(t1)
t.append(t2)

for i in range(0,n-1):
    t.append(t[i] + (t[i+1]*t[i+1]))

print(t[n-1])

