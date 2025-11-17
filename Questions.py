# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# #Multiplication table ------------------------------
# num = int(input("Enter your number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# for i in range(1, 4):         # Outer loop
#     for j in range(1, 4):     # Inner loop
#         print(f"i={i}, j={j}")

# rows = 5

# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# def add(a, b):
#     return a + b

# print(add(2, 3))

# def p(n = 1):
#     if n > 100:
#         return
#     print(n)
#     p(n + 1)
# p()

# name = 'Zain'

# for i in name:
#     print(name)

# name = 'World'
# line = '-'

# # for i in name:
# #     line = line + i
# #     print(line)

# for i in name:
#     print(line)
#     line = line + i


# name = 'World'
# line = ''

# line = '+' + name + '+'
# spaces = ''

# for i in name:
#     spaces += ' '
    
# print(line)
# for j in name:
#     print(j + spaces + j)
# print(line)

# for i in range(2, 51):
#     print(i)

# import calendar

# yy = 2025
# mm = 10

# print(calendar.month(yy,mm))

# for i in range(1, 6):
#     for j in range(i, i*10+1, i):
#         print(j, end=" ")
#     print()

# for i in range(1, 3):
#     j = 1
#     while j < 3:
#         print(i, j)
#         j = j + 1
#     print("GFG")

# x = 0
# while (x < 100):
#     x += 2
# print(x)

# d = {0, 1, 2}
# for i in d:
#     print(i)

# Ture = False
# while True:
#     print(True)
#     break

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#             var += 1
#         else:
#             var += 1
# print(var)

# for i in range(10, 14):
#     for j in range(2, i):
#         if i % j == 1:
#             print(i)
#             break

# for i in range(int(2.0)):
#     print(i)

# word = "Geeks"
# result = ""

# for i in range(len(word)):
#     # Add first character always OR add if not same as previous one
#     if i == 0 or word[i] != word[i-1]:
#         result += word[i]

# print(result)   # Output: Ges

# def remove_consecutive_duplicates(s):
#     result = s[0]   # start with first character
#     for i in range(1, len(s)):
#         if s[i] != s[i-1]:   # add only if different from previous
#             result += s[i]
#     return result

# # Example
# word = "Geeks"
# print(remove_consecutive_duplicates(word))  # Output: Ges



# # Function to print x in decreasing order
# def utility(x):
#     x = 0
#     while x <+ 3:
#         print(x)
#         x += 1

# print(utility(3))

# x = 3
# while x >= 0:
#     print(x, end=" ")
#     x -= 1

# def utility(x):
#     while x >= 0:
#         print(x, end=" ")
#         x -= 1

# x = 3
# utility(x)

# print("G" in "GeeksforGeeks")

# print(5 % 20)

# s = 'gfg'
# print(not ("g" or "") not in s)

# print(1/1)

# print(1 // 2 * 3)

# x = 1
# y = 2
# z = x
# x = y
# y = z
# print(x, y)

# x = int(input())
# y = int(input())

# x = x // y
# y = y // x

# print(y)

# x = int(input())
# y = int(input())

# x = x % y
# x = x % y
# y = y % x

# print(y)

# z = y = x = 1
# print(x, y, z, sep='*')


# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)

# 04-10-2025
#--------------
# def hellofunction():
#     print("Hello")

# # hellofunction()

# def return_value(n):
#     return n * n

# # print(return_value(2))

# # def sayhello():
# #     print("Hello")   ----------Infinite result----------
# # #     sayhello()

# # # sayhello()

# def display(b, n):
#   while n > 0:
#     print(b,end="")
#     n=n-1
# # display('z',3)

# print(ord("a"))
# print(ord("Z"))
# print(chr(122))

# str = "I'am \"Zain\""
# print(str)

# s1 = "ZainisZain"
# s2 = "Zain"
# #index,.........r.index from the last
# print(s1.index(s2, 1))

# s = "GeeksforGeeks Python Course"
# print(s.startswith("Geeks"))
# print(s.startswith("Geeks", 8, len(s)))

# s1 = "geeks for geeks"
# print(s1.split())

# l = ["geeksforgeeks", "python", "course"]
# print(type(" ".join(l)))  
# print(", ".join(l))

# print(type(l))

# print("abcd"[2])

# # example = " "
# # example[3] = 's'
# # print(example)

# print(max("geekforgeeks"))    #max returns the character which has higher ascii value

# # print("GFG" +1+2+3)
# print('geeksforgeeks'.lstrip('geeks'))

# lis = [1, 2, 2, 3, 4, 3, 5]
# print(lis)
# lis.pop(2)
# print(lis)
# lis.pop(-1)
# print(lis)

n = 10
for i in range(n):
    print("*" * i)