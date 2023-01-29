number = int(input("Please Enter any Number: "))
reverse = 0
while(number > 0):
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    number = number //10
print("\nReverse of entered number is =",reverse)