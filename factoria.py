def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))
except ValueError as e:
    print("Error:", e)
