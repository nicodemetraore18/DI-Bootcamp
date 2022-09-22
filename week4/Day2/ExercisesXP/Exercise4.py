# What is a float? What is the difference between an integer and a float?
#a float is a  decimal number, the different with a string is that it has two part integer and decimal!
import random
# Can you think of another way to generate a sequence of floats?
print(random.uniform(10,100))
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
number=[];
for i in range(1,5):
   number.append(i+0.5);
   number.append(i+0.5+0.5);

print(number)