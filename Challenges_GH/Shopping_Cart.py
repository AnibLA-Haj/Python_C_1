#Shopping cart

items = []

while True:
    
    print("-----------------------------------------")
    print("               Shopping Cart             ")
    print("-----------------------------------------\n") 
    
    print("MENU:")
    print("1.Add item")
    print("2.Remove item")
    print("3.View cart")
    print("4.Exit\n")
    
    option = input("Enter your option: ")
    
    if not option.isdigit():
        print("Enter only digits (1-4)!")
        continue
    option = int(option)
    
    if option == 1:
        while True:
            print("-----------------------------------------")
            print("               Adding Item               ")
            print("-----------------------------------------\n") 
            print("Enter 4 when you are done adding items!")
            add_item = input("Add items: ")
            
            
            if add_item == "4":
                print("Exiting the menu 'Add Items'")
                break
            elif add_item != items:
                items.append(add_item)
                print("Item added successfully!")
            else:
                print("This item already exisit")
        
    if option == 2:
        while True:
            print("-----------------------------------------")
            print("               Remove Item               ")
            print("-----------------------------------------\n") 
            print("Enter 4 when you are done adding items!")
            
            r_item = input("Enter the item you want to remove: ")
            
            if r_item == "4":
                print("Exiting the menu 'Remove Item'...")
                break
            elif r_item == items:
                print("This item does not exist in cart!")
            else:
                items.remove(r_item)
                print("Item was successfully removed from cart!")
                
                
               
    if option == 3:
        print("-----------------------------------------")
        print("                View Items               ")
        print("-----------------------------------------\n") 
        
        count = 0
        for item in items:
            count +=1
            print(f"{count}.{item}")
        print("-----------------------------------------\n") 
    
    if option == 4:
        print("Thank you for using our program!")
        print("Exiting the program...")
        break
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        