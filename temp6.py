def main():
    numbers = [3, 5, 2, 4, 1]
    result = []
    total = 0

    for i in numbers:
        total += i
        result.append(total)

    print("Cumulative sums:", result)

if __name__ == "__main__":
    main()
