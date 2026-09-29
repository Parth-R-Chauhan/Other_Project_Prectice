# Task 5 – Number Utility 
# Create a menu-driven program with options: 
# 1. Factorial 
# 2. Fibonacci 
# 3. Reverse Number 
# 4. Sum of Digits 
# Use: Recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)



while True:
    
    print("1. Factorial")
    print("2. Fibonacci Series")
    print("3. Reverse Number")
    print("4. Sum of Digits")
    print("5. Exit")
    
    choice = int(input("\nEnter your choice (1-5): "))
    
    if choice == 1:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num} is: {factorial(num)}")
        
    elif choice == 2:
        terms = int(input("Enter number of terms to print: "))
        print("Fibonacci Series: ", end="")
        for i in range(terms):
            print(fibonacci(i), end=" ")
        print() 
        
    elif choice == 3:
        num = int(input("Enter a number: "))
        print(f"Reversed Number is: {reverse_number(num)}")
        
    elif choice == 4:
        num = int(input("Enter a number: "))
        print(f"Sum of digits of {num} is: {sum_of_digits(num)}")
        
    elif choice == 5:
        print("Thank you.")
        break
        
    else:
        print("Invalid choice")
