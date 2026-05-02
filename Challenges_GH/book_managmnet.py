#BOOK MANAGMENT

books_added = []
borrowed_book = []
#

while True:
    print("Choose option:")
    print()
    print("1.Add book")
    print("2.Borrow book")
    print("3.Return book")
    print("4.View available books")
    print("5.View which books are borrowed")
    print("6.EXIT")
    
    # books_added = []
    # borrowed_book = []
    #This is not efficient because if user enters letters it will show errors
    #user = int(input("Enter your option: "))
    print()
    user = input("Enter your option: ")
    print()
    

    if not user.isdigit():
        print("Please enter a number.\n")
        continue

    user = int(user)
    
    if user == 1:
        print("-------------------------------------")
        print("              Add book               ")
        print("-------------------------------------")
        print()
        add_book = input("Enter the name of the book: ")
        if add_book in books_added:
            print("This book is already added!")
            print()
        else:
            books_added.append(add_book)
            print("Book added succesfully!")
            print()
    elif user == 2:
        print("-------------------------------------")
        print("               Borrow a book         ")
        print("-------------------------------------")
        b_book = input("Enter the name of the book you want to borrow: ")
        if b_book in books_added:
            borrowed_book.append(b_book)
            books_added.remove(b_book)
            print("Book borrowed succesfully!")
            print()
        elif b_book in borrowed_book:
            print("This book is borrowed by someone else!\n")
           ## b_book.append(borrowed_book)
        else:
            print("This book does not exist.")
            print()
    elif user == 3:
        print("--------------------------------------")
        print("              Return a book           ")
        print("--------------------------------------")
        r_book = input("Enter the name of the book you want to return: ")
        print()
        if r_book in borrowed_book: 
            borrowed_book.remove(r_book)
            books_added.append(r_book)
            print("Book was returned succesfully!")
            #print("You either mistyped, or this book was never borrowed")
            #print("OR ELSE. DID YOU STOLE THIS BOOK?")
        else:
            print("You either mistyped, or this book was never borrowed")
            print("OR ELSE. DID YOU STOLE THIS BOOK?")
            print()
    elif user == 4:
        print("---------------------------------------")
        print("          View Available Books         ")
        print("---------------------------------------")
        #string_var = “ “.join(list)
        if books_added:
            
            av_books = "\n".join(books_added)
            print("***********************************")
            print(av_books)
            print("***********************************")
            print()
    elif user == 5:
        print("---------------------------------------")
        print("          View Borrowed Books          ")
        print("---------------------------------------")
        bb_books = "\n".join(borrowed_book[:])
        print("***********************************")
        print(bb_books)
        print("***********************************")
        print()
    elif user == 6:
        print("Thank you for using our program!")
        print("Exiting the program...")
        break
    else:
        print("Choose option:")
        print()
        print("1.Add book")
        print("2.Borrow book")
        print("3.Return book")
        print("4.View available books")
        print("5.View which books are borrowed")
        print("6.EXIT")
             
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        