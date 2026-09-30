# Task 7 – Student Marks List 
# Create a 1D list containing student marks and perform: 
# ● Add marks ● Update marks 
# ● Delete marks ● Search marks 
# ● Sort ascending/descending 
# ● Find highest/lowest ● Calculate total and average 

array_1=[90,70,50,98,88]
print("1D Array : ",array_1)

array_1.append(95)
print("Add 95 in araay : ",array_1)

array_1[1]=77
print("Update 70 to 77 in araay : ",array_1)

array_1.remove(50)
print("Remove 50 in araay : ",array_1)

search= 90
if search in array_1:
    print(f"{search} Found in Array")
else:
    print(f"{search} not Found in Array")

asc=sorted(array_1)
print("Sort ascending Order: ",asc)

dec=sorted(array_1,reverse=True)
print("Sort descending Order: ",dec)
    
highest = max(array_1)
lowest = min(array_1)
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")

total=sum(array_1)
avg=total/len(array_1)
print("total :",total)
print("average :",avg)