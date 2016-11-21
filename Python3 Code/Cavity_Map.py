# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/cavity-map

n = int(input())
arr = [[num for num in input()] for _ in range(n)]



for i in range(1,n-1):
    for j in range(1,n-1):
        if (arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i][j+1]):
            arr[i][j] = 'X'

for i in range(n):
        print(''.join(str(x) for x in arr[i]))

