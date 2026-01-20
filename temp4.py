def cal(unit):
    if unit>200:
        price = 100 * 1 + 100 * 2 + (unit - 200)*3
        
    elif unit >100:
        price = 100 * 1 + (unit - 100)*2
    else:
        price=unit*1
        
    return price 
    
def main():
    
    Amount = cal(201)
    print("Total Amount",Amount)

if __name__=="__main__":
 main()
    