# Write a 'guess the number' game. The computer should 'think' of a random number within a certain range
import  random
guess_number = random.randint(1,100)
keep_going ='y'

while keep_going =='y':
  user = int(input("enter a number between 0 and 100: "))
  if user < guess_number:
    print("Too Low")

  elif user == guess_number :
    print("Guess Number !!!")

  elif user > guess_number :
   print("Too High")
  keep_going = input('Do you want to try again(Enter y for yes):')