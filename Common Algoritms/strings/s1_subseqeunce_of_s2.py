# Iterative JavaScript program to check
# If a string is subsequence of another string

# Returns true if s1 is subsequence of s2


def issubsequence(s1, s2):

    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n


# driver code
s1 = "gksrek"
s2 = "geeksforgeeks"
if (issubsequence(s1, s2)):
    print("gksrek is subsequence of geekforgeeks")
else:
    print("gksrek is not a subsequence of geekforgeeks")

# This code is contributed by shinjanpatra