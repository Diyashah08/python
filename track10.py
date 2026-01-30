def main():
    str="Python is great and Python is easy"
    dict1={}
    for word in str.split():
        dict1[word]=str.count(word)
    print(dict1)
    
if __name__ == "__main__":
    main()