# Below is the implementation of the above approach
# def printSubsequence(input, output):

#     # Base Case
#     # if the input is empty print the output string
#     if len(input) == 0:
#         print(output, end=' ')
#         return

#     # output is passed with including the
#     # 1st character of input string
#     printSubsequence(input[1:], output+input[0])

#     # output is passed without including the
#     # 1st character of input string
#     printSubsequence(input[1:], output)


# # Driver code
# # output is set to null before passing in
# # as a parameter
# output = ""
# input = "abcd"

# printSubsequence(input, output)

# https://www.geeksforgeeks.org/print-subsequences-string/ 
# Python program to generate power set in lexicographic order.

 # str: Stores input string
 # n: Length of str.
 # curr: Stores current permutation
 # index: Index in current permutation, curr
def printSubSeqRec(str, n, index = -1, curr = ""):
  
  # base case
     if (index == n):
       return
     if (len(curr) > 0):
       print(curr)

     i = index + 1

     while(i < n):
        curr = curr + str[i]
        printSubSeqRec(str, n, i, curr)
        curr = curr[0:-1]
        i = i + 1
       
#  Generates power set in lexicographic order.
#  function
def printSubSeq(str):
   printSubSeqRec(str, len(str))

# // Driver code
str = "cab"
printSubSeq(str)