def main():
    words=[" python "," AI "," Machine "," data "]
    result=list(map(lambda x: x.strip().lower(),words))
    final_result=list(filter(lambda x:len(x)>=5,result))
    print(final_result)
    
if __name__ == "__main__":
    main()