# Task 2 – Shopping Bill System 
# Create a program that accepts multiple products and prices and generates a final bill. 
# Use: *args, functions, sum(), max(), min(). 


def generate_shopping_bill(**products):
   
    prices = products.values()
    
    total = sum(prices)       
    maximum = max(prices)   
    minimum = min(prices)    
    
    print("\n------------------------------")
    
    for name, price in products.items():
        print(f"{name} : ₹{price}")
        
    print("------------------------------")
    print(f"Total Amount    : ₹{total}")
    print(f"Highest Price   : ₹{maximum}")
    print(f"Lowest Price    : ₹{minimum}")
    print("------------------------------")



generate_shopping_bill(Laptop=45000, Mobile=15000, Cover=500, Headphones=2500)
