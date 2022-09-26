"""
🌟 Exercise 3 : Dogs Domesticated
Instructions
1Create a new python file and import your Dog class from the previous exercise.

2In the new python file, create a class named PetDog that inherits from Dog.

3Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.

4Add the following methods:
 .train: prints the output of bark and switches the trained boolean to True

 .play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

 .do_a_trick: If the dog is trained the method should print one of the following sentences at random:
“dog_name does a barrel roll”.
“dog_name stands on his back legs”.
“dog_name shakes your hand”.
“dog_name plays dead”.

"""
from Exercise2 import Dog as Dg
import random

class PetDog (Dg):
	Dg.trained=False
	def train(Dg):
		Dg.bark()
		Dg.trained=True;
	def play(Dg,*args):
		print(Dg.name,",",",".join(args),"all play together")
	def do_a_trick(self):
		trick=["does a barrel roll","stands on his back legs"," shakes your hand","plays dead"]
		rndm=random.randrange(0,len(trick))
		if self.trained:
			print(self.name,trick[rndm])
		else:
			print(self.name ,"not trained")


dog1=PetDog("PetDog1");
dog2=PetDog("PetDog2")
dog3=PetDog("PetDog3")
dog4=PetDog("PetDog4")

print(dog1.trained)
dog1.train()
print(dog1.trained)
dog1.do_a_trick()
dog2.do_a_trick()
dog1.play(dog2.name,dog3.name)