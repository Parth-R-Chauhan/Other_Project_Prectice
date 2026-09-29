
Hra = 0.20  
Da = 0.40   


def calculate_salary(basic_pay):
    
    global Hra, Da
    
    hra = basic_pay * Hra
    da = basic_pay * Da
    salary = basic_pay + hra + da
    
    
    return hra, da, salary


emp = float(input("Enter Employee Basic Salary: "))


hra, da, salary = calculate_salary(emp)


print("\n----------------------------")
print(f"Basic Salary : ₹{emp:.2f}")
print(f"HRA (20%)    : ₹{hra:.2f}")
print(f"DA (40%)     : ₹{da:.2f}")
print("----------------------------")
print(f"FINAL SALARY : ₹{salary:.2f}")
print("----------------------------")
