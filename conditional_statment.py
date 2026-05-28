opp = input("enter the vowels:  ")
vowel = "aeiouAEIOU"
if opp in vowel:
    print(f"{opp} is a vowle") 
else:
    print("enter only  vowel")


age = int(input("enter the age:  "))
if age >= 12:
    print("child")
elif age >= 17:
    print("teenager")
elif age >= 18:
    print("adult")
elif age >= 50:
    print("senior")
else:
    print("enter tha valued age")

num = int(input("enter the number:  "))
if num < 0:
    print("nagative")
elif num > 0:
    print("postive")
else:
    print("zero")
num1 = float(input("enter the number: "))
operator = input("enter the operator (+,-,/,*) ")
num2 = int(input("enter the number: "))
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    if num2 == 0:
        print("cannot divide by zero")
    else:
        print("result",num1/num2)
else:
    print("enter the valued operator")
x = 8
print("even")if x % 2 ==0 else print("minor")


    
