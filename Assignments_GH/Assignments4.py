#Assignment 1: Phone Contacts

contacts = ["Alice", "Bob", "Charlie"]

new_contacts = ["Diana", "Evan"]

new = contacts + new_contacts
print(new)

ch = "Bob" in new
print(ch)

print(new[1:-1])

#Assignment 2 
#student record

student = ["John", 20, ["Math", "Physics", "CS"]]
print(student[0])
print(student[-1])
student[-1].append("English")
print(student)  
student[-1].remove("Math")
print(student)

#Assignment 3
#Count how many numbers are positive

user = input("Enter 5 numbers: ")
# print(user)
# print(type(user))

ls = user.split() # WE ARE USING split here, becuase the list will take also the spaces, so we want that spaces not to be taken as element, and split by default has the space as seperator
#split will turn the string into a list, so no need for the list method 
# print(ls)
# print(type(ls))
lis_nr = list(map(int, ls))
print(lis_nr)

count = 0
for i in lis_nr:
    if i >= 1:
        count = count + 1
print("Positive numbers: ", count)

######JUST EXERCISING
# user = input("enter: ")
# print(user)
# print(type(user))
# ls = list(user)
# print(ls)
# print(type(ls))


#Assignment 3
#Count how many strings are longer than 3 characters
#ask the user for four words

# for i in range(4):
#     user = input("Enter a word: ")
#     for ii in user:
#         count = count + 1
#         #nr = int(ii)
#         if count > 3:
#             print(ii)
#     # for ii in lss:
# print(count)
    
# #Assignment 4  
# to = 0 
# for i in range(4):
#     user = input("Enter a word: ")
#     for ii in user:
#           #print(type(user))
#           lss = user.split()
#           if ii > 3:
#             to = to + 1 
#     print(lss)
#     print(type(lss))

# #Assignment 5
# count = 0
# for i in range(4):
#     user = input("Enter a word: ")
#     if len(user) > 3:
#         print(user)
# print(count)
##to do that you need to use lists 
#you can use append to add items to the list, and from them list to a=print only words with 3 letter and more

#the solutionnnn
#Assignment 6
wo = []
result = ""
for i in range(4):
    user = input("Enter a word: ")
    if len(user) > 3:
        wo.append(user)
        result = " ".join(wo)
print(wo)
print(len(wo))
print(result)




