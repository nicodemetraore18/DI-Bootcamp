import random
#1
ask=input('Enter a string');
while len(ask)!=10:

  if (len(ask)<10):
	  print("string not long enough");
  elif(len(ask)>10):
	  print("string too long")
  ask=input('Enter a new string');


#2
print("The first char of {} is {} and the last one is:{}".format(ask,ask[0],ask[9]));
#3
ask1=input('Enter another string');

for x in range(len(ask1)):
	print(ask1[0:x+1])
#bonus
ask2=input('Enter another string');

n=''.join(random.sample(ask2,len(ask2)))
print("new string : "+n)