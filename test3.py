def main():
    products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
    ]
    electronics = filter(lambda p:p[1] == "Electronics" , products)
    total_discounted_price = sum(map(lambda X:X[2]*0.8,electronics))
    print(total_discounted_price)
if __name__ == "__main__":
    main()
    