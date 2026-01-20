def week(i):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(i, "Invalid day")

def main():
    day = week(3)
    print("Day is:", day)

if __name__ == "__main__":
    main()
