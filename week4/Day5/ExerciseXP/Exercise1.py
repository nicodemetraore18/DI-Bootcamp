#beautifull sup
# init p function (facultative)
#*********************************************************************************
p=[[" "," "," "],[" "," "," "],[" "," "," "],]
def initMatrix(Matrix):
	Matrix=[[" "," "," "],[" "," "," "],[" "," "," "],]

p=[[" "," "," "],[" "," "," "],[" "," "," "],]
cordls=[];
restart=""
#Function to start the game
#*********************************************************************************


#Function to display the play board
#*************************************************************************
def display_board():

 print(f"*************************")
 print(f"*   {p[0][0]}   |   {p[0][1]}   |   {p[0][2]}   *")
 print(f"*-------|-------|-------*")
 print(f"*   {p[1][0]}   |   {p[1][1]}   |   {p[1][2]}   *")
 print(f"*-------|-------|-------*")
 print(f"*   {p[2][0]}   |   {p[2][1]}   |   {p[2][2]}   *")
 print(f"*************************")


#Function player_input
#*************************************************************************

def player_input(plyr):
 
 #Taking Rows and Column
 print(f"Player {plyr}'s turn ...");
 row=input("Enter row :");
 column=input("Enter column :");
 while(row,column) in cordls or int(row)>2 or int(column)>2 :
  print(f"{plyr} This position has been choosen or position conflict! choose another position");
  row=input("Enter row :");
  column=input("Enter column :");
 cordls.append((row,column));
 p[int(row)][int(column)]=plyr;

#Function Check_win()
#*************************************************************************
def check_win():
 # cette fonction verifie a chaque coup s'il  n'y a pas de gagnant
 winner_exist=False
 ligne=[];
 colon=[];
 dia1=[];
 dia2=[];
 #row verification
 for row in p:
  for x in row:
   ligne.append(x);
  if ligne[0]==ligne[1]==ligne[2]!=" ":
   print(f"{ ligne[0] } is the winner")
   winner_exist=True;
   return winner_exist;

 #column verification
 for i in range(3):
  for row in p:
   colon.append(row[i])
  if colon[0]==colon[1]==colon[2]!=" ":
  	print(f"{ colon[0] } is the winner")
  	winner_exist=True;
  	return winner_exist;

 #dia1 verification
 for i in range(3):
  dia1.append(p[i][i])
 if dia1[0]==dia1[1]==dia1[2]!=" ":
  print(f"{ dia1[0] } is the winner")
  winner_exist=True;
  return winner_exist;
 #dia2 verification 
 for i in range(3):
  dia2.append(p[i][2-i])
 if dia2[0]==dia2[1]==dia2[2]!=" ":
  print(f"{ dia2[0] } is the winner")
  winner_exist=True;
  return winner_exist;
 return winner_exist;

def play():
 #Les joueurs choisissent leur mark
 print("************THE GAME IS RUNNIG******************\nLet both the both player choose a mark ! Expected mark alpha")
 plyr1=input("What's your mark player1");
 plyr2=input("What's your mark player2");
 
 #Verification:la mark doit etre une lettre de l'alphabet
 while plyr1.isalpha() == False or plyr2.isalpha() == False or plyr1==plyr2:
  if plyr1==plyr2:
   print("choose differents mark")
  else:
   print("Please Enter a valid mark")
  plyr1=input("What's your mark player1");
  plyr2=input("What's your mark player2");
 
 #Affichage du tableau de jeu vide
 display_board()
 
 #Turning player
 for i in range(9):
  if i%2==0:
   player_input(plyr1)
   display_board()
   if check_win() :
    return 1;

  else:
   player_input(plyr2)
   display_board()
   if check_win() :
   	return 1;
  #tie case   
  if i==8 and check_win()==False :
   print ("The game end in a Tie No winner!!")


play()
