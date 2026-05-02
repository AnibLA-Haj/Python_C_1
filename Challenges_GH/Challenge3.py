"""
Compute rectangle area,  A = L x w
rectangle perimeter, and P = 2(L+W)
triangle surface in one program based on user input. P= a +b +c
"""
print("Compute rectangle area, rectangle perimeter, triangle surface")
print("Answer with 'yes' or 'no'")
print()
q1 = input("Do you want to compute rectangle area? ")

if q1 == "yes":
    l = int(input("Enter the length: "))
    w = int(input("Enter the width:  "))
    a = l * w
    print("The rectangle area is: ",a) 
else:
    print("OKAY")

q2 = input("Do you want to compute rectangle perimeter? ")    
if q2 == "yes":
    l = int(input("Enter the length: "))
    w = int(input("Enter the width:  "))
    p = 2 *(l+w)
    print("The rectangle perimeter is: ", p)
else:
      print("OKAY")

q3 = input("Do you want to compute triangle surface? ")
if q3 == "yes":
    a = int(input("Enter the value of a side: "))
    b = int(input("Enter the value of b side: "))
    c = int(input("Enter the value of c side: "))
    p = a + b + c
    print("The triangle surface is: ", p)
else:
    print("OKAY")