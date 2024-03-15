# primitative dataTypes
# 1. String
# 2. Boolean
# 3. float
# 4. Integer

print("Hello"[4])

print(type("Hello"))

# type conersition

num_char = len("What is your Name? \n")
new_num_char= str(num_char)
print("Your name has " + new_num_char + " characters")

# HW

input = (input("Enter the two digit Number  \n"))

frist_digit = int(input[0])
second_digit = int(input[1])

print(frist_digit + second_digit)
print(int(input[0]) + int(input[1]) )

# Mathematical operators

print(3+2) # Addition
print(3-2) # Subtraction
print(3*2) # Multipy
print(3/2) # Divide
print(3**2) # exponential

# Importance order
# PEDMAS () , ** , / , * , - , +

print(3 * 3 + 3/3 -3)
# 3 *3 and 3/3 as it has equal importance
#(9 + 1 -3) now add and minus as it has equal importance
# so the final value is 7

# Home Work 2
# BMI CALCULATOR
user_weight = (input("Please Enter Your Weight IN \"KGS\"? \n"))
user_height = (input("Please Enter your Height in Meters? \n"))

updated_user_weight = float(user_weight)
updated_user_height = float(user_height)
type(user_height)
print(type(updated_user_height))
bmi = updated_user_weight / updated_user_height **2
print(bmi)

# Number Manipulation
print(int(8/3))
print(round(2.3333))
print(round(2.5666))
print(type(4/2))
print(4/2)
score = 1
score +=1
height = 1.6
print(score)

# f-string - used to 
print(f"your score is {height}")
#HW
your_age = input("Enter your Age? ")
updated_age = int(your_age)
life_span = 90
remainig_age = life_span - updated_age
life_in_weeks = remainig_age * 52
print(f"You have {life_in_weeks} weeks left in your life")
print(12/3)

#HW
print("Welcome to the Tip Calculator😶‍🌫️")
total_bill = float(input("What was the total bill ? \n"))
tip_percentage = int(input("How much tip would you like to give? choose between 10,12,or 15? \n"))
split_by = int(input("how many people are you there? \n"))
tip_amount = total_bill * (tip_percentage/100)
final_amount = (total_bill + tip_amount) /2
print(f"Each person should pay {final_amount}$")

