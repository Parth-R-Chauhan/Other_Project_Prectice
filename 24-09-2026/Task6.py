# Task 6 – Quick Calculator 
# Create a calculator using Lambda functions 
# for: ● Addition ● Subtraction ● Multiplication ● Division ● Square 
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
division = lambda x, y: x / y 
square = lambda x: x ** 2


while True:
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    
        
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {division(num1, num2)}")
            
    elif choice == '5':
        num = float(input("Enter number to square: "))
        print(f"Result: {square(num)}")

    elif choice == '6':
        print(" Thank you!")
        break
        
    else:
        print("Invalid Choice! ")
