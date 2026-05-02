#SIMPLE BANKING SYSTEM

balance = 0

print("Banking program")
print("Welcome to your banking account!")
print()

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    option = int(input("Choose option: "))
    if option == 1:
       deposit = int(input("Enter amount to deposit: "))
       balance = balance + deposit
       print("Deposit successful")
       print("Current balance: ", balance, "$")
       print()
    elif option == 2:
       withdraw = int(input("Enter amount to withdraw: "))
       if balance >= withdraw:
           balance = balance - withdraw
           print("Withdrawal successful.")
           print("Current balance: ", balance, "$")
           print()
       else:
           print("You dont have enough money!")
    elif option == 3:
       print("Current balance is: ", balance, "$")
       print()
    elif option == 4:
       print("You exited the program, thank you for using our services!")
       break
    else:
       print("You can you only those options!")
       print("1. Deposit")
       print("2. Withdraw")
       print("3. Check Balance")
       print("4. Exit")

       option = int(input("Choose option: "))
    
    
    
    
    
