#takes user input in the form of a string which is wrapped in the int() function converting it to an interger

number = int(input("Enter a 5-digit integer:"))

#get 10000s digit

d1 = number // 10000

#get digits in the 1s 10s 100s and 1000s, only to take the value in the thousands

d2 =(number % 10000) // 1000

#get digits in the 1s 10s 100s, only to take the value in the hundreds

d3 =(number % 1000) // 100

#get digits in the 1s 10s, only to take the value in the tens

d4 =(number % 100) // 10

#get digits in the 1s

d5 =number % 10

# next line just nests the reverse formatting in the string print format 

print(f"12345 backwards is: {d5}{d4}{d3}{d2}{d1}")