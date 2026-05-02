# Basic Calculator (no if/else)

first_nr = int(input("Enter the first number: "))
second_nr = int(input("Enter the second number: "))

operator = input("Type one of the operators (+, -, *, /): ")

#First we are doing the calculation in that case addition
plus = first_nr + second_nr
#Then we are doing the comparison if the operator is equal with +, let it print waht is inside the print funciton
res_plus = ((operator == "+") and print(first_nr, " + ", second_nr, " = ", plus))

minus = first_nr - second_nr
res_plus = ((operator == "-") and print(first_nr, " - ", second_nr, " = ", minus))

multiply = first_nr - second_nr
res_multiply = ((operator == "*") and print(first_nr, " * ", second_nr, " = ", multiply))

divide = first_nr / second_nr
res_divide = ((operator == "/") and print(first_nr, " / ", second_nr, " = ", divide))



#THose lines below, gives us undesired results
#plus = operator == "+" and first_nr + second_nr
#print(first_nr, " + ", second_nr, " = ", plus)
#print("The result is: ", plus)

#minus = operator == "-" and first_nr - second_nr
#print(first_nr, " - ", second_nr, " = ", minus)
#print("The result is: ", minus)