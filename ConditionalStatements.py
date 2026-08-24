#if-statement

age = int(input("ENter age:"))
if age>=18:
  print("Adult",age)

#if-else statement

age =int(input("enter age:"))

if age<18:
  print("Minor:",age)
else:
  print("Adult:",age)

#elif statements
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


#Nested if-else statement

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")