# Task 3 – Student Information System 
# Create a function that accepts student details such as name, age, course, city, mobile, etc., and displays them.
# Use: **kwargs and __doc__. 

def display_student_profile(**details):
    """
    Accepts student details name, age, course, mobile , city. 
    using keyword arguments (**kwargs) and prints a structured profile.
    """
    
    print(f"\n{display_student_profile.__doc__}")
    
    print("==================================")
    print("        STUDENT PROFILE           ")
    print("==================================")
    
   
    for key, value in details.items():
        print(f"{key} : {value}")
        
    print("==================================")



display_student_profile(
    name="Rahul ", 
    age=21, 
    course="Python", 
    city="Junagadh", 
    mobile="1234567890"
)


