def main():
    dict1={"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
    dict2 = {}
    
    for key in dict1:
        count = dict1[key].count("p")
        attendence = (count/ len(dict1[key])) * 100
        attendence = round(attendence, 2)
        dict2[key] = attendence
    print(dict2)
    
if __name__ == "__main__":
    main()