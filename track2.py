def main():
    dict={"a":2,"b":1,"c":3}
    print("Enter key to check")
    key=input()
    if key in dict:
        print("Key found")
    else:
        print("key not found")
if __name__ == "__main__":
    main()