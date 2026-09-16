# Python Student Task List — With Conditions
# 1. Collection Datatypes — List & Tuple

# 1. Create a list of 5 student names and use if to check whether a particular name exists.

student=["Ram","Raj","Rahul","Amit","Ramu"]
search_name="Raj"
if search_name in student:
    print("Yes this name is in student list.")
else:
    print("no this name is not in student list.")

# 2. Create a list of numbers and check whether each number is even or odd.

no=[4,6,5,3,2,1,87,66]
for i in no:
    if i % 2==0:
        print(f"Even no: {i}")
    else:
        print(f"Odd no: {i}")


# 3. Create a tuple of marks and check whether each student has passed or failed.

marks=(90,98,88,77,34,57,66)
for i in marks:
    if i >= 40:
        print(f"This { i } mark student are Passed.")
    else:
            print(f"This { i } mark student are Fail.")


# 4. Find the largest number in a list using if conditions.

no=[1,34,2,55,78,43,20]
largest=no[0]
for i in no:
     if i > largest:
          largest=i
print(f"The largest no is {largest}")
          
# 5. Check whether a list is empty or not using a condition.

my_list = []

if not my_list:
    print("list is empty!")
else:
    print("list is not empty.")


# 2. Mutability — List & Tuple

# 6. Create a list and change an element only if the index is valid.

numbers = [10, 20, 30, 40]
index_change = 2
new_value = 50
if index_change < len(numbers):
    numbers[index_change] = new_value

print(numbers) 


# 7. Create a tuple and check whether a particular value exists before accessing it.

t=("Apple","Banana","Watermelon")
search="Watermelon"
if search in t:
    position = t.index(search)
    print(f"Found '{search}' at index {position}: {t[position]}")
else:
    print(f"'{search}' does not exist in the tuple.")

# 8. Write a program to demonstrate that a list can be modified but a tuple cannot be modified.

list1=[10,20,30]
list1[1]=50
print(list1)

tuple1=(10,20,30)
try:
    tuple1[1]=50
except TypeError:
    print("tuple is not modified")


# 9. Check whether a given collection is a list or tuple using if-elif-else.

data=(1,2,3)

if type(data)==list:
    print("It is a List.")
elif type(data)==tuple:
    print("It is a Tuple.")
else:
    print("Unknown Collection.") 



# 3. List Comprehension with Conditions

# 10. Create a list of numbers from 1–20 and generate only even numbers.

even=[e for e in range(1,21) if e%2==0]
print(even)


# 11. Generate only odd numbers from 1–20.

odd=[o for o in range(1,21) if o%2!=0]
print(odd)


# 12. Generate numbers divisible by 3 from 1–50.

div=[d for d in range(1,51) if d%3==0]
print(div)


# 13. From a list of marks, create a new list containing only marks greater than or equal to 40.
l1=[40,30,35,90,67,70]
l2=[marks for marks in l1 if marks>=40]
print(l2)


# 14. From a list of numbers, create a new list containing numbers greater than 10 and less than 50.

l1=[11,5,1,40,35,22,77]
l2=[no for no in l1 if no>10 and no<50]
print(l2)


# 15. From a list of names, create a new list containing names whose length is greater than 5.
list_name=["Ram","Raj","Ramraj"]
name=[n for n in list_name if len(n)>5]
print(name)
