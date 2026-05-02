#9 -Ask the user for 5 numbers (input 5 times),
#convert each to an integer, store them in a list,
#then print:
    
fr = int(input("Enter the first number: "))
sc = int(input("Enter the second number: "))
thr = int(input("Enter the third number: "))
frth = int(input("Enter the fourth number: "))
fith = int(input("Enter the fifth number: "))

lst = [fr, sc, thr, frth, fith]

sum = lst[0] + lst[1] + lst[2] + lst[3] + lst[4]
print("The sum of the list is: ", sum)
print("The first element of the list is: ", lst[0])
print("The remainder of the last element when divided by 2 is: ", lst[-1] % 2)
