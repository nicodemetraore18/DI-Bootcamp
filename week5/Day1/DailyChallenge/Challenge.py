class farm:

  def __init__(self,name):
    self.name=name;
    self.DicAnimal={}
    

  def add_animal(self,AnimalToAdd, number=1):
    if AnimalToAdd in self.DicAnimal.keys():
      self.DicAnimal[AnimalToAdd]+=number;
    else:
      self.DicAnimal[AnimalToAdd]=number

  def get_info(self):
    print(f"{self.name}'s farm");
    for key ,value in self.DicAnimal.items():
      print(key,":",value)
    print("\n\t E-I-E-I-O!");
    return ;

  def get_animal_types(self):
    types=[]
    for key in self.DicAnimal.keys():
      types.append(key)
    types.sort()
    return types

  def get_short_info(self):
    print(f"{self.name}'s farm has :", end=" ")
    length=len(self.get_animal_types())
    for i in range(length):
      if i==length-2:
        print(self.get_animal_types()[i],end=" and ")
      elif i==length-1:
        print(self.get_animal_types()[i],".")
      else:
        print(self.get_animal_types()[i],end=",")



macdonald = farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('cow')
macdonald.add_animal('horse',5)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()
    