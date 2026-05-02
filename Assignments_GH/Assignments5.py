"""
Assignments 
"""

#1
#print numbers from 1 to 10 one by one
for i in range(1,11):
     print(i)

#2
#Print each element in the list: ["apple", "banana", "cherry"].

list = ["apple", "banana", "cherry"]

for i in list:
    print(i)

#3
#Print "Hello" 5 times.
for i in range(5):
    print("Hello")

#4
#Print each number from 1–20 only if it’s even.
for i in range(1,20+1):
    if i % 2 == 0:
        print(i)

#5
#Print squares of numbers 1–10 (like 1, 4, 9, 16…).
for i in range(11):
    print(i**2)
    
#6
#Print "Counting…", then the number, for numbers 1 to 5.
for i in range(1,6):
    print("Counting...", i)

#7
#Loop through a name "ALBANA" and print each character.
name = "David"
for i in name:
    print(i)

#8
#From a list of ages: [12, 19, 4, 25, 16], print only the ages ≥ 18.

list = [12, 19, 4, 25, 16]
for i in list:
   if i >= 18:
      print(i)

#9
#Print a star pattern:
# *
# **
# ***
# ****

for i in range(5):
    print("*" * i)

#10
#Print multiples of 7 from 7 to 70

for i in range(7, 71):
     if i % 7 == 0:
         print(i)


#11
#Find and print the sum of numbers 1–100.

total = 0
for i in range(1,101):
    total = total + i
print(total)

#12
#Count how many even numbers exist in 1–30 and print the count.
total = 0
for i in range(1,31):
    if i % 2 == 0:
        total = total + 1
        print(i)
print("The total number of even number is ", total)  

#13
#Ask the user for 5 numbers → print the largest number at the end.

fr = int(input("Enter the first number: "))
sc = int(input("Enter the second number: "))
thr = int(input("Enter the third number: "))
fth = int(input("Enter the fourth number: "))
fif = int(input("Enter the fifth number: "))

numbers = [fr, sc, thr, fth, fif]
largest = 0
for i in numbers:
    print(i)

print("The largest number is: ", max(fr, sc, thr, fth, fif))

#14
#Compute the product of numbers 1–10 and print the result.

total = 1
for i in range(1,11):
    total = total * i
print(total)

#15
#Count how many numbers in [3,7,2,9,11,13,4] are odd.

lists = [3,7,2,9,11,13,4]
for i in lists:
    if i % 2 != 0:
        print("This number is odd: ",i)

#16
#Loop through "hello world" and count how many 'l' characters there are.

wo = "Hello World"
total = 0
for i in wo:
    if i == "l":
        print(i)
        total = total + 1

print(f"There are {total} 'l's'")

#17
#From [10, 20, 5, 30, 15] find the smallest number.

nu = [-1, 20, 5, 30, 15]
smalle = nu[0]

for i in nu:
    if i <= smalle: #we are doing here <= becuase to count the first number, becuase if we dont it will not compare the first number
        print(i)

#18
#. Calculate the total length of all strings in a list: ["dog", "cat",
#"elephant"].

l =  ["dog", "cat"]

total = 0
for i in l:
    total = total + len(i)
print(total)

#19
#Ask the user for 4 temperatures → calculate the average and print it 
#formula average = sumofallnumbers / the total number entered
aver = 0
total = 0
for i in range(1,4):
    user = int(input("Enter the temp: "))
    total = total + user
    aver = total / i
print(aver)

#20
#Count how many times the number 3 appears in [1,3,5,3,3,2,3].

ls = [1,3,5,3,3,2,3,3,4,5,3]

total = 0
for i in ls:
    if i == 3:
        print(i)
        total = total + 1
print(total)

######idn
# total = 0
# for i in range(5):
#     nr = int(input("Type: "))
#     if nr == 3:
#         print(nr)
#         total = total + 1
# print(total)

#21
#You want to print all odd numbers between 1 and 15.

for i in range(1,16):
    if i % 2 != 0:
        print(i)

#22
#You want to calculate the sum of all odd numbers 1–15.

total = 0
for i in range(1,16):
    if i % 2 !=0:
        total = total + i
print("The sum of all odd numbers is: ", total)

####
##Count only how many odd numbers are there, say like the there are {} odd numbers
##Also print all numbers but just count how many numbers are odd there
# to = 0
# for i in range(1,16):
#     print(i)
#     if i % 2 != 0:
#         to = to + 1
# print(f"There are {to} odd numbers")
        
#23
#You want to print every character in a word.

count = 0 #if we put count =+ 1 in 225 line we have to do it 1
word = input("Enter a word: ")

for i in word:
    count = count + 1
    print(count, i, sep=".") #sep="", is a seperator, we can decide waht seperator do we want otherwise from space, in our case we choose dot .
    count = count + 1


#24
#You want to count how many vowels are in a word.

vowels = ["a", "e", "i", "o", "u"]

user = input("Enter a word: ")
for i in user:
    if i in vowels:         
        print(i)

#25
#Print numbers 1–5 with the text "- done" after the loop is finished.

for i in range(1,6):
     print(i)
print("Done")

#26
#From a list of test scores, print "Pass" for each passing score.

score = [1,23,45,65,78,97,34,100,99,87]

for i in score:
    if i >= 70:
        print("Pass",i, sep="-")
    else:
        print("Fail ", i) # me being creative


#27
#From the same list, print the average score once at the end. ABOVEE

score = [1,23,45,65,78,97,34,100,99,87]

#the formula for average is avg = sum(of the list) / the numbers in the list in our case 4
#and who holds the number of iteration in the score is i
avg = sum(list) / len(score)
avg = sum(list) / i #- i changes every iteration, we need a number that doesnt change in our case le(score)
sum(list) 
total = 0

total = total + i
avg = 0
total = 0
for i in score:
     print(i)
     total = total + i
     avg = total / len(score)
print(total)
print(avg)

#28
#You want to check numbers 1–20 and print "Even" or "Odd" for each.
for i in range(1,21):
    if i % 2 ==0:
        print("Even ", i)
    else:
        print("Odd ", i)


#29
#Create a sum of numbers divisible by 4 (but print only once).

lsit = [3,4,2,1,56,32,21,24,54,64,23]
totali = 0

for i in lsit:
    if i % 4 == 0:
        totali = totali + i
print("The sum of numbers divisble by 4 is: ", totali)

# #30
# Print "Loop finished!" after the loop ends.

for i in range(10):
     print(i+1)
print("Loop Finished!")







