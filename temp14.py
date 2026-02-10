def num_char(num):
    return chr(num)
def main():
    numbers=[72,69,76,76,79]
    characters=map(num_char, numbers)
    print(list(characters))

if __name__ == "__main__":
    main()