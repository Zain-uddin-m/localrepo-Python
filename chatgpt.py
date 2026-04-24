# colour = "Grey"
# number = 22
# status = "I like coding"

# print(type(colour))
# print(type(number))
# print(type(status))

# name = input("What is your name? ")
# print("Hello", name)

# age = input("Enter you age: ")
# age = int(age)
# print("My age is", age)
# print("I we'll be", age + 1, "next year")
# print(type(age))

# name1 = input("What is your name?")
# print("My name is: ", name1)
# dob = int(input("Enter your birth year: "))
# age1 = 2025 - dob
# print("My date of birth is ", dob)
# print("My current age is ", age1)

# x = "10"
# x += "5"  #x = x + 5
# result = int(x) // 3
# print(result)

# a = float(input("Enter first number: "))
# b = float(input("Enter second nummber: "))

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# remainder = num1 % num2
# power = num1 ** num2

# print("Remainder when", num1, "is divided by", num2, ":", remainder)
# print(num1, "raised to the power of", num2, ":", power)

# DAY 7
# count = 1
# while count <= 5:
#     print('Count: ',count)
#     count += 1

# for i in range(1, 6):
#     print('Number:', i)

# for ch in "Python":
#     print(ch)

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# for i in range(1, 21):            
#     if i == 15:
#         break
#     if i % 3 == 0:
#         continue
#     print(i)
#                  # same
# i = 1
# while i <= 20:
#     if i == 15:
#         break
#     if i % 3 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# for i in range(1, 6):
#     print(i)
# else:
#     print("Loop completed successfully!")


# for i in range(1, 4):         # Outer loop
#     for j in range(1, 4):     # Inner loop
#         print(f"i={i}, j={j}")

#Multiplication table:
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# x = 5
# for i in range(1, 11):
#     print(x * i)

# rows = 5
# for i in range(1, rows + 1):
#     print("*" * i)

# rows = 10
# for j in range(1, rows + 1):
#     print("*" * j)

# import math

# for num in range(2, 51):
#     is_prime = True
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# Number of rows
# rows = 5

# for i in range(1, rows + 1):       # Outer loop → rows
#     for j in range(1, i + 1):       # Inner loop → numbers in each row
#         print(j, end="")            # Print numbers on the same line
#     print()                         # Move to next line after each row

# def greet():
#     print("Hello, welcome to Python classes")

# greet()

# Functions with parameters -----
# def greet(name):
#     print("Hello", name)

# greet("Zain")
# greet("Mohd")
# greet("Ali")

# def add(a, b):
#     return a + b

# result = add(5, 3)
# print("Sum :", result)

# print("Sum :", add(5, 3))

#Function with default parameters ------
# def greet(name = "Guest"):
#     print("Hello", name)

# greet()
# greet("Zain")

# def check_even_odd(nums):
#     if nums % 2 == 0:
#         print(nums, "is even")
#     else:
#         print(nums, "is odd")

# num = int(input("Enter your number: "))
# check_even_odd(num)

# def largest_of_three(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
    
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2nd number: "))
# num3 = float(input("Enter 3rd number: "))

# print("The largest of three number is", largest_of_three(num1, num2, num3))

# 11/09/2025
# def add(a, b):    # Positional arguments ------
#     print(a + b)

# add(5, 3)   # a=5, b=3

# # Keyword arguments ----
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Zain", 21)
# greet(age= 21, name= "Zayn")

# # Variable lenght arguments -----
# # *args -- aloows multiple postional arguments (tuple) 
# def add(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     print("Sum =", total)

# add(2, 3, 4, 5)

# # **kwargs -- allows multiple keyword arguments (dictionary)
# def show_details(**info):
#     for key, value in info.items():
#         print(key, ":", value)

# show_details(name = "Zain", age = 21, country = "India")

#Practice
#----------
# def multiply_all(*nums):
#     total = 1
#     for n in nums:
#         total *= n
#     print("Multiply =", total)

# multiply_all(2, 3, 4, 5)

# #2
# def multiply_all(*nums):
#     result = 1
#     for n in nums:
#         result *= n
#     return result

# # Example usage
# print(multiply_all(2, 3, 4))        # 24
# print(multiply_all(5, 10))          # 50
# print(multiply_all(1, 2, 3, 4, 5))  # 120

# #**kwargs -------------
# def student_info(**details):
#     for key, value in details.items():
#         print(key, ":", value)

# student_info(name = "Zain", age = 21.6, grade = 9.03)

# def student_info(**details):
#     print("Student Information:")
#     print("Name :", details.get("name", "Not Provided"))
#     print("Age  :", details.get("age", "Not Provided"))
#     print("Grade:", details.get("grade", "Not Provided"))

# # Example usage
# student_info(name="Alice", age=20, grade="A")
# student_info(name="Bob", grade="B")  # age missing on purpose

def student_info(**details):
    print("Student Information:")
    for key, value in details.items():
        print(f"{key.capitalize()} : {value}")

# Example usage
# student_info(name="Alice", age=20, grade="A", school="ABC High School", city="New York")
# print()
# student_info(name="Bob", grade="B", subject="Math", hobby="Football")