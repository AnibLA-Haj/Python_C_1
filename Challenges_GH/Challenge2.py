"""
VERY SIMPLE APP
#3**Ask the user for 3 numbers, store them in a list, 
and print the first and last elements.
"""

print("Simple application")
print()
fr_nr = int(input("Enter the first number: "))
sc_nr = int(input("Enter the second number: "))
thr_nr = int(input("Enter the third number: "))
#store those numbers in a list
lllist = [fr_nr, sc_nr, thr_nr]
print("We saved those numbers in a list!")
print()
print("The first number of the list is: ",lllist[0])
print("The last number of the list is: ",lllist[-1])