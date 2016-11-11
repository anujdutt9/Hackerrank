# Solution Program for Hackerrank Problem at:
# https://www.hackerrank.com/challenges/basic-probability-puzzles-1

case = 0
def fract(num,den):
    small = min(num,den)
    for i in range(small, 1, -1):
        if num%i == 0 and den%i == 0:
            return '{}/{}'.format(int(num/i),int(den/i))

for i in range(1,7):
    for j in range(1,7):
        if (i+j) <= 9:
            case += 1

print(fract(case,36))

