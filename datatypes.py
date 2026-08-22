"""Data types shows how your data be recognised by m/c , it should be integers, strings ,boolen , float etc."""

a = 13
b = 14.12
c = "Alice"
d =  True
e = 2 + 3j
f =[10,20,30]
g= (10, 20, 30)
h = 'A'

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(e.real)
print(e.imag)
print(type(f))
print(type(g))
print(type(h))


print(ord(h)) #print(ord(a)) is used to find the Unicode (ASCII for basic characters) value of a character.
total = a +b
print(total)
