# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()
 
# importing "bisect" for bisection operations
import bisect
 
"""
 This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending 
position which has to be considered.
bisect.bisect_left(a, x, lo=0, hi=len(a))
"""

# initializing list
li = [1, 3, 4, 4, 4, 6, 7]
 
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print ("Rightmost index to insert, so list remains sorted is : ",
       end="")
print (bisect.bisect(li, 4))
 
# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print ("Leftmost index to insert, so list remains sorted is : ", 
       end="")
print (bisect.bisect_left(li, 4))
 
# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print ("Rightmost index to insert, so list remains sorted is : ",
       end="")
print (bisect.bisect_right(li, 4, 0, 4))