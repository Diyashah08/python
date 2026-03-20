class NegativeNumberError(Exception):
    pass
try:
    num=int(input("Enter the number"))
    if num<0:
        raise NegativeNumberError("Negative no.not allowed")

    print("you entered",num)
except NegativeNumberError as e:
    print(" Custom Error:",e)
    