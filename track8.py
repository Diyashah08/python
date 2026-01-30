def main():
    lst=[1,2,3,4,5,6,8]
    lst2=[]
    for i in lst:
        if i%2==0:
            lst2.append(i)
    print(lst2)
if __name__ == "__main__":
    main()