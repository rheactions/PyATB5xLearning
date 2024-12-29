# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1
from math import remainder

num_1 = int(input('Enter First num : '))
num_2 = int(input('Enter Second num : '))

Q = num_1 / num_2
R = num_1 % num_2

print('Quotient of the two numbers is ', int(Q), '\nRemainder of the two number is ',R)


