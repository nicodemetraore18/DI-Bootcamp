"""
1.Create a class called Zoo.

2.In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).

3.Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.

4.Create a method called get_animals that prints all the animals of the zoo.
5.Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
6.Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


7.Create a method called get_groups that prints the animal/animals inside each group.

8.Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)

"""
class Zoo:
  
  def __init__(self,zoo_name):
  	self.name=zoo_name
  	self.animals=[]

  def add_animal(self,new_animal):
    if new_animal not in self.animals:
  	  (self.animals).append(new_animal)

  def get_animals(self):
    for animal in self.animals:
      print (animal, end=",");

  def sell_animal(self,sold):
    for animal in self.animals:
      if animal in animals:
      	animals.remove(animal)

  def sort_animals(self):
    dico = {}
    trier = sorted(self.animals)
    res=[]
    x=[]
    for i in trier:
      if i[0] not in x:
        x.append(i[0])
    for i in x:
      p=[]
      for j in trier:
        if j[0]==i:
          p.append(j)
      res.append(p)
    for k,v in enumerate(res):
      dico[k+1]=v
    return dico
 
  def get_group (self):
  	for value in self.sort_animals():
  	  print(value)

ramat_gan_safari = Zoo("zogona")
x=""
while True:
  x=input("Which animal should we add to the zoo or write \"q\" to exit: ")
  if x == "q": break
  ramat_gan_safari.add_animal(x)
ramat_gan_safari.get_animals()
#y = input("\nwhat animal do you want to sell: ")
#ramat_gan_safari.sell_animal(y)
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()