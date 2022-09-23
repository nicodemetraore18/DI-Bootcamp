"""
Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

1.Instantiate three Cat objects using the code provided above.
2.Outside of the class, create a function that finds the oldest cat and returns the cat.
3.Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.


"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1=Cat("Mousse",3);
cat2=Cat("Moussis",5);
cat3=Cat("Mousso",1);

def OldestCat(Catlist):
  Age=0
  for cat in Catlist:
    if cat.age>Age:
      name=cat.name
      Age=cat.age
  for cat in Catlist:
    if cat.age==Age:

      return cat

print(f"The oldest cat is {OldestCat([cat1,cat2,cat3]).name} and is {OldestCat([cat1,cat2,cat3]).age} old")