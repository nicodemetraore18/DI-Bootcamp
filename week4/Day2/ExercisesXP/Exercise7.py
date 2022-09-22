# Exercise 7: Favorite Fruits
#Ask the user to input their favorite fruit(s) (one or several fruits).
fruits = input("write your favorite fruits and separe its with a single white space:  ")
fruits = fruits.split()

otherFruit = input("input a name of any fruit: ")
if otherFruit in fruits:
    print("You chose one of your favorite fruits! Enjoy")
else:
    print("You choose a new fruits. I hope you enjoy.")
    

