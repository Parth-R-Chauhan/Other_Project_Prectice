# 1. Join Strings Join a list of city names using " - ". 

city=["Junagadh","Rajkot","Surat"]
final_city=" - ".join(city)
print(final_city)


# 2. Join Strings Join a list of programming languages using " | ". 

language=["Java","Python",".net"]
final=" | ".join(language)
print(final)

# 3. Strip Remove extra spaces from both sides of a string. 

text="     python    "
print(text.strip())


# 4. Lstrip Remove spaces only from the left side of a string. 

text="     python    "
print(text.lstrip())


# 5. Rstrip Remove spaces only from the right side of a string. 

text="     python    "
print(text.rstrip())


# 6. Remove Non-Alphabetic Characters Remove numbers and special characters from a string. 

text="python@1234"
clean_text = ""

for char in text:
  if char.isalpha():
    clean_text += char

print(text)
print(clean_text)


# 7. Keep Only Numbers Extract only numeric characters from a string. 

text="python@1234"
digit=""
print(text.isdigit)
for i in text:
  if i.isdigit():
    digit += i
print(text)
print(digit)


# 8. String Checking Check whether different strings are alphabetic, numeric, lowercase, uppercase, or spaces.

text= "python@123"
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())

text= "python"
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())

text= " "
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())

# 9. Reverse String Reverse a string using slicing. 

text="python"
print(text[::-1])


# 10. Reverse String Reverse a string using reversed() and join(). 

text="python"
print("".join(reversed(text)))


# 11. Reverse String Reverse a string by converting it into a list and using .reverse(). 

text="python"
list_text=list(text)
list_text.reverse()
print(list_text)

# 12. Palindrome Take a string from the user and check whether it is a palindrome. 

text=input("enter string:")
reverse_text = text[::-1]
if text==reverse_text:
  print("It is a palindrome")
else:
  print("It is a not palindrome")
  
# 13. Palindrome Number Take a number from the user and check whether it is a palindrome.

no=int(input("enter no:"))
str_no=str(no)
reverse=str_no[::-1]
r_no=int(reverse)
if no==r_no:
  print("It is a palindrome")
else:
  print("It is a not palindrome")


# 14. Escape Characters Print text using \n, \t, \", \', and \\. 

print("python\njava")
print("python\tjava")
print("py thon \"java\"")
print('python\'s java')
print("java:\\Python")


# 15. Combined String Task Remove extra spaces, remove non-alphabetic characters, find length, reverse the string, and check whether it is a palindrome.
text="    python@123   "
print("Remove extra spaces:" ,text.strip())
clean_text = ""

for char in text:
  if char.isalpha():
    clean_text += char

print("remove non-alphabetic characters",clean_text)
print(f"the string of {text} is length {len(text)}")
r_text=text[::-1]
print("reverse the string:",r_text)
if text==r_text:
  print("It is a palindrome")
else:
  print("It is a not palindrome")


  


