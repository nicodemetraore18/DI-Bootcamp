#Exercise 8: Who Ordered A Pizza ?
listtopping = []
topping=''

while True:
    topping=input("Enter a topping of pizza: ")
    listtopping.append(topping)
    Res=input("Would you like to add a topping to the pizza: ")
    if Res=='quit':
        break
    
#calculate the total price of the pizza:
totalPrice = (10+2.5)*len(listtopping)
    
print("the all toppings on the pizza pie is ",listtopping," and the total price is: ",totalPrice)

