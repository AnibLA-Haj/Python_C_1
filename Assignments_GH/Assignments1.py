"""
Assignments from easy to advanced

"""
#easy
# #1
print("Hello Python")

#2
print("David")

# #3
x = 5
print(5)

#4
name = "al"
age = 30
5
#we are printing name ad age var, in the same line
print(name, age)

#6
# '''What my code does here is printing the name 
# and age variable in the same line'''

#7
y = 2.4
print(y)
print(type(y))

#8
word = "Peace"
print(word)

#9
ls = [23, 32, 21]
print(ls[1])
'''
When we have a lot of elements and we want to rpint the middle element
we use len'''
middle = len(ls) // 2
print(ls[middle])  #middle is the index for the middle element

#10
mix = [1,3, 4, "232", "ewrw", 2.32]
print(mix[2])

#11
print("Index 0: ",mix[0])
print("Index 1: ", mix[1])

for i in range(2):
    print("Index", i, ":", mix[i])

#12
int = 12
f = float(int)
print(f)

#13

f = 12.2
i = int(f)
print(i)

#14
ff = 23.2324
ro = round(ff, 2)
print(ro)

#15
name = input("What's your name? ")
print(name)

#MEDIUMM

age = input("What is your age?  ")
print(type(age))
i = int(age)
print(type(i))
i += 1
print(i)
i *= i
print(i)

res = 3 * 2
print(res)
print(3 / 2)

#20
di  = 43 // 4
print(di)

ex = 5 **3
print(ex)

re = 10 % 3
print(re)

print(abs(-12))

#21
ev1 = True and False
print(ev1)

ev2 = True or False
print(ev2)

ev3 = not False
print(ev3)

#22
ch1 = 10 > 3
print(ch1)

ch2 = 5 == 5
print(ch2)

ch3 = 8 != 9
print(ch3)

ch4 = 7 >= 7
print(ch4)

#22
#Ask the user for two numbers and print their sum. (Remember: conver input)

nr = input("First nr: ")
sc = input("secind nr: ")

sum0 = int(nr)
sum1 = int(sc)

print(type(sum))
sum11 = sum0 + sum1
print(sum11)

#23
nr = int(input("Firs: "))
sc = int(input("Second: "))
print(nr + sc)


#ADVANCED

#24
nr1 = int(input("Enter the first number: "))
nr2 = int(input("Enter the second number: "))
product = nr1 * nr2
print(product)

#25
a = int(input("Enter the a side of rectangle: "))
b = int(input("Enter the b side of rectangle: "))
summ = a * b
print(summ)

#26
a = int(input("Enter the a side of rectangle: "))
b = int(input("Enter the b side of rectangle: "))
per = (2*(a + b))
print(per)

#27
b = int(input("Enter the base: "))
h = int(input("Enter the height: "))
sur = b * h / 2
print(sur)

#28
l = [1,2,3,4,5]
print(l[3])

l2 = [1,2,3,4,5]
print(l2[-1])

#29
user = float(input("Enter a number: "))
print(round(user, 2))

#30
age = input("Enter your age: ")
print(age * 2)

#31
age = input("Enter your age: ")
c = int(age)
print(c * 2)

#32
res = (2 + 3) * 6 / 2
print(res)

#33
l = 4 > 3
les = 43 < 223
n = 23 != 233
print(l, les, n)

l1 = False and True
print(l1)
l2 = False or True
print(l2)


#34
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print(f"Integer division: {n1} // {n2} is ", n1 // n2)
print(f"Exponent: {n1} ** {n2} is ", n1 ** n2)
print(f"Remaider: {n1} % {n2} is ", n1 % n2)


#35
var = 5
print("Initial value: ", var) 
var += 5
print("After +=: ", var)
var -= 5
print("Ater -=: ", var)
var *= 5
print("After *=: ", var)

#36
var = int(input("Type the number of pupils: ")) 
bench = (var + 1) // 2
print(f"The number of benches need for {var} pupils is: {bench}")
