a = 15
b = 4

# Arithmetic operators
print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)

#Comparision operators
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#bitwise operators
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#identity operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#membership operators
x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#Precedence and Associativity of Operators
#Operator precedence and associativity determine the priorities of the operator.

#Precedence Operators
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

#Associativity operator
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)   