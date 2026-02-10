import functools

def factorial(n):
    if n == 0:
        return 1
    else:
        return functools.reduce(lambda x, y: x * y, range(1, n + 1))

def main():
    print(factorial(3))

if __name__ == "__main__":
    main()
