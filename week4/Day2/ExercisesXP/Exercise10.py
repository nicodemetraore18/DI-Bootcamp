#Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your {}".format(sandwich))
    finished_sandwiches.append(sandwich)
print("there is the list of your sandwitch made: ",finished_sandwiches)