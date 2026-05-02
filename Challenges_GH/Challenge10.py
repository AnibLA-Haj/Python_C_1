#Challenge 4: List Average Filter (NO if else)

user_input = input("Enter several numbers seperated by space: ")

#We are using split beacuse it turns the string, in our case the input which is string in a list
list_input =  user_input.split()
print("The list with numbers that are string:")
print(list_input)
print(type(list_input))

#Convert the string elements of the list into integers
list_int = list(map(int, list_input))
print("The converted list into integers:")
print(list_int)


#we are using round method, to give us the average number, with only 2 digit after the dot.
average = round(sum(list_int[::]) /  len(list_int), 2)
print("The average of the numbers of the list is: ",average)



#TO turn the elements of the list from string to int, we should use the map function
#The map() function applies a function to every element of a sequence (like a list or tuple)
#Automatically without you needing to write a for loop
#What map does, it takes each element in the list in our case, runs through a function and gives us a map object
#I dont know what a map object is
#But what can we do is to wrap the map function INTO A LIST METHOD, and then it gives us the result we want

"""numbers_string = ["2", "3", "4", "5"]
numbers = map(int, numbers_string)
print(numbers)"""
#This ^ gives us <map object at 0x755320543400>

#So now lets use list method
"""numbers_s = ["2", "3", "4", "4"]
numberss = list(map(int, numbers_s))
print(numberss)"""

























'''list_input = " ".join(user_input.split())
print(list_input)
print(type(list_input)'''
      



