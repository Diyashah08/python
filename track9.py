def main():
    lst=[("Alice", [80, 90]), ("Bob", [70, 85, 90])]
    tup1=()
    for(name , scores) in lst:
        avg=sum(scores)/len(scores)
        avg=round(avg,2)
        name=name.lower()
        tup1+=(name,avg),
    print(tup1)
if __name__ == "__main__":
    main()