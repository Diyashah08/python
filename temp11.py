def main():
    inp=[2,3,3,5,7,8,9]
    user_input=int(input("Enter a number to check:"))
    flag=0
    for i in range(len(inp)):
        for j in range(len(inp)):
            if inp[i]+inp[j]==user_input:
                print("2 no. to add are:" , inp[i],inp[j])
                flag=1
                break
            else:
                continue
        if flag == 1:
            break
        else:
            continue
if __name__ == "__main__":
    main()