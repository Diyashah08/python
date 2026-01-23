def main():
    num1 = [2, 6, 8]
    num2 = [1, 2, 7, 8, 9]
    result=num1+num2

    for i in range(len(result)-1):
        for j in range(len(result)-1):
            if result[j]>result[j+1]:
                temp=result[j]
                result[j]=result[j+1]
                result[j+1] = temp
            else:
                    continue  
    
    print("Merged list:", result)

if __name__ == "__main__":
    main()
