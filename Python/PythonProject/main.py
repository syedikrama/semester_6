# print("Hello")

# Applicant_name = input("Enter your applicant name : ")
# jobAppliedfor = input("Job applied for : ")
# expectedSalary = int(input("Enter expected salary : "))
#
# print("Applicant name is " , Applicant_name , "job applied For" , jobAppliedfor , "Expected Salary" , expectedSalary)
#
#
# print(f"Applicant name is{Applicant_name}\n job applied For {jobAppliedfor} \n Expected Salary {expectedSalary}")

print("My Halwa Pori Shop")

noOfpori = int(input("How many poories do you want : "))
noOfsalan =  int(input("How many Cholay do you want : "))
noOfaluu = int(input("How many Allu Ki Plate do you want : "))
noOfhalwa = int(input("How many Halwa Plate do you want : "))

singlePori = 50
singleSalan = 80
singleAlluu = 70
singleHalwa = 100

totalPori = noOfpori * singlePori
totalSalan = noOfsalan * singleSalan
totalAlluu = noOfaluu * singleAlluu
totalHalwa = noOfhalwa * singleHalwa

print(f"Your Total Pori Is {totalPori}\nYour Total Cholay is {totalSalan} \nYour Total Allu ka Salan is {totalAlluu} \nYour Total Halwa plate is {totalHalwa}")

total = totalPori + totalSalan + totalAlluu + totalHalwa
print(f"\nYour Total Amount without tax {total}")
payment = input("Do you want yo pay through card : ")
if payment ==  "yes":
    tax = total * 0.08
else:
    tax = 0
subTotal = total + tax
discount = subTotal * 0.25
grandTotal = subTotal - discount


print(f"Your Total Amount with tax {subTotal}")




print(f"Your Grand Amount After 25% Discount Is {grandTotal} PKR")

