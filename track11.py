def main():
    lst=[("Pen", 10), ("Pencil", 25), ("Pen", 15)]
    max_val = 0
    item = ""
    for i in range(len(lst)):
        if max_val < lst[i][1]:
            max_val = lst[i][1]
            item = lst[i][0]
    print(item) 
if __name__ == "__main__":
    main()       
            
    