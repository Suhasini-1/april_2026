#Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement
# char=input("enter the vowels:")
# vowels=("aeiouAEIOU")
# if char in vowels:
#     print(f"vowels")
# else:
#     print(f"not vowels")

"""
Age Group Classification
Write a program that takes an age as input and classifies the person into one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older
"""
# age=int(input("enter age:"))
# if age>=0 and age<=12:
#    print("Child age is:",age)
# elif age >= 13 and age <= 17:
#    print("Teneger age is:",age)
# elif age>=18 and age<=64:
#    print("Adult age is:",age)
# elif age>=65:
#    print("senior age is:",age)
# else:
#    print("you entered wrong age info")


# age=int(input("enter age:"))
# name=input("enter your name:")
# if age>=0 and age<=12:
#    print(f"My name is{name} and my Child age is:",age)
# elif age >= 13 and age <= 17:
#    print(f"My name is {name} and my older daughter is teneger and her age is:",age)
# elif age>=18 and age<=64:
#    print(f"I'm an Adult and my age is:",age)
# elif age>=65:
#    print("My gradma is senior citizen and her age is:",age)
# else:
#    print("Invalid age")

#program that takes an integer as input and classifies it as positive, negative, or zero. Use the if-elif-else statement
# number=int(input("enter an integer value:"))
# if number>0:
#     print(f"The number is positive value:{number}")
# elif number < 0:
#     print(f"The number is Negative value:{number}")
# else:
#     print(f"Your value is 0")


#Create a program that checks whether a given year is a leap year or not. 
# A leap year is divisible by 4, but not by 100 unless it is divisible by 400
# leap_year=int(input("Enter the year:")) 
# if (leap_year%4==0 and leap_year%100!= 0) or leap_year%400==0:
#     print(f"{leap_year} is leap year")
# else:
#     print(f"{leap_year} is not leap year")


#Build a simple calculator program that takes two numbers and an operator (+, -, *, /) as input and performs 
# the corresponding operation.
# num_1=int(input("enter the value:"))
# num_2=int(input("enter the value:"))
# operator=input("enter the operator")
# if operator== "+":
#     print(num_1 + num_2)
# elif operator== "-":
#     print(num_1 - num_2)
# elif operator=="*":
#     print(num_1*num_2)
# elif operator== "/":
#     print(num_1 / num_2)


"""
Rewrite the following code using the short-hand 
if statement:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
"""
# x=8
# print(f"{x} number is even") if x%2 == 0 else print(f"number is odd")


#Create a program that calculates the final price after applying a discount. 
#The program should take the original price and the discount percentage as input.
# orginal_price=int(input("enter tshirt price is:"))
# discount=int(input("enetr discount price is:"))
# sale_price=orginal_price*discount/100
# total_price=orginal_price - sale_price
# print(total_price)


"""
Write a program that calculates the Body Mass Index (BMI) using the 
formula: BMI = weight (kg) / (height (m))^2. The program should take 
weight and height as input.
"""
weight = float(input("enter my weight is:"))
height = float(input("enter my height is:"))
bmi= weight/height**2
print(bmi)