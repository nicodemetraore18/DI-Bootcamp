#Exercise 11 : Sandwich Orders#2

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []
print("the deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
for sandwich in sandwich_orders:
    print("I made your {}".format(sandwich))
    finished_sandwiches.append(sandwich)
print("there is the list of your sandwitch made: ",finished_sandwiches)

