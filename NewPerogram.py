#dictionaries
marks = {}

x = int(input("Enter Phys marks : "))
marks.update({"Phys" : x})

x = int(input("Enter Chem marks : "))
marks.update({"Chem" : x})

x = int(input("Enter Math marks : "))
marks.update({"Math" : x})

print(marks)

#Sets
Grade = set()

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

Grade.add((1,2,3,4))
Grade.add((3,4,5,6))

print(Grade)

print(Grade.union(set2))
print(Grade.intersection(set2))

#While loops
i = 1

while i <= 100:
    print(i)
    i += 1

print("End Loop")

i = 100

while i >= 1:
    print(i)
    i -= 1 

print("End")

# qs3
i = 1  # n = int(input("enter number : "))
while i <= 10:
    print(3 * i)
    i += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(nums):
    print(nums[i])
    i += 1

movies = ["dark", "got", "chernobyl", "p&p", "breaking bad"]
j = 0     #traverse
while j < len(movies):
    print(movies[j])
    j += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49

j = 0
while j < len(nums):
    if(nums[j] == x):
        print("found at idx", j)
    j += 1