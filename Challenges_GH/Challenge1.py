"""
Ask the user for two numbers. 
Convert them, compute all operations (+, −, *, /, //, %, ),
and print all results clearly.
"""
print("Simple Calculator App")
print("Welcome to our app!")
fr_nr = int(input("Enter the first number: "))
sc_nr = int(input("Enter the second number: "))
print()
print("Use one of the operations (+,-,*,/,//,%)")
print()
op = input("Enter the operation: ")

if op == "+":
    res = fr_nr + sc_nr
    print("The result is: ",res)
elif op == "-":
    res = fr_nr - sc_nr
    print("The result is: ",res)
elif op == "*":
    res = fr_nr * sc_nr
    print("The result is: ",res)
elif op == "/":
    res = fr_nr / sc_nr
    print("The result is: ",res)
elif op == "//":
    res = fr_nr // sc_nr
    print("The result is: ",res)
elif op == "%":
    res = fr_nr % sc_nr
    print("The result is: ",res)
else:
    print("TYPE CORRECTLY THE VALUES, AND OPERATION!!!")