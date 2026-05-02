#ATM Withdrawal

init_balance = 1000

while True:
   print("--------------------------------------")
   print("            ATM Withdrawal            ")
   print("--------------------------------------\n")
    
   print("MENU: \n")
   print("1.Withdraw")
   print("2.Deposit")
   print("3.Check Balance")
   print("4.EXIT")
   
   option = input("Enter your option: ")
   
   if not option.isdigit():
       print("Please enter a number from 1 to 4")
       continue
   option = int(option)
   
   if option == 1:
       
       while True:
           
          print("--------------------------------------")
          print("            Withdraw Money            ")
          print("--------------------------------------\n")
          
          print("Your initial balance is: ", init_balance)
          withdraw = input("Enter the amount you want to withdraw: ")
          print("Or enter '4' to exit from service 'Withdraw Moeny'")
          if not withdraw.isdigit():
              print("Please enter a number!!!")
              continue
          
          
          withdraw = int(withdraw)
          
          
          if withdraw > init_balance:
              print("You can not withdraw an amount bigger than your balanace")
              print("Your balance is: ", init_balance)
              continue
          elif withdraw == 4:
              print("Exiting the system...")
              break
          else:
              init_balance = init_balance - withdraw
              print(f"You withdrawed {withdraw}.")
              print("Your balance now is: ", init_balance)
    
   elif option == 2:
        print("--------------------------------------")
        print("            Deposit Money            ")
        print("--------------------------------------\n")
        
        deposit = input("Enter the amount of money you want to deposit: ")
        if not deposit.isdigit():
            print("Please enter the amount in number!")
            continue
        deposit = int(deposit)

        if deposit >= 0:
            init_balance = init_balance + deposit
            print(f"You deposited {deposit}$")
            print("You balance now is: ", init_balance)
        else:
            print("Enter an amount bigger than 0.")
            continue
   elif option == 3:
       print("--------------------------------------")
       print("            CHeck Balance             ")
       print("--------------------------------------\n")
       
       print("You balance is: ", init_balance)

   elif option == 4:
       print("Thank you for using our services!")
       print("Exiting the program...")
       break
   else:
       continue
        
    