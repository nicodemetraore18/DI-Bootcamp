#
TotalCost=0;
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key,value in family.items():
  if value<3:
    print (key+" must pay:0$\n");
    TotalCost+=0;
  elif value>3 and value<12 :
    print (key+" must pay:10$\n");
    TotalCost+=10;
  elif value>12:
    print (key+" must pay:15$\n");
    TotalCost+=15;
  else:
    break;

print("The total cost for the movies is {}$".format(TotalCost));

#bonnus

familly1={};
while True:
  ToDO=input("Type 'quit' to exit the entering family's members or Enter to add member")
  if ToDO=='quit':
   break;
  else:
   askName=input("Enter the name of the family's member");
   askAge=input("Enter his or her age");
   familly1[askName]=askAge;

print(familly1.items())

