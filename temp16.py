def sq(num):
    return num**2
def main():
    nums=[2,4,6,8]   
    square=map(sq,nums)
    print(list(square))

if __name__ == "__main__":
    main()