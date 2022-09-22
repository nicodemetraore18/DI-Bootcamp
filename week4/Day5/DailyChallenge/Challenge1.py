list1=input("Entrez des mot separe par une virgule");
list2=list1.split(",").copy()
list2.sort()
print(','.join(list2))