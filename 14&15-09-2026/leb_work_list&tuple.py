
# Lab Work

# 16. Student Result System
# ● Store marks of 5 subjects in a list.
# ● Check each subject: Pass/Fail.
# ● Calculate total and percentage.
# ● If percentage ≥ 75 → Distinction
# ● If percentage ≥ 60 → First Class
# ● If percentage ≥ 50 → Second Class
# ● If percentage ≥ 40 → Pass
# ● Otherwise → Fail

marks=[89,98,77,54,34]
total=sum(marks)
per=total/len(marks)

for m in marks:
   if m>=35:
    print(m,"Pass")
else:
    print(m,"Fail")
    allpass=False

if allpass==False:
   print("fail in one or more subject")
elif per >= 75:
   print("Distinction")
elif per >= 60:
    print("First Class")
elif per >= 50:
   print("Second Class")
elif per >=40:
   print("Pass")
else:
   print("fail")

print("Total:",total)
print("Percentage:",per)



# 17. Shopping Cart
# ● Store products and prices in a list.
# ● Check whether the product is available.
# ● If price > ₹1000, apply 10% discount.
# ● Otherwise, no discount.
# ● Display final price.

product=["mobile","laptop","keybord"]
price=[15000,50000,800]
item=input("Enter a product name:")
if item in product:
   print("product is available.")
   ind=product.index(item)
   p=price[ind]
   if p>1000:
      print(f"Discount: 10% final price is {p-(p * 10/100)}")
   else:
      print(f"No Discount final price is {p}")

else:
   print("product is not available")


