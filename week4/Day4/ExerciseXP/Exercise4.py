""" 
Instructions
1 Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

"""
import random;



def Iguess():
  user_number=input("Enter a number between 1 and 100");
  Computer_number=random.randrange(1,100)
  
  if Computer_number==user_number:
    print ("Good Job you guess the right number");
  else:
    print("Sorry Try again! The number was ", Computer_number)




Iguess();


