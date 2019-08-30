# Write a program that turns a sentence into camel case. The first word is lowercase,
# the rest of the words have their initial letter capitalized,
# and all of the words are joined together
import string
# input
keep_trying ='y'
while keep_trying == 'y' :
    user = input("Type a sentence : ")
    # Excpetions
    invalid = set(string.punctuation)
    if any(char in invalid for char in user):
        print("No special characters")
    else :
        print("no integers")

    # Capitalized all letter without space
    capital= string.capwords(user).replace(" ","")

    # Making first Letter lowercase
    capital = capital[0].lower() + capital[1:]
    # Output
    print(capital)
    keep_trying = input('Do you want to try again(Enter y for yes):')