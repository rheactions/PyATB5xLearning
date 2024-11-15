#Triangle Classifier:
#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

x = float(input('enter length of x : '))
y = float(input('enter length of y : '))
z = float(input('enter length of z : '))

if x == y == z:
    print('Equilateral Triangle')
elif (x == y and x != z) or ( y == z and x != z) or (z == x and y != z ):
    print('isosceles Triangle')
else:
    print('Scalene Triangle')
