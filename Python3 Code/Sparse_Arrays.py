# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/sparse-arrays

N = int(input())
input_string = [input() for _ in range(N)]
Q = int(input())
query_string = [input() for _ in range(Q)]

count = 0

for i in range(Q):
    for j in range(N):
        if (query_string[i] == input_string[j]):
            count += 1
    print(count)
    del(count)
    count = 0

