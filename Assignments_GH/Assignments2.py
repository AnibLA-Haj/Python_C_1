
"""
Assignments 2
"""
#1
nr1 = int(input("Enter the first number: "))
nr2 = int(input("Enter the second number: "))

# not necesarry
plus = nr1 + nr2
minus = nr1 - nr2
mul = nr1 * nr2
div = nr1 / nr2
divi = nr1 // nr2
rem = nr1 % nr2

print(f"{nr1} + {nr2} = ", nr1 + nr2)
print(f"{nr1} - {nr2} = ", nr1 - nr2)
print(f"{nr1} * {nr2} = ", nr1 * nr2)
print(f"{nr1} / {nr2} = ", nr1 / nr2)
print(f"{nr1} // {nr2} = ", nr1 // nr2)
print(f"{nr1} % {nr2} = ", nr1 % nr2)

#2
name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("Enter a number: "))

print(f"Hello {name}, your age is {age}, and the number you typed is {number}")

#3
nr1 = int(input("Enter the first number: "))
nr2 = int(input("Enter the second number: "))
nr3 = int(input("Enter the third number: "))

ls = [nr1, nr2, nr3]
print(ls[0], ls[-1])

#4

l1 = input("Enter the first element: ")
l2 = input("Enter the second element: ")

lii1 =[l1]
lii2 = [l2]

print(f"{lii1} > {lii2}", lii1 > lii2)
print(f"{lii1} < {lii2}", lii1 < lii2)
print(f"{lii1} >= {lii2}", lii1 >= lii2)
print(f"{lii1} <= {lii2}", lii1 <= lii2)
print(f"{lii1} == {lii2}", lii1 == lii2)
print(f"{lii1} != {lii2}", lii1 != lii2)

#5

nr = int(input("Enter a number: "))
print(f"{nr} > 10", nr > 10)
even = nr % 2 ==0
print("[False = Odd], [True = Even]: ", even)

#6
width = int(input("Enter the width of rectangle: "))
height = int(input("Enter the height of rectangle: "))

heig = int(input("Enter the height of triangle: "))
base = int(input("Enter the base of the triangle: "))
#rectangle
area = width * height
perimeter = 2 * (width + height)
#triangle
area = (base * height) / 2
area = width * height
per = 2 * (width + height)
print("The area of rectangle is: ", area)
print("The perimeter of rectangle is: ", per)

areat = (base * heig) / 2
print("The area of triangle is: ", areat)

#7
nr = input("Enter a number: ")

ff = round(float(nr), 2)
ex = int(input("Enter the exponent: "))
print(ff)
print(round(ff**ex), 2)

#8

ls = [1,2,3,4]
print(ls)
user = int(input("Enter the index:"))

print(f"In the index {user} is the element: ",ls[user])


#9

nr1 = int(input("Enter the first number: "))
nr2 = int(input("Enter the second number: "))
nr3 = int(input("Enter the third number: "))
nr4 = int(input("Enter the fourth number: "))
nr5 = int(input("Enter the fifth number: "))

li = [nr1, nr2, nr3, nr4, nr5]
print(li)
sum = sum(li)
print("The sum of the list is: ",sum)
print("The first element of the list is: ", li[0])
rem = li[-1] % 2
print("The remiader of the last element when divided by two: ", rem)
