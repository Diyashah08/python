from functools import reduce

def main():
    numbers = [1, 3, 7, 8, 10]
    m = reduce(lambda a, b: a if a > b else b, numbers)
    print("The maximum is:", m)

if __name__ == "__main__":
    main()
