
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20",
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

while True:
  Ask=input("Type 'quit' to exit or Enter to purchase");
  if Ask.casefold()=="quit":
    break
  else:
    wallet=input("Enter the amount you have in your wallet");
    list_Product=[];
    for key,value in items_purchase.items():
      price=value[1:]
      if float(price) <= float(wallet):
        list_Product.append(key);
      else:
        pass;
    print(sorted(list_Product));

