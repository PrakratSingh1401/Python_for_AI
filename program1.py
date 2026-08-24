#WAP to input a number and print its cube.

num = float(input("Enter a number"))
cube = num*num*num
print("Cube:",cube)


#WAP to input a number form user and print its square root.

num = float(input("Enter a number:"))
sqroot= num**0.5
print("Square root of given number",num," is :",sqroot)

# using standard library math

import math
num = int(input("Enter a number:"))
sqroot = math.sqrt(num)
print(sqroot)


#WAP that inputs an integer in range 0-999 and the print if the integer entered is a 1/2/3 digit number.

num = int(input("Enter a number in range 0-999:"))

if num<0:
  print("Wrong input is entered! Please enter number in a given range ")
elif num<10:
  print("The given number",num,"is 1 digit number.")
elif num<100:
  print("The given number",num,"is 2 digit number.")
elif num<1000:
  print("The given number",num,"is 3 digit number.")
else:
  print("Number is greater than the given range 0-999.")
