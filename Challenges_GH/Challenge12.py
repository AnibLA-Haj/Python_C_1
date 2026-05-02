#Challenge 1: Even and Odd Counter (Without Conditions)
print()
print("Finding which numbers are even and which are odd")
nr_1 = int(input("Type the first number: "))
nr_2 = int(input("Type the second number: "))
nr_3 = int(input("Type the third number: "))
nr_4 = int(input("Type the fourth number: "))
nr_5 = int(input("Type the fifth number: "))
nr_6 = int(input("Type the sixth number: "))
nr_7 = int(input("Type the seventh number: "))
nr_8 = int(input("TYpe the eighth number: "))
nr_9 = int(input("Type the ninth number: "))
nr_10 = int(input("Type the tenth number: "))

list_nr = [nr_1, nr_2, nr_3, nr_4, nr_5, nr_6, nr_7, nr_8, nr_9, nr_10]

print(list_nr)

remainders = [nr_1 % 2, nr_2 % 2, nr_3 % 2, nr_4 % 2, nr_5 % 2, nr_6 % 2, nr_7 % 2, nr_8 % 2, nr_9 % 2, nr_10 % 2]

odd_count = sum(remainders)
even_count = 10 - odd_count

print("The total number of odd numbers is: ",odd_count)
print("The total number of even numbers is: ", even_count)