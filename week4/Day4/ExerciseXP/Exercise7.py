import random

#Exercise7

#Instuction
"""
1.Create a function called get_random_temp().

  1.This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
  2.Test your function to make sure it generates expected results.

2.Create a function called main().
  1.Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
  2,Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius

3.Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
  1.below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
  2.between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
  3.between 16 and 23
  4.between 24 and 32
  5.between 32 and 40

"""
def get_random_temp (season):
  if season.casefold()=="fall":
   return random.randrange(-10,16)
  elif season.casefold()=="summer":
   return  random.randrange(15,20)
  elif season.casefold()=="autumn":
   return  random.randrange(30,40)
  elif season.casefold()=="spring":
   return  random.randrange(0,20)
  
  
def main():
  season=input("Enter the season")
  temperature= get_random_temp(season);
  print(f"The  temperature right now is {temperature} degrees Celsius ")
  if temperature<0:
    print("Brrr, that’s freezing! Wear some extra layers today")
  elif temperature>=0 and temperature<16:
    print("Quite chilly! Don’t forget your coat")
  elif temperature>=16 and temperature<=23:
    print("Beau temp")
  elif temperature>=24 and temperature<32:
    print("Normal")
  elif temperature>=32 and temperature<40:
    print("Tres Ensoleillé ")
main()