def main():
    numbers = [2, 5, 4, 2, 8, 9, 5, 3, 6, 2, 4]
    result = []

    for i in numbers:
        if i not in result:
            result.append(i)

    print("Unique elements:", result)

if __name__ == "__main__":
    main()
