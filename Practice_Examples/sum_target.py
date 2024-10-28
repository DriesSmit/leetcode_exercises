"""
arr = [2, 7, 11, 15]
target = 9

Find the two numbers that sum up to the target.

1) 

if arr[i] < target:
    search through array from start to finish and search for the the remainder.

Worst case O(n^2). Memory O(n).

2)
Initialise a hash table.
We can go through the array.
For every element we check < target and if the remainder is in the hash table.
Otherwise we hash it. This has linear complexity.

"""