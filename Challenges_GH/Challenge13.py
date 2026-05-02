#Traffic ligh system
#Ask the user to input the color of a traffic light (red, yellow, green)

user  = input("Enter the color og a traffic light: ")
if user.lower() == "red":
    print("Stop")
elif user.lower() == "yellow":
    print("Ready")
elif user.lower() == "green":
    print("Go")
else:
    print("Invalid color")
