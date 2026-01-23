def main():
    inp1 = int(input("Enter the first number:"))
    inp2 = int(input("Enter the second number:"))
    inp3 = int(input("Enter the third number:"))

    permut=[]
    for i in[inp1,inp2,inp3]:
        for j in [inp1,inp2,inp3]:
            for k in [inp1,inp2,inp3]:
                if i!=j and j!=k and i!=k:
                    permut.append((i,j,k))
    print("All possible permutations are:")
    for p i permmut:
        print(p)
if __name__ == "__main__":
    main()