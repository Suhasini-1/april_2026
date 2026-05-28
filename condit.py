# # if condition and else

# User_Name=input("Enter User name:")
# Password=input("Enter password: ")
# if User_Name=="vamsi" and Password=="rules":
#     print(f"login succefull ")
#     print(f"welcome to bofa bank")
#     print(f"balance amount is {1000}")
# else:
#     print(f"invalide login information and only 3 attemts a day")    


# IF-elife-else condition

# Student_marks = int(input("enter the marks: "))
# if Student_marks >100 or Student_marks < 0:
#     print(f"please enter between 0 to 100")
# elif Student_marks >=90:
#     print(f"Grade A")
# elif Student_marks >=80:
#     print(f"Grade B")
# elif Student_marks>=70:
#     print(f"grade c")      
# elif Student_marks>=60:
#     print(f"grade D")
# else:
#     print(f"your failed please attend for suppley exams")   

#nested if conidtion


User_Name=input("Enter User name:")
Password=input("Enter password: ")
if User_Name=="vamsi":
    if Password=="rules":
        print(f"login succefull ")
        print(f"welcome to bofa bank")
        print(f"balance amount is {1000}")
    else:
         print(f"invalide password")
    
else:
    print(f"invalid user name")  
