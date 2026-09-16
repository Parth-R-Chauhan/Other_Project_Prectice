# Self Exercises
# 18. Find all duplicate elements from a list using conditions.

numbers=[10,20,30,10,10,30]

duplicates=[]

for n in numbers:
    if numbers.count(n)>1 and n not in duplicates:
        duplicates.append(n)

print(duplicates) 

# 19. Separate a list into positive, negative, and zero values.

no=[10,0,11,-1,-10]
positive=[]
negative=[]
zero=[]

for n in no:
    if n>0:
        positive.append(n)
    elif n<0:
        negative.append(n)
    else:
        zero.append(n)

print("Positive no :",positive)
print("Negative no:",negative)
print("Zero:",zero)

# 20. Find the largest and smallest number using if.

numbers=[10,20,30,5,990,34]
largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n>largest:
        largest=n

    if n<smallest:
        smallest=n
print(largest)
print(smallest)


# 21. Remove numbers less than 10 from a list.

numbers=[0,1,33,66,2,7]

result=[num for num in numbers if num >= 10]
print(result) 


# 22. Create a list of numbers and generate:
# ● Even numbers
# ● Odd numbers
# ● Numbers divisible by 5

number=[22,33,45,65,43,55]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
div_by_5 = [num for num in numbers if num % 5 == 0]
print("Even Numbers :", evens)
print("Odd Numbers  :", odds)
print("Divisible by 5:", div_by_5)

# 23. Take 5 student names and display only names starting with "A".

students = []
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)
for name in students:
    if name.upper().startswith("A"):
        print(name)

# 24. Create a tuple of marks and display students who scored 70 or more.

marks=(34,56,78,90)

for i in marks:
    if i>=70:
        print(i) 
# 25. Create a list of ages and classify each person as:
# ● < 13 → Child
# ● 13–19 → Teenager
# ● 20–59 → Adult
# ● 60+ → Senior Citizen

ages=[23,5,10,18,60,44]

for age in ages:

    if age<13:
        print(age,"Child")

    elif age<=19:
        print(age,"Teenager")

    elif age<=59:
        print(age,"Adult")

    else:
        print(age,"Senior Citizen")