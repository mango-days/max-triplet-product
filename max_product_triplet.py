# Given an integer array, find a triplet having the maximum product.

# Input:  { -4, 1, -8, 9, 6 }
# Output: The triplet having the maximum product is (-4, -8, 9)
 
# Input:  { 1, 7, 2, -2, 5 }
# Output: The triplet having the maximum product is (7, 2, 5)

array = [ -4, 1, -8, 9, 6 ]
array.sort()

ans1 = array [ : 2 ] + array [ -1 : ]
ans2 = array [ -3 : ]

product1 = 1
product2 = 1
for index in range ( len ( ans1 ) ) : product1 *= ans1 [ index ]
for index in range ( len ( ans2 ) ) : product2 *= ans2 [ index ]

if product1 > product2 : print ( ans1 )
else : print  ( ans2 )