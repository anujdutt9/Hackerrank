# Solution to Problem 1 of Hackerrank Week of Code 31
# Beautiful Words


w = input().strip()
# Print 'Yes' if the word is beautiful or 'No' if it is not.
vowels = ['a','e','i','o','u','y']

f = True

for i in range(0,len(w)-1):
    if w[i] in vowels:
        if w[i+1] in vowels:
            print('No')
            f = False
            break
    elif w[i] == w[i+1]:
        print('No')
        f = False
        
if (f):
    print('Yes')
