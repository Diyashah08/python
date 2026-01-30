def main():
    inp=[2,4,3,2,6,5,6,6,6,5,5]
    max_count=0
    element=-1
    for i in range(len(inp)):
        count=0
        for j in range(len(inp)):
            if inp[i]==inp[j]:
                count+=1
        if count>max_count:
            max_count=count
            element=inp[i]
    print("Element with maximum count:",element)
    print("Maximum count is:",max_count)
if __name__ == "__main__":
    main()