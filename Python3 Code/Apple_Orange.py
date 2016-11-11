# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/apple-and-orange


##S - house starting
##t - house ending
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]

##a - apple tree location
##b - orange tree location
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]

# m - number of apples
# n - number of oranges
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]


# apple - distance from apple tree
# orange - distance from orange tree
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

sum1 = 0
sum2 = 0

for num1 in apple:
    if a + num1 >= s and a + num1 <= t:
        sum1 += 1
for num2 in orange:
    if b + num2 >= s and b + num2 <= t:
        sum2 += 1

print(sum1)
print(sum2)
