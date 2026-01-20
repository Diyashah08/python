
num = input("Enter a number: ")

if num.startswith('-'):
    num = num[1:]
if num.isdigit():
    print("Number of digits:", len(num))
else:
    print("Invalid input! Please enter a valid number.")
