def main():
    customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
    ]
    valid= list(filter(lambda customer: customer["active"], customers))
    total_revenue = 0
    for customer in valid:
        valid_purchases = filter(lambda p:p >=100,customer["purchases"])
        total_revenue += sum(map(lambda x: x*1.1,valid_purchases))
    print(total_revenue) 
if __name__ == "__main__":
    main()