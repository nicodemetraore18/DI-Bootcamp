import copy
#Exercise 9: Cinemax
#1-A movie theater charges different ticket prices depending on a person’s age.
#2-Ask a family the age of each person who wants a ticket.
# family = ['zoubair','asmaoo','falilah','sudais']
# totalCost = 0
# age=0
# for name in family:
#     age = input("{} what's you age: ".format(name))
#     if int(age) < 3:
#         totalCost+=0
#     elif 3 <= int(age) <= 12:
#         totalCost+=10
#     else:
#         totalCost+=15
# print("the total cost of all the family's tiickets is: ",totalCost)


#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
group = ['moussa', 'ali','sali','Oussoumane','Razack']
groupRestricted=copy.copy(group);
for name in group:
    age = input("{} what's you age: ".format(name))
    if 16<=int(age)<=21:
        groupRestricted.remove(name)

print(groupRestricted);