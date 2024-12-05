import random

print("Welcome to PassGen")
length = input("Enter the length of password you want, Let it be above 8 digits: \n")

#All list based on Categories
alpha_cap = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alpha_sma = list('abcdefghijklmnopqrstuvwxyz')
symbols = list("!@#$%^&*()")
number = list("1234567890")

#Combine all the list to make it as one
combination_of_list = alpha_cap + alpha_sma + symbols

#Checking the Correctness of Input
if length in combination_of_list:
    print("Invalid Input")

elif int(length) < 8:
    print("Password Length is too Small")
    
else:
    length = int(length)
    #Randomize the list based on the length the User wants
    password = random.choices(combination_of_list + number, k=length)

    #Change the list into a string
    password = "".join(password)

    print("\n")
    print(password)

