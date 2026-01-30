def main():
    str="programming"
    tup1=()
    for i in str:
        if i not in tup1:
            tup1+=(i,)
        else:
            continue
    print(tup1)
if __name__ == "__main__":
    main()