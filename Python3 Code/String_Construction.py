# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/string-construction

p = []
total = 0

n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    for char in s:
        if char not in p:
            p.append(char)
            total += 1
        else:
            total += 0
    print(total)
    del p[:]
    total = 0
    
    
