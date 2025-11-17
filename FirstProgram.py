#Lists
list = ["Game of Thrones", "Interstellar", "The Dark Night"]
print(list)

grade = ['c', 'd', 'a', 'a', 'b', 'b' 'a']
print(grade.sort())
print(grade )

movies = []

mov1 = input("Enter 1st movie : ")
mov2 = input("Enter 2nd movie : ")
mov3 = input("Enter 3rd movie : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#Dictionaries
dict = {
    "name" : "Zain Uddin",
    "surname" : "Mohammed",
    "age" : 21,
    "college" : "Osmania University"
}
print(dict)


#If conditional statements
Age = int(input("Enter your age : "))

if (Age >= 18):
    if(Age >=80):
        print("Cannot drive")
    else:
        print('Can drive')
else:
    print("Cannot drive")


#fibonacci
num = int(input("Enter the Number : "))

a, b = 0, 1

print(f'{a} {b}', end= ' ')

for i in range(num - 2):
    c = a + b
    print(c, end= ' ')

    a, b = b, c

#Q
a = 2
a += 2
b = a
print(a,b)