#Challenge 2: Word Reverse

text = "python"
print("Print the string normally: ", text)
print("The string in reveresed format: ",text[::-1])


#Let's see how the sentence of a string is reversed
sen = "i love py"
print("Print the string normally: ", sen)
print("The sentence of the string in the reversed format: ",sen[::-1])

#Reversing the words of a sentence instead of letters

sente = "I study everyday"
print("The sentence: ", sente)
reversed_se = " ".join(sente.split()[::-1])
print("The reversed sentence(only words): ", reversed_se)

#When doing analysis, everytime start from the parentheses
#In that case start from sente.split()[]

#How split works, real example
fjali = "i love py"
words = fjali.split()
print("What split method do: ",words)

#split is a string method, what it does is, ittakes the srting from a variable it seperates it
#by defautl it seperates by " " - space, so you can determine how to seperate a string
#and then the seperated string, become the elements of a list.
#Long story made short, .split method turns a string into a list.
# [::-1] - that is called index slicing, and why on earth are we allowed to use that is becuase the string that the split took, it is now a list
# and index slicing works on list
#And not only odes it work on list, but it works on any sequence type as strings, lists, tuples, etc
#[start:stop:step] - [::-1]
#[::-1] [default:default:-1]
#when you dont specify, the values of indexing, python uses the default, start value by default is 0
#stop value by default is end of sequence
#-1 means start from the end of the string, reverse order
#1 means move forward one step at a time, take everything in the normal direction
# .join it takes a list of strings and joins them together into one big string
#"seperator".join(list_of_strings)
#that means join all strings in the list using "seperator" between them
#in our case is " ".join..., which means seperate the elements of a list by space

#Example with input, what the user enters
input_user = input("Type something: ")
print("What you typed: ", input_user)
print("Reserved format: ",input_user[::-1]) 






