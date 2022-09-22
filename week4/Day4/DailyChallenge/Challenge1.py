Matrix=[

["7","i","3"],
["T","s","i"],
["h","%","x"],
["i"," ","#"],
["s","M"," "],
["$","a"," "],
["#","t","%"],
["^","r","!"],


]
decode=[];
for cpt in range(len(Matrix[0])):
 for i in Matrix:
  if i[cpt].isalpha()==True:
   decode.append(i[cpt])
  else:
   decode.append("");
cpt+=1;
 
decoded=' '.join(decode)
print(decoded)