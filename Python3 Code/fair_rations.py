# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/fair-rations

count = 0
N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

if (sum(B)%2 != 0):
    print('NO')
else:
    for i in range(0, N-1):
        if (B[i]%2 != 0):
            B[i] = B[i] + 1
            B[i+1] = B[i+1] + 1
            count += 2
    print(count)

