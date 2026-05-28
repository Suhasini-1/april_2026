#Vowel Checker:
#Write a Python program that takes a character as input and checks whether 
#it is a vowel or not. Use the 
#if-else statement.

#char=input("enter a charcter:")
#if char in "aeiouAEIOU":
#    print("vowel")
#else:
#    print("not a vowel")

#char=input("enter a charcter")
#print("vowel" if char in "AEIOUaeiou" else "not vowel")



#Age Group Classification
#Write a program that takes an age as input and classifies the person into 
#one of the following age groups:
#Child: 0-12 years
#Teenager: 13-17 years
#Adult: 18-64 years
#Senior: 65 years and older

#age=int(input("enter the person age"))
#if age<0 or age>100:
#    print("please enter age between 0 and 100")
#elif age>65:
#    print("senior citizen")
#elif age>17:
#    print("Adult")
#elif age>12:
#    print("Teenager")
#elif age>0:
#    print("child")

# age=int(input("enter the person age:"))
# if age>=0 and age<=12:
#     print("child")
# elif age>=13 and age<=17:
#     print("Teenager")
# elif age>18 and age<=64:
#     print("Adult")
# elif age>=65:
#     print("senior citizen")
# else:
#     print("entered age is inavlid")

#Number Classifier:
# Write a program that takes an integer as input and classifies it as positive, 
# negative, or zero. Use the 
# if-elif-else statement.

# number=int(input("enter a value:"))
# if number>0:
#     print(" the given nunber is positive")
# elif number<0:
#     print(" the given number is negative")
# else:
#     print("0")

#  Leap Year Checker:
# Create a program that checks whether a given year is a leap year or not. A 
# leap year is divisible by 4, but not by 100 unless it is divisible by 400

# year=int(input("enter a year:"))
# if (year%4==0 and year%100!=0)or (year%400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
    
# Calculator:
# Build a simple calculator program that takes two numbers and an operator 
# (+, -, *, /) as input and performs the corresponding operation

# num_1=int(input("enter first number:"))
# operator=input("enter operator:")
# num_2=int(input("enter second number:"))
# if operator=="+":
#     print(num_1+num_2)
# elif operator=="-":
#     print(num_1-num_2)
# elif operator=="*":
#     print(num_1*num_2)
# elif operator=="/":
#     if num_2!=0:
#         print(num_1/num_2)
#     else:
#         print("cannot divide by zero")
# else:
#     print("invalid operator")

#short hand if 
# x=8
# print("even" if x%2==0 else "odd")


# #discount calculator
# original_price=int(input("enter the original price:"))
# discount=int(input("enter the discount:"))
# discount_price=original_price*(discount)/100
# final_price= original_price - discount_price
# print(f"discount_price:{discount_price} \nfinal_price of product:{final_price}")

#BMI Calculator:

weight=float(input("enter weight in Kg:"))
height=float(input("enter height in meters"))
BMI=weight/height**2
print(f"BMI is {BMI}")
