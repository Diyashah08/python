try:
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the Second number"))
    
    result=num1 / num2
    print("Result:",result)
except ZeroDivisionError:
    print("Error : Cannot divide by zero")