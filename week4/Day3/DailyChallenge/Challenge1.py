Ask=input("Enter a word");
DIC={};
for i,v in enumerate(Ask):
	if v not in DIC:
		DIC[v]=[];
	
	DIC[v].append(i)
print(DIC)
