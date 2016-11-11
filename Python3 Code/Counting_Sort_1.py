# Solution to Hackerrank Problem for Counting Sort 1 under Algorithms:

n = int(input())
ar = [num for num in input().strip().split(' ')]

count = 0

for i in range(0,100):
    for j in range(0,100):
        if i == ar[j]:
            count += 1
            
    print(count,end=" ")
    count = 0
    
    
