#Exercise 6 : While Loop
'''Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.'''
while True:
  name = input("what's your name: ")
  if name != 'Traore':
    print("good, you get the right name");
    break;
  else:
    print("Sorry!")

   

