# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/python-lists

n = int(input())
l = []
for _ in range(n):
    s = input().strip().split(' ')
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "("+",".join(args)+ ")"
        eval("l."+cmd)
    else:
        print(l)
    
