# Python String Formatting & Manipulation 

# 1. Create a variable student_name and print its value using a string.

student_name="xyz"
print(student_name)


# 2. Create a variable course_name and display it using a multiline string. 

course_name="""Ai & Ml
It is very Important course"""
print(course_name)


# 3. Create the string "DataScience" and print the character at index 2. 

txt="DataScience"
print(txt[2])


# 4. Create the string "DataScience" and print the last two characters using negative indexing. 

txt="DataScience"
print(txt[-1])
print(txt[-2])


# 5. Create the string "DataScience" and print characters from index 1 to 5. 

txt="DataScience"
print(txt[1:6])


# 6. Create the string "DataScience" and print it in reverse order using slicing. 

txt="DataScience"
print(txt[::-1])


# 7. Create first = "Amit" and surname = "Patel" and create complete_name using +. 

first = "Amit"
surname = "Patel"
fullname=first+" "+surname
print(fullname)


# 8. Create product = "Mobile" and amount = 25000 and display both values using an f-string. 

product = "Mobile" 
amount = 25000
print(f"The {product} price is a {amount} .")


# 9. Create product = "Keyboard" and amount = 799.567 and display the amount with 2 decimal places using an f-string. 

product = "Keyboard" 
amount = 799.567
print(f"The {product} price is a {amount:.2f} .")


# 10. Create x = 15 and y = 25 and display their addition inside an f-string. 

x = 15 
y = 25
print(f"Addition is {x+y}")


# 11. Create employee, department, and salary variables and display them using format() with {}. 

employee="Ram"
department="It"
salary=50000
print(f"A {employee} is work in {department} department in a big company  and it`s sallary is {salary}. ")


# 12. Create name and designation variables and display them using positional arguments {0} and {1}. 

name="Ram"
designation="Project Manager"
print("A {0} as work in {1} in a big company.".format(name,designation))


# 13. Create name, city, and course variables and display them using named arguments with format(). 

name="Ram"
city="Junagadh"
course="Ai & Ml"
print("A {first} Lives in {second} and doing a {third} Course. ".format(first=name,second=city,third=course))


# 14. Create brand = "Apple" and model = "iPhone" and display Brand and Model using an f-string. 

brand = "Apple" 
model = "iPhone"
print(f"The {brand} company is lounch new {model} model .")


# 15. Create student = "Neha" and marks = 85.4567 and display 85.46 using an f-string. 

student = "Neha" 
marks = 85.4567
print(f"The {student} is achive {marks:.2f} marks in a school.")


# 16. Create a = 50 and b = 30 and display their sum, difference, and multiplication using expressions inside an f-string. 


a = 50
b = 30
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Multiplication: {a * b}")


# 17. Create name = "Kiran" and city = "Rajkot" and display: Kiran lives in Rajkot. using format(). 

name = "Kiran" 
city = "Rajkot"
print(f"{name} lives in {city}")


# 18. Create item = "Laptop", price = 45000, and quantity = 2, then display the total price using an expression inside an f-string. 

item = "Laptop"
price = 45000
quantity = 2
print(f"A {item} price is {price} and we bay a {quantity} quantity and its total price is {price * quantity}.")


# 19. Create first_name = "Ravi", last_name = "Mehta", and course = "Python", then display the sentence using named arguments with format(). 

first_name = "Ravi"
last_name = "Mehta"
course = "Python"
print(f"{first_name} {last_name} is doing a {course} Course ")


# 20. Create a small student information program using student name, course, city, and marks. Display the complete information using f-string formatting and show marks with 2 decimal places.
student_name="Ram"
course="Python"
city="Junagadh"
marks=85.74

print("Student Information")
print(f"Name : {student_name}")
print(f"course : {course}")
print(f"city : {city}")
print(f"marks : {marks:.2f}")

