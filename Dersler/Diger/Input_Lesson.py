# Find square root of real or complex numbers

num = float(input('Enter a number: '))          # To take the input from the user:

num1 = input('Enter a number: ')
num1 = float(num1)                              # Converting String to number

num2 = 9

num_sqrt = num2 ** 0.5
print('The square root of %0.0f is %0.3f'%(num ,num_sqrt))
# The square root of 9 is 3.000

print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
# The square root of 9.000 is 3.000

print('The square root of %0f is %0.3f'%(num ,num_sqrt))
# The square root of 9.000000 is 3.000

# Importing the complex math module     ==> used after line 24
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)              # we use the sqrt() function in the cmath (complex math) module.
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))