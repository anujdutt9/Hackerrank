# Question:

# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first  letters of Lilah's infinite string.

s = input().strip()
n = int(input().strip())

print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
