number = int(input("give a number: "))
length = int(input("give a length: "))
liste = []
for i in range(1,length+1):
    liste.append(number*i)
print(f"number: {number} - length: {length} => ",liste)