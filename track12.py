def main():
    dict1={"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
    lst1=[]
    for key in dict1:
        for i in range(len(dict1[key])):
            if dict1[key][i] not in lst1:
                lst1.append(dict1[key][i])
    lst1.sort()
    print(lst1)
if __name__ == "__main__":
    main() 