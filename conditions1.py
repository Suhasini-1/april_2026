#checking vowels

#char=input("enter the value:")
#vowels="aeiouAEIOU"
#if char in vowels:
    #print(f"it is vowel")
#else:
    #print(f"it is not vowel")    

#age group calculation

#age = int(input("enter value"))
#if age>0 and age<=12:
    #print(f"child")
#elif age>=13 and age<=17:
    #print(f"teenager")
#elif age>=18 and age<=64:
    #print(f"adult")
#else:
    #print(f"senior")             


#age = int(input("enter value"))
#if age>0 or age<=12:
    #print(f"child")
#elif age>=13 or age<=17:    #this code is wrong
    #print(f"teenager")      #dont use or operator
#elif age>=18 or age<=64:
    #print(f"adult")
#else:
    #print(f"senior")                 

#number classifier

#number= int(input("enter value:"))
#if number > 0:
    #print(f"it is a positive number")
#elif number < 0:
    #print(f"it is a negative number")
#else:
    #print(f"it is zero")

#leap year

#year =  int(input("enter the year:"))
#if year%4==0:
    #print(f"it is a leap year")
#else:
    #print(f"it is a not leap year")    


#calculator

#num_1 = float(input("enter the value"))
#num_2 = float(input("enter the value"))
#operator = input("enter operator")            
#if operator== "+":
    #print(f" Addition is {num_1  + num_2}")
#elif operator == "-":
    #print(f" subtraction is {num_1  - num_2}")    
#elif operator == "*":
    #print(f" multiflication is {num_1  * num_2}")    
#elif operator  == "/":
    #print(f" division is {num_1 *  num_2}")    
#else:
    #print(f"enter valid operator")

#short hand
""" given
x =8
if x % 2 == 0: result = "Even"
  else:  result = "odd" """

#x = 8
#print(f"{x} is Even") if x % 2 == 0 else print(f" {x} is Odd")

#discount calculator

#original_price = float(input("actual price is:"))
#discount = float(input("discount percentage is:"))
#final_dicount = original_price * (discount/100 )
#original_price -= final_dicount
#print(f"discount is {discount}% final_discount is {final_dicount} final price is {original_price}")


#BMI calculator

weight = float(input("enter the value"))
height = float(input("enter value"))
BMI = weight / (height ** 2)
print(f"your BMI is {BMI}")