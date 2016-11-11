# Solution to Hackerrank problem at:
# https://www.hackerrank.com/challenges/circular-array-rotation

def rotate(l, x=1):
   if len(l) == 0:
      return l
   x = -x % len(l)     
   return l[x:] + l[:x]

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a2 = []
a = [int(a_temp) for a_temp in input().strip().split(' ')]
for a0 in range(q):
    m = int(input().strip())
    a2.append(m)

a1 = []
a1 = rotate(a,k)

for i in a2:
    print(a1[i])

