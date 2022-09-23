"""
Exercise2

Instructions
1.Create a class called Dog.
2.In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
3.Create a method called bark that prints the following string “<dog_name> goes woof!”.
4.Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
5.Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
6.Print the details of his dog (ie. name and height) and call the methods bark and jump.
7.Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
8.Print the details of her dog (ie. name and height) and call the methods bark and jump.
9.Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

"""
class Dog:
  def __init__(self,Dogname,Dogheight):
    self.name=Dogname
    self.height=Dogheight


  def bark(self):
  	print(f"{self.name} goes woof")

  def jump(self):
  	x=self.height*2
  	print(f"{self.name} jump {x} cm high!")

davids_dog=Dog("Rex",50)
print(f"{davids_dog.name},{davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()
sarahs_dog=Dog("Teacup",20)
print(f"{sarahs_dog.name},{sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height>sarahs_dog.height:
  print(f"The bigger dog is {davids_dog.name}")
elif sarahs_dog.height>davids_dog.height:
  print(f"The bigger dog is {sarahs_dog.name}")
else:
  print(f"There is no bigger dog they have equal height")



