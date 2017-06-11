# Counting Valleys
# https://www.hackerrank.com/challenges/counting-valleys?h_r=next-challenge&h_v=zen


n = int(input())
s = input()

def Valley(s):
    valley, current_level = 0,0
    for step in s:
        if step == 'D':
            current_level -= 1
        else:
            if current_level == -1:
                valley += 1
            current_level += 1
    return valley

print(Valley(s))
