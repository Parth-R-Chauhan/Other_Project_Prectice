# Task 1 – Student Result Analyzer 
# Create a program that accepts student name, 5 subject marks, and displays: 
# ● Total and percentage ● Grade ● Highest and lowest marks ● Pass/Fail 
# Use: UDF, arguments, return values, built-in functions. 

def result(name,marks_list):
    total_mark=sum(marks_list)
    per=total_mark/5
    highest_mark = max(marks_list)
    lowest_mark = min(marks_list)

    if per>=90:
        grade="A"
    elif per>=80:
        grade="B"
    elif per>=70:
        grade="C"
    elif per>=60:
        grade="D"
    elif per>=50:
        grade="E"
    else:
        grade="F"

    final="Pass" if all(mark>=40 for mark in marks_list) else "Fail"

    return total_mark,per,grade,highest_mark,lowest_mark,final

name=input("Enter your Name:")
marks=[]
print("Enter Your 5 Subject Marks")
for i in range(5):
    mark=float(input(f"Enter your {i+1} subject mark: "))
    marks.append(mark)

total_mark,per,grade,highest_mark,lowest_mark,final=result(name,marks)

print("="*30)
print(f"Student name: {name}")
print(f"Total Marks   : {total_mark} / 500")
print(f"Percentage    : {per:.2f}%")
print(f"Grade         : {grade}")
print(f"Highest Mark  : {highest_mark}")
print(f"Lowest Mark   : {lowest_mark}")
print(f"Final Status  : {final}")
print("="*30)


