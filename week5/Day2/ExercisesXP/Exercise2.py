"""
Exercise1.py

Instructions
1.Create a class called Dog with the following attributes name, age, weight.
2.Implement the following methods in the Dog class:
.bark: returns a string which states: “<dog_name> is barking”.
.run_speed: returns the dogs running speed (weight/age*10).
.fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

3.Create 3 dogs and run them through your class.

"""

class Dog():
	def __init__(self,name="Chien",age=1,weight=15):
		self.name=name
		self.age=age
		self.weight=weight
	def bark(self):
		 print(f"{self.name} is barking")
	def run_speed(self):
		running_speed=(self.weight/self.age*10)
		return running_speed;
	def fight(self,Dog):
		if self.run_speed()>Dog.run_speed():
			print(self.name ,"won the fight")
		elif self.run_speed()<Dog.run_speed():
			print(Dog.name ,"won the fight")
		else:
			print("Tie Case")


