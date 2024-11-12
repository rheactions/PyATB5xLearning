#Task 3 Problem to find the max between two ( 3,4) → 4

Num_1 = float(input('Enter first number :'))
Num_2 = float(input('Enter Second number :'))

result = max(Num_1,Num_2)

print(max(Num_1,Num_2))
#or

print("\nnum_1 is greater" if Num_1 > Num_2 else "Num_2 is greater")
# or

print(f'\nGreater number is : {result:.2f}')