# Write a program that asks for your name and the month you were born in
# input
name = input("What is your name : ")
month = input("What month your were born: ")
# display
print('Good Morning ,', name,'\n')

print('There is',(len(name)-name.count(" ")),'letters in your name','\n')
# Condition to check if birth is on angust
if month =='august':
    print('Happy Birthday!!! ',name)
else:
    print('Your birthday is not on August !')


