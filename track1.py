def count(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
def main():
    lst=[1,2,3,3,3,3]
    print(count(lst))
if __name__ == "__main__":
    main()