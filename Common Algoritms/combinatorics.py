# Factorial
math.factorial(23)


# Unique pairs in a list
# 4 items:
# A
# B
# C
# D
# 6 unique pairs possible:

# AB
# AC
# AD
# BC
# BD
# CD
# (n(n-1))/2


# Binomial coefficients
# The binomial coefficient (n, k) equals the number of ways we can choose a subset
# of k elements from a set of n elements. 
import math
def binc(n, k):
    if 0 <= k <= n:
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    else:
        return 0
n = 5
k = 2
result = binc(n, k)
print(f"The binomial coefficient C({n}, {k}) is: {result}")

# OR
# import scipy.special

# the two give the same results 
# scipy.special.binom(10, 5)
