# Python String  
# 1. String Formatting: Create a sentence using %s and %d to display a teacher's name, subject, and experience. 

teacher_name="RAM"
subject="Maths"
experience=5
print("A teacher name %s teaches %s to boys and has %d years of experience ."%(teacher_name,subject,experience))


# 2. Float Formatting: Create a sentence using %.2f to display a movie name and its rating. 

movie_name="xyz"
rating=3.5
print("A movie name is %s and its rating is %.2f"%(movie_name,rating))


# 3. Case Conversion: Create a sentence about summer vacation and apply upper(), lower(), title(), capitalize(), and swapcase(). 

sentance="Summer Vacation is fun vacation"
print(sentance.upper())
print(sentance.lower())
print(sentance.title())
print(sentance.capitalize())


# 4. String Searching: Create a sentence containing the word Java and find its position using find(). 

text="The java language is a used for secutity."
print(text.find("java"))


# 5. Membership: Create a sentence about food and check whether pizza exists using the in operator. 

text="In a resto best food is a pizza"
print("pizza" in text)


# 6. String Index: Create the string Elephant and print specific characters using positive and negative indexing. 

t="Elephant"
print(t[1])
print(t[4])
print(t[-1])
print(t[-4])


# 7. Start & End: Create a sentence about a movie and check whether it starts with The using startswith() and ends with ! using endswith(). 

text="A movie name is xyz and its rating is 3.5"
print(text.startswith("A"))
print(text.endswith("."))
print(text.endswith("3.5"))


# 8. String Replacement: Create a sentence about cricket containing the word India and replace India with Team India using replace(). 

text="This yesr India is win cricket trophy."
print(text.replace("India","Team India"))


# 9. Replace One Occurrence: Create a sentence containing car multiple times and replace only the first occurrence using replace() with count 1. 

text="A new car is better then old car."
print(text.replace("car","Bick",1))

# 10. String Counting: Create a sentence about travel and count how many times the character a appears using count(). 

t="We are Enjoy in traveling"
print(t.count("a"))

# 11. Split Comma: Create a comma-separated string containing mobile brands and convert it into a list using split(","). 

mobile_brand="Oppo,Oneplus,Samasang,Vivo"
print(mobile_brand.split(","))


# 12. Split Words: Create a sentence about education and convert it into a list of words using split(). 

education="Education is very important for everyone"
print(education.split())


# 13. Multiline String: Create a multiline string containing different cities of Gujarat, then split it using split("\n"). 

gujarat=''' Junagadh
Rajkot
Amreli
'''
print(gujarat.split("\n"))


# 14. For Loop: Create a multiline string containing five animal names, split it using split("\n"), and print each animal using a for loop. 

animal='''Dog
Cat
Lion
Elephant
Cow
'''
animals = animal.split("\n")
print(animals)

for i in animals:
  print(i)


# 15. Combined Task: Create a sentence about a shopping order containing product name, quantity, price, and customer name. Use % formatting, upper(), lower(), find(), replace(), count(), and split() on the data.
customer_name = "Ram"
product_name = "Mobile"
quantity = 2
price = 25000

sentance="Customer name is %s ,ordered %s that quantity is %d and is price %.2f each. " % (customer_name,product_name,quantity,price)
print("Original Sentance:",sentance)
print("Upper Case:",sentance.upper())
print("lower case:",sentance.lower())
print("Find a price in sentance:",sentance.find("price"))
print("replace mobile to computer:",sentance.replace("Mobile","computer"))
print("count:",sentance.count("a"))
print("split:",sentance.split(" "))