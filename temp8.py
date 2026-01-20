def main():
    numbers = [2, 5, 4, 2, 8, 9, 5, 3, 6, 2, 4]
    unique = []

    for i in numbers:
        if i not in unique:
            unique.append(i)
        else:
            pass  

    print("List after removing duplicates:", unique)

if __name__ == "__main__":
    main()
