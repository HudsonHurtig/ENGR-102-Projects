import math

#making the while loop case true so it will run
user_input = -1

#this loop will run forever until user input is between 0 and 1
while(not(0<user_input<1)):
    #taking input
    user_input = float(input("please input a number between 0 and 1"))
    #printing error message
    if(not(0<user_input<1)):
        print("Error, please input number between 0 and 1")
    #newline
    print("\n")

#printing output
print(f"e raised to {user_input} is {math.exp(user_input)}")

