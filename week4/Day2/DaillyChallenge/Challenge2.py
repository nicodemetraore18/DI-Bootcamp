#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

mot = input("user's word: ")
n = len(mot)
mot=list(mot.rstrip())
if n<2:
    print(''.join(mot))
else:
    j=0
    for i in range(n):
        if (mot[j]!=mot[i]):
            j+=1
            mot[j]=mot[i]
    j+=1
    mot = mot[:j]        
print(''.join(mot))