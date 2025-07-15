# # print("Hello")
#
# # Applicant_name = input("Enter your applicant name : ")
# # jobAppliedfor = input("Job applied for : ")
# # expectedSalary = int(input("Enter expected salary : "))
# #
# # print("Applicant name is " , Applicant_name , "job applied For" , jobAppliedfor , "Expected Salary" , expectedSalary)
# #
# #
# # print(f"Applicant name is{Applicant_name}\n job applied For {jobAppliedfor} \n Expected Salary {expectedSalary}")
#
# print("My Halwa Pori Shop")
#
# noOfpori = int(input("How many poories do you want : "))
# noOfsalan =  int(input("How many Cholay do you want : "))
# noOfaluu = int(input("How many Allu Ki Plate do you want : "))
# noOfhalwa = int(input("How many Halwa Plate do you want : "))
#
# singlePori = 50
# singleSalan = 80
# singleAlluu = 70
# singleHalwa = 100
#
# totalPori = noOfpori * singlePori
# totalSalan = noOfsalan * singleSalan
# totalAlluu = noOfaluu * singleAlluu
# totalHalwa = noOfhalwa * singleHalwa
#
# print(f"Your Total Pori Is {totalPori}\nYour Total Cholay is {totalSalan} \nYour Total Allu ka Salan is {totalAlluu} \nYour Total Halwa plate is {totalHalwa}")
#
# total = totalPori + totalSalan + totalAlluu + totalHalwa
# print(f"\nYour Total Amount without tax {total}")
# payment = input("Do you want yo pay through card : ")
# if payment ==  "yes":
#     tax = total * 0.08
# else:
#     tax = 0
# subTotal = total + tax
# discount = subTotal * 0.25
# grandTotal = subTotal - discount
#
#
# print(f"Your Total Amount with tax {subTotal}")
#
#
#
#
# print(f"Your Grand Amount After 25% Discount Is {grandTotal} PKR")
#
# import random
#
# print("---------- Number Guessing Game ---------")
#
# print("You Have Total 3 Lives")
#
# auto_generated_no = random.randint(1,20)
# lives = 3
#
# while lives > 0:
#
#     user_guess = int(input("Enter your guess between 1 - 20 : "))
#     if user_guess == auto_generated_no:
#         print("Congratulation you are gusessed")
#         break
#     else:lives -= 1
#
#     if user_guess > auto_generated_no:
#         print("Please low number")
#     else:
#         print("Please guess high number")
#
#     if lives > 0:
#         print(f"You have {lives} lives left")
#
#     else:
#         print("All lives have been finished")
from math import trunc

import pandas

# import string
# import random
# import sys
#
# import pyperclip
#
# print("********** Random Password Generator **********")
#
# uppercase_length = int(input("How many upper latters do you want ? "))
# if uppercase_length <= 0 or uppercase_length > 10:
#     print("Atleast 1 uppercase is required and maximum 10")
#     sys.exit()
# lowercase_length = int(input("How many lower latters do you want ? "))
# if lowercase_length <= 0 or lowercase_length > 10:
#     print("Atleast 1 lowerccase is required and maximum 10")
#     sys.exit()
# digit_length = int(input("How many numbers do you want ? "))
# if digit_length <= 0 or digit_length > 10:
#     print("Atleast 1 number is required and maximum 10")
#     sys.exit()
# special_character_length = int(input("How many special charactor do you want ? "))
# if special_character_length <= 0 or special_character_length > 10:
#     print("Atleast 1 special charactor is required and maximum 10")
#     sys.exit()
#
# upper_list, lower_list, number_list, sp_list = [] , [] , [] , []
# uppercase = string.ascii_uppercase
# lowercase = string.ascii_lowercase
# numbers = string.digits
# special_character = ["!","@","#","$","%","^","&","*","(",")"]
#
# # Bari abcd
# for i in range(uppercase_length):
#     upper_list.append(random.choice(uppercase))
#
# for i in range(lowercase_length):
#     lower_list.append(random.choice(lowercase))
#
# for i in range(digit_length):
#     number_list.append(random.choice(numbers))
#
# for i in range(special_character_length):
#     sp_list.append(random.choice(special_character))
#
# PasswordList = upper_list + lower_list + sp_list + number_list
#
# # Bari abcd
#
# random.shuffle(PasswordList)
# random.shuffle(PasswordList)
# random.shuffle(PasswordList)
#
# # Password list to string
# pswd_string = "".join(PasswordList)
# print(pswd_string)
#
# choice = input("Do you want to copy this password ?")
# if choice.lower() == "yes":
#     pyperclip.copy(pswd_string)
#     print("Password has been copied")




# list
#
# dishes_list = ["Biryani" , "Korma" , "Karhai" , "Achar Gosht" , "Pulao" , "Nihari" , "Paya" , "Kaleji" , "Chinese Rice"]
#
# print(dishes_list)
# print(f"Print index 1 : {dishes_list[1]}")
# print(f"Print index 2:5 : {dishes_list[2:5]}")
# print(f"Print 2nd last dish{dishes_list[-2]}")
#
# dishes_list.append("Korma")
# print(f"Add korma end of list {dishes_list}")
#
# dishes_list.insert(3,"Paye")
# print(f"Add Paye index 4 of list {dishes_list}")
#
# sweets_list = ["Kheer" , "Sheer khurma" , "Lab-e-sheren"]
# dishes_list.extend(sweets_list)
# print(f"Add sweets dishes end of list {dishes_list}")
#
# print(f"Dishes length {len(dishes_list)}")
#
# dishes_list.sort()
# print(f"Print assending order of list {dishes_list}")
#
# dishes_list.sort(reverse=True)
# print(f"Print desending order of list {dishes_list}")
#
# dishes_list.remove("Nihari")
# print(f"Remove Nihari in list {dishes_list}")
#
# dishes_list.pop()
# print(f"Remove last in list {dishes_list}")
#
# dishes_list.pop()
# print(f"Remove last in list {dishes_list}")
#
# for i in dishes_list:
#     print(i)
#
# print(f"print all dishes using loop {dishes_list}")



# dictionary

# my_info = {
#     "Name" : "Ikrama",
#     "Gender" : "Male",
#     "Age" : 10,
#     "Address" : "Karachi",
#     "Weight" : 20,
#     "Favt Dish" : "Biryani"
# }
#
# print(my_info)
#
# my_info ["Course"] = "Python"
#
# print(my_info.keys())
#
# del my_info ["Weight"]
# print(f"After delete weight{my_info}")
#



# pip install pandas

# import pandas
# dummy_data = {
#     "Name": ["Ali", "Sara", "Bilal", "Zoya", "Usman", "Areeba", "Hamza", "Nimra", "Tahir", "Hina"],
#     "Language": ["Python", "JavaScript", "C++", "Java", "Python", "TypeScript", "Go", "Ruby", "C#", "Rust"],
#     "Experience (Years)": [2, 3, 1, 4, 5, 2, 3, 4, 2, 1],
#     "GitHub Profile": [
#         "github.com/ali-dev",
#         "github.com/sara-js",
#         "github.com/bilal-cpp",
#         "github.com/zoya-java",
#         "github.com/usman-py",
#         "github.com/areeba-ts",
#         "github.com/hamza-go",
#         "github.com/nimra-rb",
#         "github.com/tahir-cs",
#         "github.com/hina-rust"
#     ],
#     "Favorite Framework": [
#         "Django", "React", "Qt", "Spring", "Flask",
#         "Angular", "Gin", "Rails", ".NET", "Rocket"
#     ]
# }
#
# print(dummy_data)
#
# dframe = pandas.DataFrame(dummy_data)
#
# print(dframe)
#


