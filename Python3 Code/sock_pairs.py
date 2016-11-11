# John's clothing store has a pile of 'n' loose socks where each sock 'i' is labeled with an integer, ci, denoting its color. 
# He wants to sell as many socks as possible, but his customers will only buy them in matching pairs. Two socks, i and , j
# are a single matching pair if ci = cj.
# Given  and the color of each sock, how many pairs of socks can John sell?


n = int(input().strip())                                            # Input total number of socks
c = [int(c_temp) for c_temp in input().strip().split(' ')]          # Enter the "labels" as integer 
total = 0

for x in set(c):
    total += c.count(x) // 2                # Count number of appearances of each sock and divide by two to get total number of pairs  

print(total)
    
