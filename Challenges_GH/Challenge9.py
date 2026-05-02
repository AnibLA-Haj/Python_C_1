#Challenge 3: Multipication Table Generator

input_user = input("Enter a number: ")

one = ((input_user == "1") and print("The multiplication for one:\n 1 x 1 = 1\n 1 x 2 = 2\n 1 x 3 = 3 \n 1 x 4 = 4\n 1 x 5 = 5\n 1 x 6 = 6\n 1 x 7 = 7\n 1 x 8 = 8\n 1 x 9 = 9\n 1 x 10 = 10"))
two = ((input_user == "2") and print("The multiplication for two:\n 2 x 1 = 2\n 2 x 2 = 4\n 2 x 3 = 6 \n 2 x 4 = 8\n 2 x 5 = 10\n 2 x 6 = 12\n 2 x 7 = 14\n 2 x 8 = 16\n 2 x 9 = 18\n 2 x 10 = 20"))
three = ((input_user == "3") and print("The multiplication for three:\n 3 x 1 = 3\n 3 x 2 = 6\n 3 x 3 = 9 \n 3 x 4 = 12\n 3 x 5 = 15\n 3 x 6 = 18\n 3 x 7 = 21\n 3 x 8 = 24\n 3 x 9 = 27\n 3 x 10 = 30"))
four = ((input_user == "4") and print("The multiplication for four:\n 4 x 1 = 4\n 4 x 2 = 8\n 4 x 3 = 12 \n 4 x 4 = 16\n 4 x 5 = 20\n 4 x 6 = 24\n 4 x 7 = 28\n 4 x 8 = 32\n 4 x 9 = 36\n 4 x 10 = 40"))
five = ((input_user == "5") and print("The multiplication for five:\n 5 x 1 = 5\n 5 x 2 = 10\n 5 x 3 = 15 \n 5 x 4 = 20\n 5 x 5 = 25\n 5 x 6 = 30\n 5 x 7 = 35\n 5 x 8 = 40\n 5 x 9 = 45\n 5 x 10 = 50"))
six = ((input_user == "6") and print("The multiplication for six:\n 6 x 1 = 6\n 6 x 2 = 12\n 6 x 3 = 18 \n 6 x 4 = 24\n 6 x 5 = 30\n 6 x 6 = 36\n 6 x 7 = 42\n 6 x 8 = 48\n 6 x 9 = 54\n 6 x 10 = 60"))
seven = ((input_user == "7") and print("The multiplication for seven:\n 7 x 1 = 7\n 7 x 2 = 14\n 7 x 3 = 21 \n 7 x 4 = 28\n 7 x 5 = 35\n 7 x 6 = 42\n 7 x 7 = 49\n 7 x 8 = 56\n 7 x 9 = 63\n 7 x 10 = 70"))
eight = ((input_user == "8")and print("The multiplication for eight:\n 8 x 1 = 8\n 8 x 2 = 16\n 8 x 3 = 24 \n 8 x 4 = 32\n 8 x 5 = 40\n 8 x 6 = 48\n 8 x 7 = 56\n 8 x 8 = 72\n 8 x 9 = 72\n 8 x 10 = 80"))
nine = ((input_user == "9") and print("The multiplication for nine:\n 9 x 1 = 9\n 9 x 2 = 18\n 9 x 3 = 27 \n 9 x 4 = 36\n 9 x 5 = 45\n 9 x 6 = 54\n 9 x 7 = 63\n 9 x 8 = 72\n 9 x 9 = 81\n 9 x 10 = 90"))
ten = ((input_user == "10") and print("The multiplication for ten:\n 10 x 10 = 2\n 10 x 2 = 20\n 10 x 3 = 30 \n 10 x 4 = 40\n 10 x 5 = 50\n 10 x 6 = 60\n 10 x 7 = 70\n 10 x 8 = 80\n 10 x 9 = 90\n 10 x 10 = 100"))


#README
#This program shows my journey of learning python.
#I am excited to learn in the near future about flow controls, so I can see how easy it will be to write the same program.
#I did that program without the flow controls.
#We see how much we have to type manually to give us the desired results.

#Why we are using "and" logical operator
#TRUE and TRUE = TRUE
#TRUE and FALSE = FALSE
#FALSE and TRUE = FALSE
#FALSE and FALSE = FALSE
#So when the user types for example 4, it goes to the first varibale which is 1, and compare ("4" == "1")
#and 4 is not equal to 1, so it give us FALSE, then print part is TRUE. FALSE and TRUE, gives us FALSE
#It continues till' the variable four, when it comapres ("4" == "4"),"4" is equal to "4", so it gives us TRUE
#The print part is Always TRUE, so TRUE and TRUE is TRUE. 
#Gives us the muliplication for 4.

