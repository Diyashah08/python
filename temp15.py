def ascii(char):
    return ord(char)

def main():
    characters = ['A','B','C','D']
    ascii_val = map(ascii,characters)
    print(list(ascii_val))

if __name__ == "__main__":
    main()