# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/reduced-string

s = input()
arr = []

for i in range(len(s)):
    if not arr or s[i] != arr[-1]:
        arr += s[i]
    else:
        arr.pop()

if arr:
    arr = ''.join(arr)
    print(arr)
else:
    print('Empty String')
