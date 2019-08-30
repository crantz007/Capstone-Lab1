# Write a 'guess the number' game. The computer should 'think' of a random number within a certain range
import  random
guess_number =2

user = int(input("Enter a number between 1 and 100: "))
number = random.randint(1,100)
while user < guess_number :
    print("Too low")
    user = int(input("Enter a number between 1 and 100: "))
    if user > guess_number :
        print("Too high")
        user = int(input("Enter a number between 1 and 100: "))
    else:
        print("Guess Number!!!")
