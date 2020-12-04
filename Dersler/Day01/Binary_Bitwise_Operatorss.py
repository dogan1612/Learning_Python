# BIT-WISE OPERATORS
# &     |       ^       ~       <<      >>


#  &
#  0 - 0 = 0
#  0 - 1 = 0
#  1 - 0 = 0
#  1 - 1 = 1

# 4 = 1 0 0
# 5 = 1 0 1
print( 4 & 5 )      # 4 or 5 ==> 4
print( 4 or 5 )     # 4

print( 4 and 5 )    # 5
print( 4 | 5 )      # 5

print( 4 ^ 5 )      # 1     (match olursa 0 ==> 0 0 1)

# NOT ~ OPERATOR
# x becomes -(x+1)
print(~7)           # -8

# LEFT SHIFT OPERATOR  <<
print( 3 << 2)       # 12       3 = 1 1 ==> 1 1 0 0 ==12


# RIGHT SHIFT OPERATOR  >>
print( 3 >> 1)       # 1       3 = 1 1 ==> 1 == 1       deletes from right