#
users = ["Mickey","Minnie","Donald","Ariel","Pluto"];
#1
DIC={};
for i in range(len(users)):
  DIC[users[i]]=i;
print(DIC)

#2-------------------------------------
DIC={}
for i in range(len(users)):
   DIC[i]=users[i];
print(DIC)

#3--------------------------------------
DIC={};
users.sort()
for i in range(len(users)):
  DIC[users[i]]=i;
print(DIC)

#4------------------------------------
DIC={};
for i in range(len(users)):
  if "i" in users[i]:
    DIC[users[i]]=i;
print(DIC)
DIC={};


#5------------------------------------
for i in range(len(users)):
  if (users[i])[0:1].casefold()=="m" or (users[i])[0:1].casefold()=="p":
    DIC[i]=users[i];
print(DIC)

