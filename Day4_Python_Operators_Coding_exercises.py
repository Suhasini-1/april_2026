
#arithmetic operators
#addition
# num_1 = 12
# num_2 = 16
# result = num_1 + num_2
# print(result)

#subtraction -
# num_1 = 12
# num_2 = 16
# result = num_1 - num_2
# print(result)

#multiply *
# num_1 = 12
# num_2 = 16
# result = num_1 * num_2
# print(result)
#div /
# num_1 = 34
# num_2 = 16
# result = num_1 / num_2
# print(result)
#expo **
# num_1 = 3
# num_2 = 2
# result = num_1 ** num_2
# print(result)
#floor_div //
# num_1 = 3
# num_2 = 2
# result = num_1 // num_2
# print(result)
#mod %
# num_1 = 3
# num_2 = 2
# result = num_1 %  num_2
# print(result)

# a = 10
# b = 3

# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponentiation = a ** b
# print(addition, subtraction, multiplication, division, remainder,floor_division,exponentiation)

#assignment operators

# num_1 = 20
# num_1 %= 5  # tried all assignement operators
# print(num_1)

# Comparison operators

# prod_cost = 10
# prod_cost_2 = 10
# print(prod_cost <= prod_cost_2) # tried all comparison operatos

#logical operators
# user_name = "naren"
# pass_word = "naren4317"
# print ( user_name == "naren" and pass_word == "naren4317")

# user_name = input("enter the username: ")
# pass_word = input("enter the password: ")
# if (user_name == "naren" and pass_word == "naren4317"):
#     print(f"login succesfull,welcome {user_name}")
# else:
#     print("invalid username or password")    

# sample = True
# print(not sample)
#identity operators
# a = 1000
# b = 1000
# print(id(a))
# print(a)
# print(id(b))
# print(b)
# print(a is b)
# print(a is not b)
# a = 1000 ** 1000
# b = 1000 ** 1000
# print(id(a))
# print(a)
# print(id(b))
# print(b)
# print(a is b)
# print(a is not b)

#membership operator

# prod_data = ["vivo","oppo","samsung","nokia","apple"]
# print( "oppo" not in prod_data)

# F string in discount calculation

# prod_price = 1000
# discount = 10 #in percentage
# discount_amount = prod_price * (discount/100)
# prod_price_final = prod_price - discount_amount
# print(prod_price_final)
# print(f"the actual product price is {prod_price},the discount is {discount}%, after discount final price of the product is {prod_price_final}")

#coding exercise
#1.area of rect

# length = int(input("please enter the value of length : "))
# width = int(input("please enter the value of width : "))
# area = length * width
# print(area)

# 2.incr and decr of a variable
# num_1 = 6
# num_2 = 8
# num_1 += 2
# num_2 -= 2
# print( num_1,num_2)

# 3.celsius to foreignheit

# temp_value_c = int(input("enter the value of temp in celsius: "))
# temp_value_f = (temp_value_c * (9/5))+32
# print(f"the temperatue value in foreinheit {temp_value_f}")

# 4.simple intrest

# prin_amount = int(input("the prin amount is:"))
# rate = int(input("the rate of intrest per year is:"))
# time = int(input("the time period in years is:"))
# SI = (prin_amount * rate * time )/100
# prin_amount += SI
# print(SI)
# print(prin_amount)

# 5. concatinate two strings

# first_name = input("enter the text:")
# sur_name = input("enter the text:")
# full_name = first_name + " " + sur_name
# print(full_name)

# 6. km to miles

distance_km = int(input("enter the distance in km:"))
distnce_mile = distance_km * 0.62
print(distnce_mile)



