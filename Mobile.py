nums = [1, 2, 3]
for i in nums:
    nums.append(i)
    if len(nums) > 6:
        break
print(nums)

for i in range(3):
    print(i)
    if i == 1:
        break
    else:
        continue

scale = int(input("Enter your number: "))

if scale > 0:
    print("Positive")
elif scale < 0:
    print("Negative")
else:
    print("Zero")

age1 = int(input("Enter your age: "))

if age1 >= 18:
    if age1 >= 60:
        print("You are a senior citizen")
    else:
        print("You are an adult")
else:
    print("Yuo are a minor")

x = 10
if x > 5: print("x is greater than 5")

x = 5
print("Positive") if x > 0 else print("Negative")


number = int(input("Enter your number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

#Generating a Calender
import calendar

yy = 2025
mm = 8

print(calendar.month(yy,mm))


# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("vivek468/superstore-dataset-final")

# print("Path to dataset files:", path)