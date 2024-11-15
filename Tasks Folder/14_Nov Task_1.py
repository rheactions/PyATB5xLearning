#Checking for a Leap Year , 2024 → Yes
#Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

'''step 1 : define input and output
ipt -> leap year -> int
opt -> yes or no -> str'''

'''step 2 : rough logic
there would be three condition
if x is divisible by 4 else not leap 
if x is not divisible by 100 else not leap
if x is divisble by 400 else not leap

if the year is divisible by 4, 
then check if it is divisible by 100 
(and if divisible by 100, it should further check if divisible by 400).'''



x = int(input('Enter the year: '))

if x % 4 == 0  and (x % 100 != 0 or x % 400 == 0):
    print('leap year')
else:
    print('not a leap year')