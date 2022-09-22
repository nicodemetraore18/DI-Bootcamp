#Exo 6
"""
1Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
2Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
3Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
4Call the function make_great().
5Call the function show_magicians() to see that the list has actually been modified.

"""

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(users):
    for user in users:
        print(user)
print("---------------function make_great()--------------")
def make_great(users):
    add=" the Great"
    for i in range(len(magician_names)) :
        magician_names[i]+=add
        
print("-------------la function show_magicians--------------------")
make_great(magician_names)
print("-------------la function make_great()--------------------")
show_magicians(magician_names)