# # For loops
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print("")

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Zain"))

#Lambda (anonymous) function
square = lambda y: y * y
print(square(7))

# Parameters & Arguments
def greet(name):
    return f"Hello, {name}"

print(greet("My lady"))

#*args
def add_all(*numbers):
    return sum(numbers)

print(add_all(2, 4, 6, 8))

# #**kwargs
# def profile(**info):
#     return info


def shout(text):
    return text.upper()

# print(shout("mohd zain uddin"))

def shout(text):
    return text.upper()

def greet(func):
    return func("hello")

print(greet(shout)) #nope

#Write a function to check if a number is even or odd.
def check_odd_even(numbers):
    if numbers % 2 == 0:
        return f"{numbers} is Even"
    else:
        return f"{numbers} is Odd"
    
print(check_odd_even(20))
print(check_odd_even(13))

#Create a function that returns the largest of three numbers.
def find_largest(a, b, c):
    if a >= b and a >= c:
        return f"{a} is the largest"
    elif b >= a and b >= c:
        return f"{b} is the largest"
    else:
        return f"{c} is the largest"
    
print(find_largest(10, 12, 9))

#Through built-in functions:
def find_largest(a, b, c):
    return f"{max(a, b, c)} is the largest"
print(find_largest(10, 12, 9))

def find_largest(a, b, c):
    return f"{min(a, b, c)} is the smallest"
print(find_largest(10, 12, 9))