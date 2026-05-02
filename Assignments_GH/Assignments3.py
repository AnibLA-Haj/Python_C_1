"""assignments"""

#1
nr = int(input("Enter a number: "))
if nr != 7:
     print("number entered")
    
#2
nr = int(input("Enter a number: "))
if nr % 2 == 0:
    print("Multiple of 2")

#3
nr = int(input("Enter a number: "))
if nr > -10 and nr < 10:
    print("valid")
    
#4
nr = int(input("Enter a number: "))
if nr % 2 != 0:
    print("Odd")

nr = int(input("Enter a number: "))
if nr % 2 ==0:
    print("Even")

#5
nr1 = int(input("Enter a number: "))
nr2 = int(input("Enter a number: "))

if nr1 > nr2:
    print("First is bigger")
else:
    print("Second is bigger")
    
#6
nr1 = int(input("Enter a number: "))
if nr1 >= 0 and nr1 <= 5:
     print("It is in range (0-5)")
elif nr1 >= 6 and nr1 <= 10:
     print("It is in range (6-10)")
else:
     print("other")
    
#7
nr1 = int(input("Enter a number: "))
nr2 = int(input("Enter a number: "))

if nr1 % nr2 == 0:
    print("It is divisible")
else:
    print("It is not divisible")
    
#8
nr1 = int(input("Enter a number: "))
if 1 < nr1 < 9:
    print("within range")
else:
    print("outside")

#9
nr1 = int(input("Enter a number: "))
nr2 = int(input("Enter a number: "))
nr3 = int(input("Enter a number: "))

if nr1 < nr2 and nr1 < nr3:
    print(f"{nr1} is smaller")
else:
    print(f"{nr1} is not the smallest")

#10
nr1 = int(input("Enter a number: "))

if nr1 > 5:
     if nr1 > 10:
        print(f"{nr1} is greater than 5 and 10")

#11

nr1 = int(input("Enter a number: "))

if nr1 > 8:
     print("bigger than 8")
else:
    if nr1 < 8 or nr1 ==8:
        print("blah")

#12
nr1 = int(input("Enter a number: "))
if nr1 >= -5 and nr1 <= 5:
    print("interval")
else:
    print("outside")

#13
nr1 = int(input("Enter a number: "))
nr2 = int(input("Enter a number: "))

if nr1 % 2 != 0:
    print(nr1 + nr2)
else:
    print(nr1 * nr2)

#14

x = int(input("Enter a number: "))

if -2 < x < 2:
    y = 2 * x
    print(y)
elif 5 <= x < 7:
    y = 3 * x - 1
    print(y)
else:
    y = 1 / x
    print(y)



























