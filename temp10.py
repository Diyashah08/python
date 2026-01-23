def main():
    inp=[1,3,5,6,7]
    number=int(input("enter a number to search:"))
    for i in range(len(inp)):
        if (inp[i]==number):
            print("Index of the number is :",i)
            break
if __name__=="__main__":
    main()