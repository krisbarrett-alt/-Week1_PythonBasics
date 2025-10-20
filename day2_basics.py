#many variables to multiple variables
x, y, z = ("Orange", "Banana", "Cherry")
print(x,y,z)

#one value to multiple values
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection (list,tuple)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
#global vs. local variables
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#for global variable inside function use global keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
"""
#change value of global variable inside function using global keyword
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print ("Python is " + x)

x = 5
print(type(x))

"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))

for x in "banana":
    print(x)

txt = "The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present")

txt = "The best things in life are free"
print("expensive" not in txt) 

txt = "The best things in life are free"
if "expensive" not in txt:   
    print("No, 'expensive' is NOT present")

x = 'Welcome'
print(x[3])  

# var.upper(), var.lower(), var.strip(), var.replace(), var.split()

#concatenate

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#string format
"""
age = 36
#error bc not formatted
txt = "My name is John, I am" + age
"""
age = 36
txt = f"My name is John, I am {age}" 
print(txt)

#f string modifiers & placeholders

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print (txt)

txt = f"The price is {20 * 59} dollars"
print(txt)














