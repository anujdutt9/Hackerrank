# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/find-digits

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (len([i for i in list(str(n)) if int(i)!=0 and n%int(i)==0]))
    
