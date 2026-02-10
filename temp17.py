def vowel(n):
    v=['a','e','i','o','u']
    if n in v:
        return True
    else:   
        return False
def main():   
    list=['a','b','c','d','e',]
    vowels=filter(vowel,list)
    for i in vowels:
        print(i)

if __name__ == "__main__":
    main()